import math




# PART ONE
with open("input.txt") as my_file:
    x = 1
    cycle_number = 1
    important_cycles = [20,60,100,140,180,220]
    important_signals = []
    lines = my_file.read().splitlines()

    for line in lines:

        if cycle_number in important_cycles:
                important_signals.append(cycle_number * x)
        if line == "noop":
            cycle_number += 1
        else:
            adder = int(line[5:])
            x += adder
            cycle_number += 2

    print(sum(important_signals))

# PART TWO
with open("input.txt") as my_file:
    x = 1
    cycle_number = 1
    new_lines = [1,41,81,121,161,201, 240]
    
    lines = my_file.read().splitlines()

    max_rows = 6
    current_row = 1
    current_line = 0
    current_pixel = 0
    output = [
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    ]

   
    while current_line < len(lines):
        print("Current Line is ", current_line)
        if current_row > max_rows:
            break
   
        ln = lines[current_line]

        if ln == "noop":
            
            print("noop")
            print("cycle no ",cycle_number)
            print("X is ", x)
            # only one cycle
            horiz_num = cycle_number - (new_lines[current_row - 1]) + 1
            print("Horiz", horiz_num)
            if x in range(horiz_num - 1, horiz_num + 2):
                new_str = list(output[current_row - 1])
                print("replace")
                new_str[current_pixel] = '█'
            
                output[current_row - 1] = "".join(new_str)
            current_pixel += 1
            cycle_number += 1


        else:
            # first cycle
            print("add1")
            print("Cycle No is", cycle_number)
            print("X is ", x)
            horiz_num = cycle_number - (new_lines[current_row - 1]) + 1
            print("Horiz", horiz_num)
            if x in range(horiz_num - 1, horiz_num + 2):
                new_str = list(output[current_row - 1])
                print("replace")
                new_str[current_pixel] = '█'
                output[current_row - 1] = "".join(new_str)
            current_pixel += 1
            if cycle_number >= new_lines[current_row]:
                current_row += 1
                current_pixel = 0
            cycle_number += 1

            # second cycle
            print("add2")
            print("Cycle No is",cycle_number)
            
            adder = int(ln[5:])
            x += adder
            print("X is ", x)
            horiz_num = cycle_number - (new_lines[current_row - 1]) + 1
            print("Horiz", horiz_num)
            if x in range(horiz_num - 1, horiz_num + 2):
                new_str = list(output[current_row - 1])
                new_str[current_pixel] = '█'
                print("replace")
                output[current_row - 1] = "".join(new_str)
            current_pixel += 1
            cycle_number += 1

        
        current_line += 1
        
        if cycle_number >= new_lines[current_row]:
            current_row += 1
            current_pixel = 0
        print("#############################")

    
    print(f"{output[0]}\n{output[1]}\n{output[2]}\n{output[3]}\n{output[4]}\n{output[5]}")