
from zone_validation import is_valid, empty_sign
from board import Board


def guess_cell_valid(board, row, column, guessed_value):
    """
    Receives a board and the next guess movement and checks whether it is valid.
    :param board: the given board.
    :param row: the given row to change.
    :param column: the given column to change.
    :param guessed_value: the given value to check for validity.
    :return: whether or not the given move is valid.
    """
    if not board.is_cell_empty(row, column):
        return False
    return_value = False
    board.set_cell(row, column, guessed_value)
    row_square, column_square = int(row / 3), int(column / 3)
    if is_valid(board.get_row(row)) and is_valid(board.get_column(column)) and is_valid(board.get_square(
            row_square, column_square)):
        return_value = True
    board.clear_cell(row, column)
    return return_value


if __name__ == '__main__':
    test_board = Board([['-', 8, 2, '-', 1, '-', '-', '-', '-'],
                  ['-', '-', 7, 2, '-', '-', '-', 3, 4],
                  ['-', '-', '-', '-', '-', 7, '-', '-', '-'],
                  [9, '-', '-', '-', 5, '-', 7, '-', '-'],
                  ['-', 6, '-', 1, '-', '-', 3, '-', '-'],
                  ['-', '-', '-', 4, '-', 2, '-', '-', '-'],
                  ['-', '-', '-', 6, '-', '-', 1, 2, '-'],
                  [8, '-', '-', '-', '-', '-', '-', 6, '-'],
                  ['-', 3, '-', 5, '-', 9, '-', '-', 8]])
    print(guess_cell_valid(test_board, 2, 1, 9))  # True
    test_board.set_cell(2, 1, 9)
    print(guess_cell_valid(test_board, 2, 1, 9))  # False
    test_board.clear_cell(2, 1)
    print(guess_cell_valid(test_board, 2, 1, 3))  # False

