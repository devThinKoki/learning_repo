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
    negative_min = 0 - len(computer_pieces)
    positive_max = len(computer_pieces)

    while True:
        random_number = random.randint(negative_min, positive_max)
        # if random_number == 0:
        #     print('Pop from the Stock...')
        # else:
        #     print(f'{computer_pieces[abs(random_number)-1]} is Chosen...')
        if random_number == 0:
            if not stock_pieces:
                return 'draw'
            stock_pieces, popped_piece = pop_from_stock(stock_pieces)
            computer_pieces.append(popped_piece)
            break
        if is_violate_rule(computer_pieces, domino_pieces, random_number):
            # print('\tChosen piece is violating the rule....')
            continue

        popped_piece = pop_from_pieces('computer', random_number)
        update_number_cnt(popped_piece)
        if random_number < 0:
            domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, -1)
            break
        else:
            domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, 1)
            break

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