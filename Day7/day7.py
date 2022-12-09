
def get_dir_name(line):
    return line[4:]

def get_cd_dest(line):
    return line[5:]

def get_file_names_and_size(line):
    return line.split(" ") 


class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.parent = None
        self.children = []

    def total_folder_size(self):
        size = 0
        for file in self.files:
            size += file.size
        return size

    def total_size_of_self_and_children(self):
        size = self.total_folder_size()
        for child in self.children:
            size += child.total_size_of_self_and_children()
        return size

    def does_child_exists(self, child_name):
        for child in self.children:
            if child.name == "child_name":
                return True
            return False

class File:
    def __init__(self, name, size = 0):
        self.name = name
        self.size = size


with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    all_dirs = []
    current_dir = Folder("/")
    all_dirs.append(current_dir)

    for line in lines:
        if line[0:7] == "$ cd ..":
            if current_dir.parent == None:
                continue
            else:
                current_dir = current_dir.parent
                continue
        if line[0:4] == "$ cd":
            new_dir_name = get_cd_dest(line)
            if not current_dir.does_child_exists(new_dir_name):
                new_dir = Folder(new_dir_name)
                new_dir.parent = current_dir
                all_dirs.append(new_dir)
                current_dir.children.append(new_dir)
                current_dir = new_dir
                continue
        if line[0:4] == "$ ls":
            continue
        if line[0:3] == "dir":
            new_dir_name = get_dir_name(line)
            if not current_dir.does_child_exists(new_dir_name):
                new_dir = Folder(new_dir_name)
                new_dir.parent = current_dir
                all_dirs.append(new_dir)
                current_dir.children.append(new_dir)
                continue
        elif line[0] in '1234567890':
            size, filename = get_file_names_and_size(line)
            f = File(filename, int(size))
            current_dir.files.append(f)

    cut_off = 100000
    total_size = 0
    for dir in all_dirs:
        curr_size = dir.total_size_of_self_and_children()
        if curr_size <= cut_off:
            total_size += curr_size

    # PART ONE SOLUTION
    print(total_size) 


    # PART TWO SOLUTION
    total_disk_space_available = 70000000
    required_unused_space = 30000000

    total_used_space = all_dirs[0].total_size_of_self_and_children()
    current_unused_space = total_disk_space_available - total_used_space
    required_deletions = required_unused_space - current_unused_space
    print(required_deletions)

    min_size = total_disk_space_available
    for dir in all_dirs:
        curr_size = dir.total_size_of_self_and_children()
        if curr_size > required_deletions:
            if curr_size < min_size:
                min_size = curr_size
                continue

    print(min_size)








    