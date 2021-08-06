cells = input('Enter cells: ').replace('_', ' ')

def win(player):
    if cells[0] == cells[1] == cells[2] == player or \
            cells[3] == cells[4] == cells[5] == player or \
            cells[6] == cells[7] == cells[8] == player or \
            cells[0] == cells[3] == cells[6] == player or \
            cells[1] == cells[4] == cells[7] == player or \
            cells[2] == cells[5] == cells[8] == player or \
            cells[0] == cells[4] == cells[8] == player or \
            cells[2] == cells[4] == cells[6] == player:
        return True
    else:
        return False


def check_game_state(string):
    # One player has too many more turns than the other
    if abs(string.count('X') - string.count('O')) > 1 or win('X') and win('O'):
        return 'Impossible'
    elif win('X'):
        return 'X wins'
    elif win('O'):
        return 'O wins'
    # Game incomplete if there are empty cells
    elif ' ' in cells:
        return 'Game not finished'
    elif not win('X') and not win('O'):
        return 'Draw'


print('---------')
for i in range(0, 9, 3):
    print('|', cells[i], cells[i + 1], cells[i + 2], '|')
print('---------')

print(check_game_state(cells))