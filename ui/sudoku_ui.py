
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import tkinter.messagebox
from board import empty_sign, Board
from solver import game_solvable, recursive_solve_improved
from movement import guess_cell_valid

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuUi(Frame):
    """
       The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, parent, board):
        self.parent = parent
        self.board = board
        self.original_board = board.get_all_cells()
        Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        self.__init_ui()

    def __init_ui(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear answers",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)
        self.__draw_grid()
        self.__draw_puzzle()
        self.canvas.bind("<Button-1>", self.__cell_clicked)  # Left-click
        self.canvas.bind("<Key>", self.__key_pressed)
        
    def __clear_answers(self):
        self.board = Board(self.original_board)
        self.canvas.delete("victory")
        self.__draw_puzzle()

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)  # Vertical line

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)  # Horizontal line

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                current_cell_value = self.board.get_cell(i, j)
                if current_cell_value != empty_sign:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    original_cell_value = self.original_board[i][j]
                    color = "black" if current_cell_value == original_cell_value else "sea green"
                    self.canvas.create_text(
                        x, y, text=current_cell_value, tags="numbers", fill=color
                    )

    def __cell_clicked(self, event):
        if self.board.is_full():
            return
        x, y = event.x, event.y
        if MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
            self.canvas.focus_set()
            row, col = int((y - MARGIN) / SIDE), int((x - MARGIN) / SIDE)
            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.board.get_cell(row, col) == empty_sign:
                self.row, self.col = row, col
                
        self.__draw_cursor()
                
    def __key_pressed(self, event):
        if self.board.is_full():
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            input_num = int(event.char)
            if guess_cell_valid(self.board, self.row, self.col, input_num):
                self.board.set_cell(self.row, self.col, input_num)
                if not game_solvable(self.board, recursive_solve_improved):
                    tkinter.messagebox.showinfo("Alert",
                                                "The cell value of {} which was entered makes the board unsolvable!"
                                                .format(input_num))
                    self.board.set_cell(self.row, self.col, empty_sign)
                self.col, self.row = -1, -1
                self.__draw_puzzle()
                self.__draw_cursor()
                if self.board.is_full():
                    self.__draw_victory()
            else:
                tkinter.messagebox.showinfo("Alert",
                                            "The cell value of {} which was entered is illegal!".format(input_num))
                self.board.set_cell(self.row, self.col, empty_sign)

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __draw_victory(self):
        # create a oval (which will be a circle)
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="winner",
            fill="white", font=("Arial", 32)
        )


if __name__ == '__main__':
    root = Tk()
    SudokuUi(root, Board())
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()
