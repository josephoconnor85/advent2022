
# Rock - A - X - 1
# Paper - B - Y - 2
# Scissors - C - Z - 3

# Win = 6, Draw = 3, Loss = 0





# DAY TWO - PART ONE
with open("input.txt") as my_file:

    score = 0
    lines = my_file.read().splitlines()
    for line in lines:
        # get own selection and get score for selection
        own_selection = line[-1]
        score_for_selection = 0
        if own_selection == 'X':
            score_for_selection = 1
        elif own_selection == 'Y':
            score_for_selection = 2
        else:
            score_for_selection = 3
        # get opponent selection
        opponent_selection = line[0]
        # compare them to see score for result
        score_for_result = 0
        if own_selection == 'X': #rock
            if opponent_selection == 'A': #rock
                score_for_result = 3
            if opponent_selection == 'C': #scissors
                score_for_result = 6
        if own_selection == 'Y': #paper
            if opponent_selection == 'B': #paper
                score_for_result = 3
            if opponent_selection == 'A': #rock
                score_for_result = 6
        if own_selection == 'Z': #scissors
            if opponent_selection == 'C': #scissors
                score_for_result = 3
            if opponent_selection == 'B': #paper
                score_for_result = 6
        # append score
        score = score + score_for_selection + score_for_result


   
    # x = lose, y = draw, z = win
   

# DAY TWO - PART TWO
with open("input.txt") as my_file:
    total_score = 0
    lines = my_file.read().splitlines()
    
    for line in lines:
        # get opponent selection
        opponent_selection = line[0]

        # get desired result
        desired_result = line[-1]

        # get scores
        if desired_result == 'X': # lose
            score_for_result = 0
            if opponent_selection == 'A': # rock - we need to play scissors
                score_for_selection = 3
            if opponent_selection == 'B': # paper - we need to play rock
                score_for_selection = 1
            if opponent_selection == 'C': # scissors - we need to play paper
                score_for_selection = 2
            
        if desired_result == 'Y': # draw
            score_for_result = 3
            if opponent_selection == 'A': # rock - we need to play rock
                score_for_selection = 1
            if opponent_selection == 'B': # paper - we need to play paper
                score_for_selection = 2
            if opponent_selection == 'C': # scissors - we need to play scissors
                score_for_selection = 3

        if desired_result == 'Z': # win
            score_for_result = 6
            if opponent_selection == 'A': # rock - we need to play paper
                score_for_selection = 2
            if opponent_selection == 'B': # paper - we need to play scissors
                score_for_selection = 3
            if opponent_selection == 'C': # scissors - we need to play rock
                score_for_selection = 1

        total_score = total_score + score_for_result + score_for_selection

    print(total_score)


       