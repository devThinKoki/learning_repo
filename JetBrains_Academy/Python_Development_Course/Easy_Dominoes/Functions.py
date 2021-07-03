def interface(stock_pieces, computer_pieces, player_pieces, domino_pieces):
    # Print the header using seventy equal sign characters (=).
    print('='*70)
    # Print the number of dominoes remaining in the stock – Stock size: [number].
    print(f'Stock size: {len(stock_pieces)}')
    # Print the number of dominoes the computer has – Computer pieces: [number].
    print(f'Computer pieces: {len(computer_pieces)}\n')
    
    # Print the domino snake. At this stage, it consists of the only starting piece.
    if len(domino_pieces) <= 6:
        for piece in domino_pieces:
            print(piece, end = '')
    else:
        for i in range(3):
            print(domino_pieces[i], end = '')
        print('...', end = '')
        for j in range(-3, 0):
            print(domino_pieces[j], end = '')
    print()
    
    # Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
    print("\nYour pieces:")
    for i, piece in enumerate(player_pieces):
        print(f'{i + 1}:{piece}')
    print()
    return

def print_result(winner):
    if winner == 'draw':
        result = "Status: The game is over. It's a draw!"
    else:
        result = f'Status: The game is over. {winner} won!'
    print(result)

def pop_from_stock(stock_pieces):
    # global stock_pieces
    popped_piece = stock_pieces.pop()
    return stock_pieces, popped_piece 

def place_to_domino_snake(domino_pieces, popped_piece, direction):
    # global domino_pieces
    idx, edge, inserting_idx = -1, 1, len(domino_pieces) 
    if direction == -1:
        idx, edge, inserting_idx = 0, 0, 0
    if need_change_orientation(domino_pieces, idx, edge, popped_piece):
        domino_pieces.insert(inserting_idx, popped_piece[::-1])
    else:
        domino_pieces.insert(inserting_idx, popped_piece)
    return domino_pieces

def need_change_orientation(domino_pieces, idx, edge, piece):
    if domino_pieces[idx][edge] == piece[idx + 1]:
        return False
    return True

def change_turn(status):
    if status == 'computer':
        return 'player'
    else:
        return 'computer'
# 05:
def calculate_rarity(rarity_pieces, pieces1, pieces2):
    for piece in pieces1:
        ele1, ele2 = piece[0], piece[1]
        rarity_pieces[ele1] += 1
        rarity_pieces[ele2] += 1
    for piece in pieces2:
        ele1, ele2 = piece[0], piece[1]
        rarity_pieces[ele1] += 1
        rarity_pieces[ele2] += 1
    return rarity_pieces
#################### Boolean check methods #########################

def is_game_over(winner, computer, player, domino, status, num_cnt):
    if domino[0][0] == domino[-1][1] and num_cnt[domino[0][0]] == 8:
        if status == 'computer':
            winner = 'The computer' 
        else:
            winner = 'You'
        return winner
    if not computer:
        winner = 'The computer'
        return winner
    if not player:
        winner = 'You'        
        return winner
    return False

def is_valid(user_input):
    valid = True
    if user_input == '': 
        valid = False
    elif user_input.isdigit():
        valid = True
    elif user_input[0] == '-':
        if not user_input[1:].isdigit():
            valid = False
    else:
        valid = False
    return valid

# Rule: the numbers on the ends of the two neighboring dominoes must match each other
# So, check whether one of the chosen piece(related to given number)'s number matches with the number of the edge
# return False if it obey the rule
# return True if it disobey the rule
# def is_violate_rule(pieces_of, domino_pieces, number):
#     # change the number to absolute value
#     direction, end = -1, 1
#     if number < 0:
#         number = abs(number)
#         direction, end = 0, 0

#     if domino_pieces[direction][end] in pieces_of[number-1]:
#         return False
#     return True

    ###########################################
def is_violate_rule(*args):
    if isinstance(args[0], int):
        piece_max_rarity_idx = args[0]
        temp_pieces = args[1]
        domino_pieces = args[2]
        print(f'piece_max_rarity_idx: {piece_max_rarity_idx}')
        if domino_pieces[0][0] in temp_pieces[piece_max_rarity_idx]: 
            return False
        elif domino_pieces[-1][1] in temp_pieces[piece_max_rarity_idx]:
            return False
        return True
        
    else:
        pieces_of = args[0]
        domino_pieces = args[1]
        number = args[2]
        direction, end = -1, 1
        if number < 0:
            number = abs(number)
            direction, end = 0, 0

        if domino_pieces[direction][end] in pieces_of[number-1]:
            return False
        return True
