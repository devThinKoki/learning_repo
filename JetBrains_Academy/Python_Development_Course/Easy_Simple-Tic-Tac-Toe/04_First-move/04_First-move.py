class TicTacToe:
    def __init__(self):    
        self.grid = [
            ["|", " ", "_", " ", "_", " ", "_", " ", "|"],
            ["|", " ", "_", " ", "_", " ", "_", " ", "|"],
            ["|", " ", "_", " ", "_", " ", "_", " ", "|"],
        ]
        self.winner = set()
        self.empty_cells = 0
        self.user_str = ''
        self.x_, self.y_ = 0, 0

    def take_input(self):
        self.user_str = input("Enter cells: ").strip()

    def user_move(self, move_str=None):
        if move_str != None:
            rows = move_str[:3], move_str[3:6], move_str[6:]
            for i in range(3):
                self.grid[i][2] = rows[i][0]
                self.grid[i][4] = rows[i][1]
                self.grid[i][6] = rows[i][2]
        else:
            while True:
                coordinates = input("Enter the coordinates: ")
                try:
                    x, y = list(map(int, coordinates.split()))
                    if x in [1, 2, 3] and y in [1, 2, 3]:
                        if self.check_coordinate_validation(x, y):
                            self.grid[x - 1][y * 2] = 'X'
                            break
                        else:
                            print('The cell is occupied! Choose another one!')
                    else:
                        print('Coordinates should be from 1 to 3!') 
                except ValueError:
                    print("You should enter numbers!")

    def check_coordinate_validation(self, x_, y_):
        if self.grid[x_ - 1][y_ * 2] == '_':
            return True
        else:
            return False

    def print_grid(self):
        print("-" * 9)
        for row in self.grid:
            print(*row, sep='')
        print("-" * 9)


game = TicTacToe()
game.take_input()
game.user_move(move_str=game.user_str)    
game.print_grid()
game.user_move()
game.print_grid()