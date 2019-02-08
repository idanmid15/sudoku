
from board import board_length, Board, empty_sign
from movement import guess_cell_valid


class Solver:

    def __init__(self, board):
        # Copy the original board so we don't mutate it
        self.board = Board(board.get_all_cells())
        self.solution = {"iterations": 0, "board": []}

    def _recursive_solve_improved(self, board, row, column, digit):

        self.solution["iterations"] += 1
        # We have placed all digits in all rows, thus found a solution.
        if row >= board_length:
            self.solution["board"] = board.get_all_cells()
            return True
        if digit > board_length:
            return self._recursive_solve_improved(board, find_fullest_row(board), 0, 1)
        # We could not find a proper cell to place this digit in the current row.
        if column >= board_length:
            return False

        # The digit was already placed in this row, on partially filled board inputs.
        if board.get_cell(row, column) == digit:
            return self._recursive_solve_improved(board, find_fullest_row(board), 0, digit + 1)

        # It is illegal to place this digit in the cell, try the next one.
        if not guess_cell_valid(board, row, column, digit):
            return self._recursive_solve_improved(board, row, column + 1, digit)

        board.set_cell(row, column, digit)

        # Try solving by placing the digit in the current cell or trying in the next one
        if self._recursive_solve_improved(board, row, 0, digit + 1):
            return True
        else:
            board.clear_cell(row, column)
            return self._recursive_solve_improved(board, row, column + 1, digit)

    def _recursive_solve_naive(self, board, row, column, digit):

        self.solution["iterations"] += 1
        # We have placed all digits in all rows, thus found a solution.
        if digit > board_length:
            self.solution["board"] = board.get_all_cells()
            return True

        # We have placed the current digit in all rows, move on to the next digit.
        if row >= board_length:
            return self._recursive_solve_naive(board, 0, 0, digit + 1)

        # We could not find a proper cell to place this digit in the current row.
        if column >= board_length:
            return False

        # The digit was already placed in this row, on partially filled board inputs.
        if board.get_cell(row, column) == digit:
            return self._recursive_solve_naive(board, row + 1, 0, digit)

        # It is illegal to place this digit in the cell, try the next one.
        if not guess_cell_valid(board, row, column, digit):
            return self._recursive_solve_naive(board, row, column + 1, digit)
        board.set_cell(row, column, digit)

        # Try solving by placing the digit in the current cell or trying in the next one
        if self._recursive_solve_naive(board, row + 1, 0, digit):
            return True
        else:
            board.clear_cell(row, column)
            return self._recursive_solve_naive(board, row, column + 1, digit)

    def game_solvable(self, **kwargs):
        if kwargs["implementation"] == "naive":
            return self._recursive_solve_naive(self.board, 0, 0, 1)
        elif kwargs["implementation"] == "improved":
            return self._recursive_solve_improved(self.board, 0, 0, 1)

    def solve_game(self, **kwargs):
        if self.game_solvable(**kwargs):
            return str("\n".join(str(x) for x in self.solution["board"]) +
                       "The number of iterations taken to reach the solution: {}".format(self.solution["iterations"]))
        else:
            return False


def find_fullest_row(board):
    full_lengths = [board_length - board.get_row(row).count(empty_sign) for row in range(board_length)]
    max_val = -1
    row_idx = board_length
    for idx, value in enumerate(full_lengths):
        if value > max_val and value != 9:
            max_val = value
            row_idx = idx
    return row_idx


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
    hardest_known_board = Board([[8, '-', '-', '-', '-', '-', '-', '-', '-'],
                                 ['-', '-', 3, 6, '-', '-', '-', '-', '-'],
                                 ['-', 7, '-', '-', 9, '-', 2, '-', '-'],
                                 ['-', 5, '-', '-', '-', 7, '-', '-', '-'],
                                 ['-', '-', '-', '-', 4, 5, 7, '-', '-'],
                                 ['-', '-', '-', 1, '-', '-', '-', 3, '-'],
                                 ['-', '-', 1, '-', '-', '-', '-', 6, 8],
                                 ['-', '-', 8, 5, '-', '-', '-', 1, '-'],
                                 ['-', 9, '-', '-', '-', '-', 4, '-', '-']])
    solver = Solver(empty_board)
    print("A trivial empty board's solution with the naive approach:")
    print(solver.solve_game(implementation="naive"))
    solver = Solver(empty_board)
    print("A trivial empty board's solution with the improved approach:")
    print(solver.solve_game(implementation="improved"))
    print("An easy board's solution with the naive approach:")
    solver = Solver(easy_board)
    print(solver.solve_game(implementation="naive"))
    print("An easy board's solution with the improved approach:")
    solver = Solver(easy_board)
    print(solver.solve_game(implementation="improved"))
    print("The hardest board ever created's solution(this may take some time) with the naive approach:")
    solver = Solver(hardest_known_board)
    print(solver.solve_game(implementation="naive"))
    print("The hardest board ever created's solution(this may take some time) with the improved approach:")
    solver = Solver(hardest_known_board)
    print(solver.solve_game(implementation="improved"))
