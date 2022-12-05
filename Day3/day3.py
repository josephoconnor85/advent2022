

def get_priority(letter):
    pos = ord(letter)
    if pos < 96: # means it is a upper case letter
        return pos - 38
    else: # lower case letter
        return pos - 96

# DAY 3 - PART ONE

with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    sum_priorities = 0
    for rucksack in lines:
        rucksack_size = len(rucksack)
        
        rucksack_middle = int(rucksack_size / 2)
        rucksack_A = rucksack[0:rucksack_middle]
        rucksack_B = rucksack[rucksack_middle:]

        # go through rucksack B and convert to a dictionary
        dict_B = {ltr: get_priority(ltr) for ltr in rucksack_B}

        # go through rucksack A and see if it exits in Dict B
        for letter in rucksack_A:
            if letter in dict_B:
                sum_priorities += dict_B[letter]
                break


 # DAY 3  - PART TWO
with open("input.txt") as my_file:
    lines = my_file.read().splitlines()

    groups = []
    current_group = []
    
    for line in lines:
        current_group.append(line)
        if len(current_group) == 3:
            groups.append(current_group)
            current_group = []

    sum_group_priorities = 0


    for group in groups:
        # convert indexes 1 and 2 to dictionaries
        dict_idx_1 = {ltr: get_priority(ltr) for ltr in group[1]}
        dict_idx_2 = {ltr: get_priority(ltr) for ltr in group[2]}
    

        for letter in group[0]:
            if letter in dict_idx_1:
                if letter in dict_idx_2:
                    sum_group_priorities += dict_idx_1[letter]
                    break
    
    print(sum_group_priorities)


