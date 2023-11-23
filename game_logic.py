class Connect4Game:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(f' {cell} |', end='')
            print('\n' + '-' * (4 * self.columns - 1))

    def make_move(self, column):
        if not 0 <= column < self.columns:
            raise ValueError("Column number must be between 1 and 7.")
        
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return self.check_winner(row, column)
        return None

    def check_winner(self, row, column):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 4):
                r, c = row + dr * i, column + dc * i
                if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r, c = row - dr * i, column - dc * i
                if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 4:
                return self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None
