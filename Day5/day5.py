
with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    # go through all the lines - separating the stacks, the headers, and the instructions
    stacks = []
    instructions = []

    for line in lines:
        if 'move' in line:
            instructions.append(line)
            continue
        if '[' in line:
            stacks.append(line)
            continue
        continue

    # Clean up the stacks - remove whitespaces and brackets
    adjusted_stacks = []
    for stack in stacks:
        adj_stack = []
        i = 1
        while i < len(stack):
            if stack[i] == ' ':
                adj_stack.append('*')
            else:
                adj_stack.append(stack[i])
            i += 4
        adjusted_stacks.append(adj_stack)


    # transpose the stacks
    transposed_stacks = [
        [adjusted_stacks[i][j] for i in reversed(range(len(adjusted_stacks)))
        ] for j in range(len(adjusted_stacks[0])) 
        
    ]

    for stack in transposed_stacks:
        while True:
            if stack[-1] == "*":
                remove = stack.pop()
                continue
            else:
                break


    # clean the instructions
    adjusted_instructions = []
    for instruction in instructions:
        qty_start_pos = instruction.find(" ")
        qty_end_pos = instruction.find(" fr")
        qty = int(instruction[qty_start_pos:qty_end_pos])
        origin_start_pos = instruction.find("m ") + 2
        origin_end_pos = instruction.find("to ") - 1
        origin = int(instruction[origin_start_pos:origin_end_pos])
        end_start_pos = instruction.find(" to ") + 4
        end = int(instruction[end_start_pos:])
        adjusted_instructions.append((qty,origin,end))

    def move_item(instructions):
        (remaining_moves,origin,end) = instructions
        while remaining_moves > 0:
            to_move = transposed_stacks[origin - 1].pop()
            transposed_stacks[end - 1].append(to_move)
            remaining_moves -= 1

    def move_item_as_group(instructions):
        (remaining_moves,origin,end) = instructions
        to_move = transposed_stacks[origin - 1][-remaining_moves:]
        transposed_stacks[origin - 1] = transposed_stacks[origin - 1][:-remaining_moves]
        transposed_stacks[end - 1] += to_move


    

    def part_one():
        for inst in adjusted_instructions:
            move_item(inst)
        

    def part_two():
        for inst in adjusted_instructions:
            move_item_as_group(inst)



part_one()
# part_two()

stack_heads = [stack[-1] for stack in transposed_stacks]
print(''.join(stack_heads))
    