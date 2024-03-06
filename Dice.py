import random

while True:
    dice = input('What kind of die would you like to use?' 
                 '\nPlease select one of the following (d4, d6, d10, d20, d100): ').lower()
    if dice == 'd4':
        max_value = 4
        break
    if dice == 'd6':
        max_value = 6
        break
    if dice == 'd10':
        max_value = 10
        break
    if dice == 'd20':
        max_value = 20
        break
    if dice == 'd100':
        max_value = 100
        break
    else:
            print('INVALID die selection')

def roll():
    min_value = 1
    global max_value
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input('Enter the number of players (1-6): ')
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 6:
            for y in range(players):
                input('What is your name? ')
            break
        else:
            print('Please select a number 1-6: ')
    else:
        print('INVALID # of players')

while True:
    num_dice = input('Enter the number of die to roll (1-10): ')
    if num_dice.isdigit():
        num_dice = int(num_dice)
        if 1 <= num_dice <= 10:
            break
        else:
            print('Please select a number 1-10: ')
    else:
        print('INVALID # of die')

max_score = int(input('Please enter the maximum score: '))
player_scores = [0 for x in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print(player_index + 1, ', it is your turn!\n')
        print('Your total score is: ', player_scores[player_index], '\n')
        current_score = 0

        while True:
            desire_roll = input('Would you like to roll ' + str(num_dice) + ' ' + str(dice) + '? (y or n): ')
            if desire_roll.lower() != 'y':
                break

            value = num_dice*roll()
            if value == 1*num_dice:
                print('CRITICAL FAILURE \n It is now', players,"'s turn.")
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a total of ', value)

            print('Your score is: ', current_score)

    player_scores[player_index] += current_score


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(winning_idx, ' is the winner with a score of: ', max_score)