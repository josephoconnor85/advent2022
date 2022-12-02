
# DAY ONE - PART ONE
with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    
    most_calories = 0
    current_calories = 0

    for line in lines:
        if line == '':
            if current_calories > most_calories:
                most_calories = current_calories
            current_calories = 0
            continue
        current_calories += int(line)

    print(most_calories)

# DAY ONE - PART TWO
with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    
    # represent the top 3 elves as 'min', 'mid', and 'top'
    min = 0
    mid = 0
    top = 0

    current_calories = 0

    for line in lines:
        if line == '':
            if current_calories > top:
                min = mid
                mid = top
                top = current_calories
                current_calories = 0
                continue
            if current_calories > mid:
                min = mid
                mid = current_calories
                current_calories = 0
                continue
            if current_calories > min:
                min = current_calories
                current_calories = 0
                continue
            current_calories = 0
            continue
        current_calories += int(line)

    total_top_three = min + mid + top

    print(total_top_three)
