# Description
    # A good game needs a good interface. 
    # In this stage, you will make your output user-friendly.

    # The player should be able to see the domino snake, the so-called playing field, and their own pieces. 
    # It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.

    # Two things must remain hidden from the player: 
    # the stock pieces and the computer's pieces. 
    # The player should not be able to see them, only the number of pieces remaining.

# Objectives
    # Print the header using seventy equal sign characters (=).
# print('='*70)
    # Print the number of dominoes remaining in the stock – Stock size: [number].
# print(f'Stock size: [{len(stock_pieces)}]')
    # Print the number of dominoes the computer has – Computer pieces: [number].
# print(f'Computer pieces: [{len(computer_pieces)}]')
    # Print the domino snake. At this stage, it consists of the only starting piece.
# print(domino_pieces)
    # Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
# for piece in player_pieces:
# print(piece)
# Print the status of the game:
# print(f'Status: {status}')
    # If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
# if status == 'computer':
# print('Computer is about to make a move. Press Enter to continue...')
# status = 'player'
    # If status = "player", print "Status: It's your turn to make a move. Enter your command."
# if status == 'player':
# print('It's your turn to make a move. Enter your command')
# status = 'computer'
    # Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.

from Creation import *
from Functions import interface, display_turns
pieces = create_shuffled_pieces()
stock_pieces, computer_pieces, player_pieces, domino_pieces, status = distribute_pieces(pieces)
interface(stock_pieces, computer_pieces, player_pieces, domino_pieces)

print(f'\nStatus:', end= ' ')
# If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
if status == 'computer':
    print('Computer is about to make a move. Press Enter to continue...')
    # status = 'player'
# If status = "player", print "Status: It's your turn to make a move. Enter your command."
elif status == 'player':
    print("It's your turn to make a move. Enter your command")
    # status = 'computer'