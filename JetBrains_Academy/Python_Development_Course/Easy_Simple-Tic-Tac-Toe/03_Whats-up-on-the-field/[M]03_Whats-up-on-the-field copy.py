class TicTacToe:
    def __init__(self):    
        self.grid = []
        self.winner = set()
        self.empty_cells = 0
        self.user_str = ''
        self.possible_combinations = {
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # colom combination positions
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # row combination positions
            [0, 4, 8], [2, 4, 6] # diagonal combination positions
        }

    def take_input(self):
        self.user_str = input("Enter cells: ").strip()

    def set_grid(self):
        for i in range(0, 9, 3):
            self.grid.append([*self.user_str[i: i + 3]])        

    def print_grid(self):
        print("-" * 9)
        for row in self.grid:
            print(f'| {row[0]} {row[1]} {row[2]} |')
        print("-" * 9)
    





    def check_diagonals(self):
        if len(self.winner) == 2:
            return
        if self.grid[0][2] not in self.winner:
            if self.grid[0][2] == self.grid[1][4] == self.grid[2][6]:
                self.winner.add(self.grid[0][2])
        if self.grid[0][6] not in self.winner:
            if self.grid[0][6] == self.grid[1][4] == self.grid[2][2]:
                self.winner.add(self.grid[0][6])

    def check_rows(self):
        if len(self.winner) == 2:
            return

        for i in range(3):
            if self.grid[i][2] not in self.winner:
                if self.grid[i][2] == self.grid[i][4] == self.grid[i][6]:
                    self.winner.add(self.grid[i][2])

    def check_cols(self):
        if len(self.winner) == 2:
            return
        
        for i in range(2, 7, 2):
            if self.grid[0][i] not in self.winner:
                if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                    self.winner.add(self.grid[0][i])

    def count_empty(self):
        for i in range(3):
            for j in range(2, 7, 2):
                if self.grid[i][j] == '_':
                    self.empty_cells += 1

    def print_status(self):
        if len(self.winner) == 0:
            self.count_empty()
            if self.empty_cells == 0:
                print("Draw")
            else:
                print("Game not finished")
        elif len(self.winner) == 1:
            print(f"{self.winner.pop()} wins")
        else:
            print("Impossible")

    def valid(self):
        if abs(self.user_str.count('X') - self.user_str.count('O')) <= 1:
            return True
        return False
        
for i in range(8):
    game = TicTacToe()
    game.take_input()
    game.set_grid()
    game.print_grid()
    if game.valid():        
        game.check_diagonals()
        game.check_rows()
        game.check_cols()
        game.print_status()
    else:
        print("Impossible")

