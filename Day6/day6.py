
def find_marker(num):
    with open("input.txt") as my_file:
        lines = my_file.read()
        

        for idx, char in enumerate(lines):
            # start = idx + 1
            end = idx + num
            sequence = lines[idx:end]
            set_sequence = set(sequence)
            if len(set_sequence) == num:
                return end
            else:
                continue

print(find_marker(4)) # part one
print(find_marker(14)) # part two