class TicTacToe:
    def __init__(self):    
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.continue_ = True
        self.winner = set()
        self.empty_cells = 9
        self.counts = {'X': 0, 'O': 0}
        self.turn = ['X', 'O']
        self.combinations = [
            [(0, 0), (0, 1), (0, 2)],  # combinations of cols
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],  # combinations of rows 
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],  # combinations of diagonals
            [(0, 2), (1, 1), (2, 0)]
        ]

    def print_grid(self, init=False):
        print("-" * 9)
        for row in self.rows:
            if init:
                print(f"|       |")
            else:
                print(f"| {row[0]} {row[1]} {row[2]} |")
        print("-" * 9)

    def user_move(self, player):
        while True:
            coordinates = input("Enter the coordinates: ")
            try:
                x, y = list(map(int, coordinates.split()))
                if x in [1, 2, 3] and y in [1, 2, 3]:
                    if self.check_coordinate_validation(x, y):
                        self.rows[x - 1][y - 1] = player
                        self.turn[0], self.turn[1] = self.turn[1], self.turn[0]
                        self.counts[player] += 1
                        self.empty_cells -= 1
                        break
                    else:
                        print('The cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!') 
            except ValueError:
                print("You should enter numbers!")

    def check_coordinate_validation(self, x_, y_):
        if self.rows[x_ - 1][y_ - 1] == ' ':
            return True
        else:
            return False

    def check_combinations(self, player):
        for combinations in self.combinations:
            if self.rows[combinations[0][0]][combinations[0][1]] not in self.winner:
                if all(True if self.rows[x_][y_] == player else False for x_, y_ in combinations):
                    self.winner.add(player)
                    return False

    def check_status(self):
        if len(self.winner) == 1:
            print(f"{self.winner.pop()} wins")
            self.continue_ = False
            return
        if self.empty_cells == 0:
            print('Draw')
            self.continue_ = False
            return
   
game = TicTacToe()
game.print_grid(True)
while game.continue_:
    player = game.turn[0]
    game.user_move(player)
    game.print_grid()
    game.check_combinations(player)
    game.check_status()