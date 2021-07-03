# Description
    # It's time to bring the game to life. 
    # In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.

    # In dominoes, you can make a move by taking one of the following actions:
        # Select a domino and place it on the right side of the snake.
        # Select a domino and place it on the left side of the snake.
        # Take an extra piece from the stock (if it's not empty) and skip a turn.

    # To make a move, the player has to specify the action they want to take. 
    # In this project, the actions are represented by integer numbers in the following manner:
        # {side_of_the_snake (+/-), domino_number (integer)} or {0}. 
    # For example:
        # -6 : Take the sixth domino and place it on the left side of the snake.
        # 6 : Take the sixth domino and place it on the right side of the snake.
        # 0 : Take an extra piece from the stock (if it's not empty) and skip a turn.

    # When it's time for the player to make a move, your program must prompt the user for a number. 
    # If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. 
    # Once the valid input is received, your program must apply the move.

    # For now, don't bother about the AI, our goal is just to make the game playable. 
    # So, when it's time for the computer to make a move, make it choose a random number between -computer_size and computer_size (where the computer_size is the number of dominoes the computer has).

    # The end-game condition can be achieved in two ways:
        # 1. One of the players runs out of pieces. 
        #    The first player to do so is considered a winner.
        # 2. The numbers on the ends of the snake are identical and appear within the snake 8 times. 
        #    For example, the snake bellow will satisfy this condition:
        #       [5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]
        #    These two snakes, however, will not:
        #       [5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]
        #       [6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]
        #    If this condition is satisfied, it is no longer possible to go on with this snake. 
        #    Even after emptying the stock, no player will have the necessary piece. 
        #    Essentially, the game has come to a permanent stop, so we have a draw.

    # When the game ends, your program should print the result.

    # Throughout the gameplay, the snake will grow in length. 
    # If it gets too large, the interface might get ugly. 
    # To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, ..., for example, [3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4].

# Objectives
    # Modify your code:
        # 1. At the end of the game, print one of the following phrases:
            # Status: The game is over. You won!
            # Status: The game is over. The computer won!
            # Status: The game is over. It's a draw!

        # 2. Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.

        # 3. Add a game loop that will repeat the following steps until the game ends:
            # - Display the current playing field (stage 2).
            # - If it's a user's turn, prompt the user for a move and apply it. 
            #   If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: 
                    # Invalid input. Please try again.
            # - If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.
            # - Switch turns.

    # Keep in mind that at this stage we have no rules! 
    # Both the player and the computer can place their dominoes however they like.

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
        # if is_violate_rule(player_pieces, domino_pieces, user_number):
        #     user_number = input('Illegal move. Please try again.\n')    
        #     continue

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