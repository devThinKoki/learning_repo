from Creation import *
from Functions import *
import random

stop = False
number_cnt = {i:0 for i in range(7)}
shuffled_pieces = create_shuffled_pieces()
stock_pieces, computer_pieces, player_pieces, domino_pieces, status = distribute_pieces(shuffled_pieces)
number_cnt[domino_pieces[0][0]] += 2

def computer_move():
    global stock_pieces, computer_pieces, domino_pieces
    input('Computer is about to make a move. Press Enter to continue...\n')
    num_freq = {i : 0 for i in range(7)}
    com_pieces_freq = [[piece, 0] for piece in computer_pieces]
    num_freq = calculate_rarity(num_freq, computer_pieces, domino_pieces)
    for i in range(len(com_pieces_freq)):
        piece = com_pieces_freq[i][0]
        com_pieces_freq[i][1] += (num_freq[piece[0]] + num_freq[piece[1]])
    temp_pieces = computer_pieces[:]
    while len(temp_pieces):
        piece_max_rarity_idx =  max(range(len(com_pieces_freq)), key = lambda x: com_pieces_freq[x][1])
        if com_pieces_freq[piece_max_rarity_idx][1] < 0:
            break
        if not is_violate_rule(piece_max_rarity_idx, temp_pieces, domino_pieces):
            break
        else:
            com_pieces_freq[piece_max_rarity_idx][1] = -1
    if len(temp_pieces) == 0 or piece_max_rarity_idx < 0:
        if not stock_pieces:
            return 'draw'
        stock_pieces, popped_piece = pop_from_stock(stock_pieces)
        computer_pieces.append(popped_piece)
        return

    popped_piece = pop_from_pieces('computer', piece_max_rarity_idx + 1)
    del temp_pieces, com_pieces_freq, piece_max_rarity_idx

    update_number_cnt(popped_piece)
    if domino_pieces[0][0] in popped_piece:
        domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, -1)
        return
    elif domino_pieces[-1][1] in popped_piece:
        domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, 1)
        return

def player_move():
    global stock_pieces, player_pieces, domino_pieces
    user_number = input("It's your turn to make a move. Enter your command.\n")

    while True:
        # if given number is not valid continue while loop
        if not is_valid(user_number):
            # If invalid, prompt for input with error message and loop again
            user_number = input('Invalid input. Please try again.\n')
            continue

        # if given user_number is valid: make it as INTEGER type
        user_number = int(user_number)

    # option1: pop from stock_pieces
        if user_number == 0:
            if not stock_pieces:
                return 'draw'
            stock_pieces, popped_piece = pop_from_stock(stock_pieces)
            player_pieces.append(popped_piece)
            break

    # option2: if given number is out of range:
        if abs(int(user_number)) - 1 >= len(player_pieces):
            user_number = input('Invalid input. Please try again.\n')
            continue
        # if given number is violate the rule continue while loop
        if is_violate_rule(player_pieces, domino_pieces, user_number):
            user_number = input('Illegal move. Please try again.\n')
            continue

    # option3: if given number is within the range:
        # pop a piece from player_piece
        popped_piece = pop_from_pieces('player', user_number)
        # update the number_cnt variable.
        update_number_cnt(popped_piece)
        if user_number < 0:
            domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, -1)
        else:
            domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, 1)
        break

def update_number_cnt(piece):
    global number_cnt
    number_cnt[piece[0]] += 1
    number_cnt[piece[1]] += 1


def pop_from_pieces(pieces_of, number):
    global computer_pieces, player_pieces
    number = abs(number)
    if pieces_of == 'player':
        popped_piece = player_pieces.pop(number - 1)
    else:
        popped_piece = computer_pieces.pop(number -1)
    return popped_piece

def initial_display(stock_pieces, computer_pieces, player_pieces, domino_pieces, status):
    interface(stock_pieces, computer_pieces, player_pieces, domino_pieces)
    print(f'Status:', end = '')
    if status == 'computer':
        computer_move()
    else:
        player_move()
#################################
winner = ''
initial_display(stock_pieces, computer_pieces, player_pieces, domino_pieces, status)
while not stop:
    interface(stock_pieces, computer_pieces, player_pieces, domino_pieces)
    if len(domino_pieces) > 6:
        winner = is_game_over(winner, computer_pieces, player_pieces, domino_pieces, status, number_cnt)
        if winner:
            print_result(winner)
            stop = True
            status = change_turn(status)
            continue

    status = change_turn(status)

    print(f'Status:', end = ' ')
    if status == 'computer':
        if computer_move() == 'draw':
            print_result('draw')
            break
    elif status == 'player':
        if player_move() == 'draw':
            print_result('draw')
            break
