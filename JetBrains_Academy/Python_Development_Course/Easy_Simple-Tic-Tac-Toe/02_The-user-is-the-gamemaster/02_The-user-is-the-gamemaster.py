# user_ = input("Enter cells: ")
class TicTacToe:
    def __init__(self):    
        self.grid = [
            ["|", " ", "_", " ", "_", " ", "_", " ", "|"],
            ["|", " ", "_", " ", "_", " ", "_", " ", "|"],
            ["|", " ", "_", " ", "_", " ", "_", " ", "|"],
        ]

    def print_grid(self):
        print("-" * 9)
        for row in self.grid:
            print(*row, sep='')
        print("-" * 9)
    
    def user_move(self, user_input):
        rows = user_input[:3], user_input[3:6], user_input[6:]
        for i in range(3):
            self.grid[i][2] = rows[i][0]
            self.grid[i][4] = rows[i][1]
            self.grid[i][6] = rows[i][2]

game = TicTacToe()
user_ = input("Enter cells: ")
game.user_move(user_)    
game.print_grid()