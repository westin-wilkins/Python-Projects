import random

# This program rolls two dice for both the player and computer and compares
# the sum. It then compares the two values and decides who won the round.
# This program also uses try/except to catch invalid responses. 

# Keeps track of score for the duration of the game.
player_score = 0
computer_score = 0

while True:
    # Dice for both the player and computer. Player and computer result values 
    # made to make win condition code more readable.
    player_dice = [random.randint(1, 6), random.randint(1, 6)]
    computer_dice = [random.randint(1, 6), random.randint(1, 6)]
    player_result = player_dice[0] + player_dice[1]
    computer_result = computer_dice[0] + computer_dice[1]
    user = input('Enter "y" or "n" to play the game: ')
    print(' ')
    # Quits the game after giving the final results.
    if user == 'n':
        print('The final score is:')
        print(f'Player score: {player_score} Computer score {computer_score}')
        if player_score > computer_score:
            print('You won the game!')
        elif player_score == computer_score:
            print("It's a tie!")
        else:
            print('You lost. Try again next time!')
        print(' ')
        print('Thanks for playing!')
        break
    # Rolls the dice.
    elif user == 'y':
        print("You rolled")
        print(f'{player_dice}')
        
        print(' ')
        
        print("The computer rolled")
        print(f'{computer_dice}')
    # Adds the player and computers dice and decides who won and who lost. 
        if player_result > computer_result:
            print('You win!')
            player_score += 1
        elif player_result == computer_result:
            print("It's a tie!")
        else:
            print('You Lose!')
            computer_score += 1
    else:
        print('Input a valid response.')

        
        
            