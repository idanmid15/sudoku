
from tkinter import *
import tkinter.messagebox
from board import Board, empty_sign
from solver import solve_game, recursive_solve_improved
from movement import guess_cell_valid


def entered_value(x, y):
    given_num = int(board_entries[x][y].get())
    if guess_cell_valid(board, x, y, given_num):
        board.set_cell(x, y, given_num)
        if not solve_game(board, recursive_solve_improved):
            tkinter.messagebox.showinfo("Alert", "The cell value of {} which was entered makes the board unsolvable!"
                                        .format(given_num))
            board.set_cell(x, y, empty_sign)
            board_entries[x][y].delete(0, END)
            board_entries[x][y].insert(END, empty_sign)

    else:
        tkinter.messagebox.showinfo("Alert", "The cell value of {} which was entered is illegal!".format(given_num))
        board.set_cell(x, y, empty_sign)
        board_entries[x][y].delete(0, END)
        board_entries[x][y].insert(END, empty_sign)


def create_board_entries(board_cells):
    entries = [i for i in board_cells]
    for i, _ in enumerate(board_cells):
        for j, _ in enumerate(board_cells[i]):
            entry = Entry(root, justify=CENTER, bd=3)
            entry.grid(row=i, column=j)
            entry.insert(END, board_cells[i][j])
            entry.bind("<Return>", lambda event, a=i, b=j: entered_value(a, b))
            entries[i][j] = entry
    return entries


if __name__ == '__main__':
    root = Tk()
    board = Board()
    board_entries = create_board_entries(board.get_all_cells())
    root.mainloop()
