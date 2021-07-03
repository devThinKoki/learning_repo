import random

# create Domino Pieces
def create_shuffled_pieces():
    result = []
    for i in range(0,7):
        for j in range(i, 7):
            result.append((i, j))
    random.shuffle(result)
    return result

# give shuffled_pieces and distribut the pieces to the computer and player and return all the results.
def distribute_pieces(shuffled__pieces):
    # Bool: check at least one of the player has double pair piece.
    while True:
        stock_pieces = shuffled__pieces[:]
        # pop from stock_pieces and insert randomly chosem piece to computer and player's pieces. 
        max, stock_pieces, computer_pieces, player_pieces = pop_insert_pieces(stock_pieces)

        # escape the while loop if max_list is made.
        if type(max[1]) == tuple:
            status, domino_pieces = max[0], max[1]
            break

    if status == 'player':
        player_pieces.remove(max[1])
        status = 'computer'
    else:
        computer_pieces.remove(max[1])
        status = 'player'

    domino_pieces = [list(domino_pieces)]
    stock_pieces = [list(piece) for piece in stock_pieces]
    computer_pieces = [list(piece) for piece in computer_pieces]
    player_pieces = [list(piece) for piece in player_pieces]

    return stock_pieces, computer_pieces, player_pieces, domino_pieces, status

def pop_insert_pieces(stock_pieces):
    max, computer_pieces, player_pieces  = ['', 0], [], []

    for _ in range(7):
        popped_piece = stock_pieces.pop()
        computer_pieces.append(popped_piece)
        if popped_piece[0] == popped_piece[1]:
            if check_max(max, popped_piece):
                max[0] = 'computer'
                max[1] = popped_piece
    for _ in range(7):
        popped_piece = stock_pieces.pop()
        player_pieces.append(popped_piece)
        if popped_piece[0] == popped_piece[1]:
            if check_max(max, popped_piece):
                max[0] = 'player'
                max[1] = popped_piece
    return max, stock_pieces, computer_pieces, player_pieces


# if given peice's value is greater than original max piece's value return True
def check_max(max_list, given_piece):
    # if max_list is initial value(0) return True (allow given_piece as new max piece)
    if max_list[0] == '' or  max_list[1] == 0:
        return True
    # if given_piece's value(same value pair) is greater than original make it as new max piece
    if max_list[1][0] <= given_piece[0]:
        return True
    return False