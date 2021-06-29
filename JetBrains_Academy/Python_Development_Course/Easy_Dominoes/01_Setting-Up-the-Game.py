# Theory
    # Note:
        # Before you start this project, it's better to get familiar with the basic domino rules. 
        # Keep in mind that there are many versions of the game. 
        # The rules used in this particular project will be described as we go along.

        # As you might know, a domino is a playing piece that is characterized by the two numbers written on it. 
        # The numbers are integers and can range from 0 to 6. 
        # A single domino piece has no orientation, so, a full domino set (that includes all the possible pairs of numbers) will have 28 unique dominoes.

        # You may think that there should be 7*7=49 dominoes in total. 
        # However, this is not the case because the combinations like [1,2] and [2,1] are the same domino, not two separate ones.

# Description
    # To play domino, you need a full domino set and at least two players. 
    # In this project, the game is played by you and the computer.
    
    # At the beginning of the game, each player is handed 7 random domino pieces. 
    # The rest are used as stock (the extra pieces).
    
    # To start the game, players determine the starting piece. 
    # The player with the highest domino or the highest double ([6,6] or [5,5] for example) will donate that domino as a starting piece for the game. 
    # After doing so, their opponent will start the game by going first. 
    # If no one has a double domino, the pieces are reshuffled and redistributed.
    
    # Status is the player, who is to make the next move

# Objectives
#     1. Generate a full domino set. 
#        Each domino is represented as a list of two numbers. 
#        A full domino set is a list of 28 unique dominoes.
    
#     2. Split the full domino set between the players and the stock by random. 
#        You should get three parts: 
#             Stock pieces (14 domino elements), 
#             Computer pieces (7 domino elements), 
#             Player pieces (7 domino elements).
    
#     3. Determine the starting piece and the first player. 
#        Modify the parts accordingly. 
#        You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer".
#             Stock pieces      # 14 domino elements
#             Computer pieces   # 7 or 6 domino elements
#             Player pieces     # 6 or 7 domino elements
#             Domino snake      # 1 starting domino
#             Status            # the player that goes first

#     4. If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
#     Output all five variables.

# Write your code here
# Write your code here
import random

def create_pieces():
    result = []
    for i in range(0,7):
        for j in range(i, 7):
            result.append((i, j))
    return result

def shuffle(original_pieces_list):
    random.shuffle(original_pieces_list)

# if given peice's value is greater than original max piece's value return True
def check_max(max_list, given_piece):
    if type(max_list[1]) == int:
        return True

    if max_list[1][0] <= given_piece[0]:
        return True
    return False

#
def distribute_pieces(shuffled_pieces):
    # Bool: check at least one of the player has double pair piece.
    double_pair = False
    while True:
        # copy the original_shuffled_pieces
        stock_pieces = shuffled_pieces[:]
        computer_pieces, player_pieces = [], []
        status = 'computer'
        # print('stock_pieces:\n\t', stock_pieces)
        # print('computer_pieces:\n\t', computer_pieces)
        # print('player_pieces:\n\t', player_pieces)
        max = ['player', 0] # set default max value as player's with [0,0] double pair

        for i in range(7):
            popped_piece1 = stock_pieces.pop()
            computer_pieces.append(popped_piece1)
            if popped_piece1[0] == popped_piece1[1]:
                if check_max(max, popped_piece1):
                    max[0] = 'computer'
                    max[1] = popped_piece1

            popped_piece2 = stock_pieces.pop()
            player_pieces.append(popped_piece2)
            if popped_piece2[0] == popped_piece2[1]:
                if check_max(max, popped_piece2):
                    max[0] = 'player'
                    max[1] = popped_piece2
        # print('current_max: ', max)

        if type(max[1]) == tuple:
            if max[0] == 'player':
                player_pieces.remove(max[1])
                status = 'computer'
            else:
                computer_pieces.remove(max[1])
                status = 'player'
            domino_snake = [list(max[1])]
            stock_pieces = [list(piece) for piece in stock_pieces]
            computer_pieces = [list(piece) for piece in computer_pieces]
            player_pieces = [list(piece) for piece in player_pieces]

            return stock_pieces, computer_pieces, player_pieces, domino_snake, status

pieces = create_pieces()
shuffle(pieces)
sp, cp, pp, ds, s = distribute_pieces(pieces)
print('Stock pieces:', sp)
print('Computer pieces:', cp)
print('Player pieces:', pp)
print('Domino snake:', ds)
print('Status:', s)
