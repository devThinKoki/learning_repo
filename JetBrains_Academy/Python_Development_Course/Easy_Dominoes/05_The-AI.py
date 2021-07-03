# Description
    # Randomly made choices are hardly a sign of intelligence. 
    # Teach your computer to make educated decisions with the help of basic statistics. 
    # Here's how it works:

        # The primary objective of the AI is to determine which domino is the least favorable and then get rid of it. 
        # To reduce your chances of skipping a turn, you must increase the diversity of your pieces. 
        # For example, it's unwise to play your only domino that has a 3, unless there's nothing else that can be done. 
        # Using this logic, the AI will evaluate each domino in possession, based on the rarity. 
        # Dominoes with rare numbers will get lower scores, while dominoes with common numbers will get higher scores.
        ### 즉, computer AI로 하여금 가지고 있는 도미노들 중에서 적게 포함된 수에 낮은 점수를, 많이 포함된 수에 높은 점수를 부여

        # The AI should use the following algorithm to calculate the score:
            # 1. Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
            # 2. Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.
            #### 1. AI는 자신의 piece들 그리고 Domino_Pieces에 있는 0 부터 6까지의 갯수를 센다.
            #### 2. 각각의 숫자에 대한 점수는 해당숫자가 computer의 패와 Domino_Pieces에 총 몇개가 있는지와 같게 한다.
            #### 최종적으로 computer가 갖고 있는 각각의 패는 각 숫자의 점수의 합과 같게 된다.
        # The AI will now attempt to play the domino with the largest score, trying both the left and the right sides of the snake. 
        # If the rules prohibit this move, the AI will move down the score list and try another domino. 
        # The AI will skip the turn if it runs out of options.
        ### 가장 높은 점수를 갖고 있는 도미노를 먼저 왼쪽, 오른쪽에 시도하고,
        ### 룰에 위배될 경우, 차례로 가장 낮은 점수를 갖는 도미노까지 시도를 한 뒤,
        ### 마지막에 Stack_pieces에서 뽑아오는 경우를 취한다.
    
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
    
    num_freq = {i : 0 for i in range(7)}
    com_pieces_ferq = [[piece, 0] for piece in computer_pieces]
    # print(f'num_freq: {num_freq}')
    # print(f'com_pieces_ferq: {com_pieces_ferq}')
    # while True:
    num_freq = calculate_rarity(num_freq, computer_pieces, domino_pieces)
    # print(f'computer_pieces: {computer_pieces}')
    # print('='*10)
    # print(f'num_freq: {num_freq}') 
    for i in range(len(com_pieces_ferq)):
        cnt = 0
        piece = com_pieces_ferq[i][0]
        cnt += num_freq[piece[0]]
        cnt += num_freq[piece[1]]
        com_pieces_ferq[i][1] = cnt
    # print('='*10)
    temp_pieces = computer_pieces[:]
    while len(temp_pieces):
        piece_max_rarity_idx =  max(range(len(com_pieces_ferq)), key = lambda x: com_pieces_ferq[x][1])
        if com_pieces_ferq[piece_max_rarity_idx][1] < 0:
            break
        print(f'Temp_pieces: {temp_pieces}')
        print(f'Computer_pieces_rarity: {com_pieces_ferq}')
        if not is_violate_rule(piece_max_rarity_idx, temp_pieces, domino_pieces):
            print('Valid::::::::::')
            print(f'Current piece_max_rarity_idx: {piece_max_rarity_idx}')
            break
        else:
            print('Invalid::::::::::')
            com_pieces_ferq[piece_max_rarity_idx][1] = -1
            print(f'Temp_pieces changed: {temp_pieces}')
            print(f'Computer_pieces_rarity changed: {com_pieces_ferq}')
            print('='*10)
        input('check')
    if len(temp_pieces) == 0 or piece_max_rarity_idx < 0:
        if not stock_pieces:
            return 'draw'
        stock_pieces, popped_piece = pop_from_stock(stock_pieces)
        computer_pieces.append(popped_piece)
        return
    
    print(f'Current computer_pieces: {computer_pieces}')
    popped_piece = pop_from_pieces('computer', piece_max_rarity_idx + 1)
    del temp_pieces, com_pieces_ferq, piece_max_rarity_idx
    print('Popped_piece:', popped_piece)
    
    update_number_cnt(popped_piece)
    if domino_pieces[0][0] in popped_piece: 
        print('Place popped_piece to leftside of domino_pieces')
        domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, -1)
        return
    elif domino_pieces[-1][1] in popped_piece:
        print('Place popped_piece to rightside of domino_pieces')
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