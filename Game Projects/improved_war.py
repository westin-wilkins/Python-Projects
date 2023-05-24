import random
from time import sleep

# This is an improved version of war.py. I broke the main function into multiple functions 
# to improve readability and reduce the complexity of the program. This program also takes
# into account face cards unlike its predecessor

def main():
    player_deck_size = 26
    computer_deck_size = 26
    # Main game loop
    while player_deck_size > 0 and computer_deck_size > 0:
        # Ask to either play War or quit out
        user_input = input("Do you want to play? (y/n): ")
        print(' ')
        print(' ')
        print(' ')
        # If y then the game starts
        if user_input.lower() == 'y':
            
            player_draw, computer_draw = create_deck()
            player_deck_size, computer_deck_size = play_round(player_deck_size, computer_deck_size)
        # If n then the game quits
        elif user_input.lower() == 'n':
            print('Thanks for playing!')
            return False
        # Deals with invalid inputs
        else:
            print('Invalid input: ' )
    # Losing/Winning conditions
    if player_deck_size == 0:
        print('You lost the game!')
    else:
        print('You won the game!')

def create_deck():
    # A list of tuples that contains information about each possible card.
    # The first element is what is displayed while the second element is used by 
    # compare_numbers() to decide the winner.
    deck = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
        ('J', 11), ('Q', 12), ('K', 13), ('A', 14)]
    # Randomly selects a tuple from the list and gives it to the player and computer
    player_draw, computer_draw = random.choice(deck), random.choice(deck)
    return player_draw, computer_draw

def play_round(player_deck_size, computer_deck_size):
    player_draw, computer_draw = create_deck()
    player_card = player_draw
    computer_card = computer_draw
    winner = compare_cards(player_card, computer_card)
    
    print(f'Player draws: {player_card[0]} Computer draws: {computer_card[0]}')
    # Takes the output from the compare_cards function and awards the winner one card
    # to their deck
    if winner == 'player':
        print('You won the round!')
        print('')
        player_deck_size += 1
        computer_deck_size -= 1
        print(f'Player Deck: {player_deck_size} Computer Deck: {computer_deck_size}')
        print('')
    elif winner == 'computer':
        print('You lost the round!')
        print('')
        player_deck_size -= 1
        computer_deck_size += 1
        print(f'Player Deck: {player_deck_size} Computer Deck: {computer_deck_size}')
        print('')
    else:
        print("It's a tie!")
        tie_break(player_draw, computer_draw, player_deck_size, computer_deck_size, num_cards = 1)
    # Returns the updated deck size of each player to the other functions
    return player_deck_size, computer_deck_size

def compare_cards(player_card, computer_card):
    # Function that figures out which player's card has the largest value and then
    # returns who won to the play_again() function, which will then award the winner with
    # one card
    player_card_value = player_card[1]
    computer_card_value = computer_card[1]
    if player_card_value > computer_card_value:
        return 'player'
    elif player_card_value < computer_card_value:
        return 'computer'
    else:
        return 'tie'

def tie_break(player_draw, computer_draw, player_deck_size, computer_deck_size, num_cards = 1):
    # Function that deals with ties. It will keep drawing cards for both players until
    # somebody wins. The amount rewarded to the winner is based on the 
    # number of draws (num_cards)
    print(f'Dealing {num_cards} card(s)')
    print(' ')
    player_draw_war , computer_draw_war = create_deck()
    print(f'Player draw: {player_draw_war[0]} Computer draw: {computer_draw_war[0]}')
    print(' ')
    if player_draw_war  > computer_draw_war :
        print(f'You won the war! You took {num_cards} cards')
        player_deck_size += num_cards
        computer_deck_size -= num_cards
        return player_deck_size, computer_deck_size
    elif player_draw_war  < computer_draw_war :
        print(f'You lost the war! The computer took {num_cards} cards')
        player_deck_size -= num_cards
        computer_deck_size += num_cards
        return player_deck_size, computer_deck_size
    else:
        # If there is another tie then the program will continue drawing cards
        return tie_break(player_draw, computer_draw, player_deck_size, computer_deck_size, num_cards + 1) 

if __name__ == '__main__':
    main()