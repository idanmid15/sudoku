
from board import board_length, Board
from movement import guess_cell_valid


def recursive_solve(board, row, column, digit, solution):

    # We have placed all digits in all rows, thus found a solution.
    if digit > board_length:
        solution[0] = board.clone()
        return True

    # We have placed the current digit in all rows, move on to the next digit.
    if row >= board_length:
        return recursive_solve(board, 0, 0, digit + 1, solution)

    # We could not find a proper cell to place this digit in the current row.
    if column >= board_length:
        return False

    # The digit was already placed in this row, on partially filled board inputs.
    if board.get_cell(row, column) == digit:
        return recursive_solve(board, row + 1, 0, digit, solution)

    # It is illegal to place this digit in the cell, try the next one.
    if not guess_cell_valid(board, row, column, digit):
        return recursive_solve(board, row, column + 1, digit, solution)
    board.set_cell(row, column, digit)

    # Try solving by placing the digit in the current cell or trying in the next one
    if recursive_solve(board, row + 1, 0, digit, solution):
        return True
    else:
        board.clear_cell(row, column)
        return recursive_solve(board, row, column + 1, digit, solution)


def solve_game_naive(board):
    solution = {}
    if recursive_solve(board, 0, 0, 1, solution):
        print("\n".join(str(x) for x in solution[0]))
    else:
        print("No solution found for {}".format(board))


if __name__ == '__main__':
    empty_board = Board()
    easy_board = Board([[2, '-', 6, 3, '-', '-', '-', '-', 4],
                        ['-', '-', 3, 6, 7, 1, 2, '-', 9],
                        [5, 1, '-', '-', '-', 4, 6, '-', 3],
                        [4, 3, '-', '-', 6, '-', '-', 7, 2],
                        [1, 7, '-', 4, '-', '-', 9, 3, '-'],
                        [9, '-', '-', 7, 3, 5, '-', '-', 8],
                        ['-', 8, 1, '-', '-', 7, 3, 9, '-'],
                        ['-', '-', 9, 8, 1, '-', 4, 2, '-'],
                        ['-', 2, 4, '-', 9, 3, '-', 6, '-']])
    hardest_board = Board([[8, '-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', 3, 6, '-', '-', '-', '-', '-'],
                           ['-', 7, '-', '-', 9, '-', 2, '-', '-'],
                           ['-', 5, '-', '-', '-', 7, '-', '-', '-'],
                           ['-', '-', '-', '-', 4, 5, 7, '-', '-'],
                           ['-', '-', '-', 1, '-', '-', '-', 3, '-'],
                           ['-', '-', 1, '-', '-', '-', '-', 6, 8],
                           ['-', '-', 8, 5, '-', '-', '-', 1, '-'],
                           ['-', 9, '-', '-', '-', '-', 4, '-', '-']])
    print("A trivial empty board's solution:")
    solve_game_naive(empty_board)
    print("An easy board's solution:")
    solve_game_naive(easy_board)
    print("The hardest board ever created's solution(this may take some time:")
    solve_game_naive(hardest_board)
