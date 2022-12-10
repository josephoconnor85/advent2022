



with open("input.txt") as my_file:
    lines = my_file.read().splitlines()

    forest = []
    for line in lines:
        row = [int(char) for char in line]
        forest.append(row)

    visible_trees = 0

    for i in range(len(forest)):
        for j in range(len(forest[i])):
            current_tree = forest[i][j]
            # if we are at extremeties, we can increment answer by one and move on
            # if we are on far left:
            if j == 0:
                visible_trees += 1
                continue
            # if we are on far right:
            if j == len(forest[i]) - 1:
                visible_trees += 1
                continue
            # if we are on top:
            if i == 0:
                visible_trees += 1
                continue
            # if we are on bottom:
            if i == len(forest) - 1:
                visible_trees += 1
                continue

            # check left
            left = j - 1
            left_visible = True
            while left >= 0:
                comparison = forest[i][left]
                if comparison >= current_tree:
                    left_visible = False
                    break
                left -= 1
            if left_visible == True:
                visible_trees += 1
                continue
            # check right
            right = j + 1
            right_visible = True
            while right < len(forest[i]):
                comparison = forest[i][right]
                if comparison >= current_tree:
                    right_visible = False
                    break
                right += 1
            if right_visible == True:
                visible_trees += 1
                continue
            # check up
            up = i - 1
            up_visible = True
            while up >= 0:
                comparison = forest[up][j]
                if comparison >= current_tree:
                    up_visible = False
                    break
                up -= 1
            if up_visible == True:
                visible_trees += 1
                continue
            # check down
            down = i + 1
            down_visible = True
            while down < len(forest):
                comparison = forest[down][j]
                if comparison >= current_tree:
                    down_visible = False
                    break
                down += 1
            if down_visible == True:
                visible_trees += 1
                continue
            

           
    # Part One Solution
    print(visible_trees)

    # Part Two Solution
    def trees_visible_above(forest, row, col):
        home_value = forest[row][col]
        if row == 0:
            return 0
        viewing_distance = 0
        curr = row - 1
        while curr > -1:
            viewing_distance += 1
            if forest[curr][col] >= home_value:
                break
            curr -= 1
        return viewing_distance

    def trees_visible_below(forest, row, col):
        home_value = forest[row][col]
        if row == len(forest) - 1:
            return 0
        viewing_distance = 0
        curr = row + 1
        while curr < len(forest):
            viewing_distance += 1
            if forest[curr][col] >= home_value:
                break
            curr += 1
        return viewing_distance

    def trees_visible_left(forest, row, col):
        home_value = forest[row][col]
        if col == 0:
            return 0
        viewing_distance = 0
        curr = col - 1
        while curr > -1:
            viewing_distance += 1
            if forest[row][curr] >= home_value:
                break
            curr -= 1
        return viewing_distance

    def trees_visible_right(forest, row, col):
        home_value = forest[row][col]
        if col == len(forest[row]) - 1:
            return 0
        viewing_distance = 0
        curr = col + 1
        while curr < len(forest[row]):
            viewing_distance += 1
            if forest[row][curr] >= home_value:
                break
            curr += 1
        return viewing_distance

    def total_trees_visible(forest, row, col):
        above = trees_visible_above(forest, row, col)
        below = trees_visible_below(forest, row, col)
        left = trees_visible_left(forest, row, col)
        right = trees_visible_right(forest, row, col)

        return above * below * left * right


    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()
        forest = []
        for line in lines:
            row = [int(char) for char in line]
            forest.append(row)

        highest_scenic_score = 0

        for i in range(len(forest)):
            for j in range(len(forest[i])):
                current_scenic_score = total_trees_visible(forest, i, j)
                if current_scenic_score > highest_scenic_score:
                    highest_scenic_score = current_scenic_score

        print(highest_scenic_score)
   