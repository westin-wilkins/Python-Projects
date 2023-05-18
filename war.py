import random
from time import sleep

# For program that is relatively more complicated than my other projects. 
# I plan on coming back to it to make improvements in readability.

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def main(cards):
    player_deck = 26
    computer_deck = 26
    while player_deck != 0 or computer_deck != 0:
        user = input('Want to play War? y or n: ')
        # For quitting the game.
        if user == 'n':
            if player_deck > computer_deck:
                print('You won the game!')
                print(' ')
                print('Thanks for playing!')
            else:
                print('You lost. Try again next time!')
                print(' ')
                print('Thanks for playing!')
            break
        # Start game.
        elif user == 'y':
            print('Dealing cards')
            print('.')
            sleep(1)
            print('..')
            sleep(1)
            print('...')
            sleep(1)
            player_draw = [random.choice(cards)]
            computer_draw = [random.choice(cards)]
            print(f'Player draws: {player_draw} Computer draws: {computer_draw}')
            # If player beats the computer.
            if player_draw > computer_draw:
                print(' ')
                print('You won the round')
                player_deck += 1
                computer_deck -= 1
                print(f'Player Deck: {player_deck} Computer Deck: {computer_deck}')
                print(' ')
            # If computer beats the player.
            elif player_draw < computer_draw:
                print(' ')
                print('You lost the round!')
                player_deck -= 1
                computer_deck += 1
                print(f'Player Deck: {player_deck} Computer Deck: {computer_deck}')
                print(' ')
            # If there is a tie.
            elif player_draw == computer_draw:
                print("It's a tie!")
                sleep(1)
                print(f'Player Deck: {player_deck} Computer Deck: {computer_deck}')
                print('Dealing again')
                sleep(1)
                i = 1
                i += 1
                # Keeps reiterating until somebody wins and awards the winner
                # with i number of cards.
                while player_draw == computer_draw:
                    player_draw = [random.choice(cards)]
                    computer_draw = [random.choice(cards)]
                    print(f'Player draw: {player_draw} Computer draw: {computer_draw}')
                    print(' ')
                    if player_draw > computer_draw:
                        print(' ')
                        print(f'You won the war! You took {i} cards.')
                        player_deck += i
                        computer_deck -= i
                        print(f'Player Deck: {player_deck} Computer Deck: {computer_deck}')
                        break
                    elif player_draw < computer_draw:
                        print(' ')
                        print(f'You lost the war! The computer took {i} cards')
                        player_deck -= i
                        computer_deck += i
                        print(f'Player Deck: {player_deck} Computer Deck: {computer_deck}')
                        break
            # Losing condition.
            if player_deck <= 0:
                print('You ran out of cards. Try again next time!')
                break
            # Winning condition.
            elif computer_deck <= 0:
                print('The computer ran out of cards. You won!')
                break
        # For invalid inputs.
        else:
            print('Please input a valid response')

if __name__ == '__main__':
    main(cards)
