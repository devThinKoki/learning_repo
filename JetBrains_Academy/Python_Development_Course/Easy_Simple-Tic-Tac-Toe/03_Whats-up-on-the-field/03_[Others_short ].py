n_row = 3
cells = input("Enter cells:")

# print board
print("---------")
count = 0
while count < len(cells):
    print("|", cells[count], cells[count + 1], cells[count + 2], "|")
    count += n_row
print("---------")

# check if the difference between x and o is greater than 1
len_x = len([item for item in cells if item.lower() == "x"])
len_o = len([item for item in cells if item.lower() == "o"])
if abs(len_x - len_o) > 1:
    print("Impossible")
else:
    # create a matrix for an easier evaluation
    matrix = list()
    for index_i in range(n_row):
        row = list()
        for index_j in range(n_row):
            row.append(cells[(index_i * n_row) + index_j])
        matrix.append(row)

    # possible winning moves for a 3 x 3 matrix
    winning_moves = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]

    # check all the winning move
    result = list()
    for winning_move in winning_moves:
        partial_result = list()
        for x, y in winning_move:
            value_cell = matrix[x][y]
            if len(partial_result) == 0 or (value_cell.lower() in ["x", "o"] and value_cell in partial_result):
                partial_result.append(value_cell)
        if len(partial_result) == 3:
            result.append(partial_result[0])

    if len(result) == 1:
        print(f"{result[0]} wins")
    elif len(result) > 1:
        print("Impossible")
    elif len(result) == 0:
        # check if the board is completed
        if len_x + len_o == n_row * n_row:
            print("Draw")
        else:
            print("Game not finished")
