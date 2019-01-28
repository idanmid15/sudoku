
class Board:
    def __init__(self):
        self.board = [['-' for _ in range(9)] for _ in range(9)]

    def get_cell(self, row, column):
        if not (0 <= row <= 8) or not (0 <= column <= 8):
            raise ValueError("Entered an invalid row or column: ({}, {})".format(row, column))
        return self.board[row][column]

    def set_cell(self, row, column, value):
        if not (0 <= row <= 8) or not (0 <= column <= 8):
            raise ValueError("Entered an invalid row or column: ({}, {})".format(row, column))
        if value > 9 or value < 1:
            raise ValueError("Entered an invalid cell value: {}".format(value))
        self.board[row][column] = value

    def get_row(self, row):
        if row < 0 or row > 8:
            raise ValueError("Entered an invalid row: {}".format(row))
        return self.board[row].copy()

    def get_column(self, column):
        if column < 0 or column > 8:
            raise ValueError("Entered an invalid column: {}".format(column))
        return [self.board[row][column] for row in range(len(self.board))]

    def get_square(self, square_row, square_column):
        if not (0 <= square_row <= 2) or not (0 <= square_column <= 2):
            raise ValueError("Entered an invalid square row or square column: ({}, {})"
                             .format(square_row, square_column))
        first_actual_row, first_actual_column = square_row * 3, square_column * 3

        return [self.board[first_actual_row + r][first_actual_column + c] for r in range(3) for c in range(3)]


if __name__ == '__main__':
    board = Board()
    board.set_cell(3, 4, 5)
    board.set_cell(4, 3, 1)
    board.set_cell(5, 3, 4)
    board.set_cell(5, 5, 2)
    print(board.get_square(1, 1))  # should print ['-', 5, '-', 1, '-', '-', 4, '-', 2]
    print(board.get_column(3))  # should print ['-', '-', '-', '-', 1, 4, '-', '-', '-']

