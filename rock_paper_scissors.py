import random

# Rock, Paper, Scissors against the ai.
# The program keeps track of number of wins between the player and computer.
# Gives the score inbetween rounds.
# Inputting q when prompted gives the final score.

player_points = 0
computer_points = 0

while True:
    # Possible hands
    possible_hands = ['rock', 'paper', 'scissors']
    player_hand = input('Select either rock, paper, scissors, or q to quit: ')
    computer_hand = random.choice(possible_hands)
    print(f'Player chose {player_hand} and the computer chose {computer_hand}')

    # Case were player selects rock
    if player_hand == 'rock':
        if computer_hand == 'scissors':
            print('Rock beats scissors! You win!')
            player_points += 1 
            print(f"Player score: {player_points}")
        else:
            print('Paper beats rock! You lose!')
            computer_points += 1
            print(f"Computer's score: {computer_points}")
    
    # Case were player selects paper
    if player_hand == 'paper':
        if computer_hand == 'rock':
            print('Paper beats rock! You win!')
            player_points += 1 
            print(f"Player score: {player_points}")
        else:
            print('Scissors beat paper! You lose!')
            computer_points += 1
            print(f"Computer's score: {computer_points}")
            
    # Case were player selects scissors
    if player_hand == 'scissors':
        if computer_hand == 'paper':
            print('Scissors beat paper! You win!')
            player_points += 1
            print(f"Player score: {player_points}")
        else:
            print('Rock beats You lose!')
            computer_points += 1
            print(f"Computer's score: {computer_points}")
            
    # Case were player selects q
    if player_hand == 'q':
        print(f'The player won {player_points} games and the computer won {computer_points} games')
        if player_points > computer_points:
            print('Congradulations! You won!')
        elif player_points == computer_points:
            print("It's a tie!")
        else:
            print('The computer won. Try again next time!')
        break        
