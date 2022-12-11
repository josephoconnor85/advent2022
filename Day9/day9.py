

def tuple_to_string(tup):
    return str(tup[0]) + "-" + str(tup[1])

def update_visited_points(tail):
    txt = tuple_to_string(tail)
    if txt in visited_points:
        visited_points[txt] += 1
    else:
        visited_points[txt] = 0

def tail_catch_head(head, tail, update = False):
    head_row, head_col = head
    tail_row, tail_col = tail

    # if they are in the same row
    if head_row == tail_row:
        if abs(head_col - tail_col) <= 1:
            return tail
        if (head_col - tail_col) > 1:
            new_tail = move_pos(tail, "R")
            if update == True:
                update_visited_points(new_tail)
            return new_tail
        if (head_col - tail_col) < -1:
            new_tail = move_pos(tail, "L")
            if update == True:
                update_visited_points(new_tail)
            return new_tail

    # if they are in the same col
    if head_col == tail_col:
        if abs(head_row - tail_row) <= 1:
            return tail
        if (head_row - tail_row) > 1:
            new_tail = move_pos(tail, "U")
            if update == True:
                update_visited_points(new_tail)
            return new_tail
        if (head_row - tail_row) < -1:
            new_tail = move_pos(tail, "D")
            if update == True:
                update_visited_points(new_tail)
            return new_tail

    # if they are in different rows and columns
    if (abs(head_row - tail_row)) <= 1 and (abs(head_col - tail_col)) <= 1:
        return tail
    row_move = ""
    col_move = ""
    if (head_row - tail_row) > 0:
        row_move = "U"
    else:
        row_move = "D"
    if (head_col - tail_col) > 0:
        col_move = "R"
    else:
        col_move = "L"

    diag_move = row_move + col_move
    new_tail = move_pos(tail, diag_move)
    if update == True:
                update_visited_points(new_tail)
    return new_tail




    


    
    

def move_pos(start, dir):
    row, col = start
    # up
    if dir == "U":
        return (row + 1, col)
    # down
    if dir == "D":
        return (row - 1, col)
    # left
    if dir == "L":
        return (row, col - 1)
    # right
    if dir == "R":
        return (row, col + 1)
    # up/right
    if dir == "UR":
        return (row + 1, col + 1)
    # up/left
    if dir == "UL":
        return (row + 1, col - 1)
    # down/right
    if dir == "DR":
        return (row - 1, col + 1)
    # down/left
    if dir == "DL":
        return (row - 1, col - 1)
    

# PART ONE SOLUTION
with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    instructions = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]

    start_point = (0,0)
    start_text = tuple_to_string(start_point)
    visited_points = {start_text: 0}

    head = (0,0)
    tail = (0,0)

    for inst in instructions:
        dir, steps = inst
        for i in range(steps):
            head = move_pos(head, dir)
            tail = tail_catch_head(head, tail)



    # print(len(visited_points))

# PART TWO SOLUTION
    head = (0,0)
    body_1 = (0,0)
    body_2 = (0,0)
    body_3 = (0,0)
    body_4 = (0,0)
    body_5 = (0,0)
    body_6 = (0,0)
    body_7 = (0,0)
    body_8 = (0,0)
    tail = (0,0)

    for inst in instructions:
        dir, steps = inst
        for i in range(steps):
            head = move_pos(head, dir)
            body_1 = tail_catch_head(head, body_1)
            body_2 = tail_catch_head(body_1, body_2)
            body_3 = tail_catch_head(body_2, body_3)
            body_4 = tail_catch_head(body_3, body_4)
            body_5 = tail_catch_head(body_4, body_5)
            body_6 = tail_catch_head(body_5, body_6)
            body_7 = tail_catch_head(body_6, body_7)
            body_8 = tail_catch_head(body_7, body_8)
            tail = tail_catch_head(body_8, tail, True)

    print(len(visited_points))
