
import copy
empty_sign = '-'
board_length = 9


class Board:
    def __init__(self, existing_board=None):
        if existing_board is None:
            self.board = [[empty_sign for _ in range(board_length)] for _ in range(board_length)]
        else:
            self.board = existing_board

    def get_cell(self, row, column):
        if not (0 <= row <= board_length - 1) or not (0 <= column <= board_length - 1):
            raise ValueError("Entered an invalid row or column: ({}, {})".format(row, column))
        return self.board[row][column]

    def set_cell(self, row, column, value):
        if value == empty_sign:
            self.board[row][column] = value
        elif not (0 <= row <= board_length - 1) or not (0 <= column <= board_length - 1):
            raise ValueError("Entered an invalid row or column: ({}, {})".format(row, column))
        elif value > board_length or value < 1:
            raise ValueError("Entered an invalid cell value: {} for ({}, {})".format(value, row, column))
        self.board[row][column] = value

    def clear_cell(self, row, column):
        self.board[row][column] = empty_sign

    def is_cell_empty(self, row, column):
        return self.board[row][column] == empty_sign

    def get_row(self, row):
        if row < 0 or row > board_length - 1:
            raise ValueError("Entered an invalid row: {}".format(row))
        return self.board[row].copy()

    def get_column(self, column):
        if column < 0 or column > board_length - 1:
            raise ValueError("Entered an invalid column: {}".format(column))
        return [self.board[row][column] for row in range(len(self.board))]

    def get_square(self, square_row, square_column):
        if not (0 <= square_row <= 2) or not (0 <= square_column <= 2):
            raise ValueError("Entered an invalid square row or square column: ({}, {})"
                             .format(square_row, square_column))
        first_actual_row, first_actual_column = square_row * 3, square_column * 3

        return [self.board[first_actual_row + r][first_actual_column + c] for r in range(3) for c in range(3)]

    def get_all_cells(self):
        return copy.deepcopy(self.board)


if __name__ == '__main__':
    board = Board()
    board.set_cell(3, 4, 5)
    board.set_cell(4, 3, 1)
    board.set_cell(5, 3, 4)
    board.set_cell(5, 5, 2)
    print(board.get_square(1, 1))  # should print ['-', 5, '-', 1, '-', '-', 4, '-', 2]
    print(board.get_column(3))  # should print ['-', '-', '-', '-', 1, 4, '-', '-', '-']

