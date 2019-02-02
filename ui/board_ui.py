
from tkinter import *
from board import Board


def print_event(x, y):
    print("({}, {}), value: {}".format(x, y, board_entries[x][y].get()))


def create_board_entries(board_cells):
    entries = [i for i in board_cells]
    for i, _ in enumerate(board_cells):
        for j, _ in enumerate(board_cells[i]):
            entry = Entry(root, justify=CENTER, bd=3)
            entry.grid(row=i, column=j)
            entry.insert(END, board[i][j])
            entry.bind("<Return>", lambda event, a=i, b=j: print_event(a, b))
            entries[i][j] = entry
    return entries


if __name__ == '__main__':
    root = Tk()
    board = Board().get_all_cells()
    board_entries = create_board_entries(board)


root.mainloop()

