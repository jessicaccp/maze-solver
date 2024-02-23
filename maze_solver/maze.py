from window import Window
from cell import Cell
from point import Point
import time


class Maze:
    """A class used to represent a Maze."""

    __x1: float
    __y1: float
    __n_rows: int
    __n_cols: int
    __cell_size: float
    __window: Window | None
    __cells: list[list[Cell]]

    def __init__(self, x1: float, y1: float, n_cols: int, n_rows: int,
                 cell_size: float, window: Window | None = None):

        # The top left coordinate
        self.__x1 = x1
        self.__y1 = y1

        self.__n_rows = n_rows
        self.__n_cols = n_cols
        self.__cell_size = cell_size
        self.__window = window
        self.__create_cells()

    def get_cells(self) -> list[list[Cell]]:
        return self.__cells

    def __create_cells(self) -> None:
        """Create and draw the initial state of the Maze Cells."""

        self.__cells = []

        for x in range(1, self.__n_cols + 1):
            self.__cells.append([])

            for y in range(1, self.__n_rows + 1):
                self.__cells[x - 1].append(Cell(
                    Point(self.__x1 + self.__cell_size * (x - 1),
                          self.__y1 + self.__cell_size * (y - 1)),
                    Point(self.__x1 + self.__cell_size * x,
                          self.__y1 + self.__cell_size * y),
                    self.__window))

                self.__draw_cell(x - 1, y - 1)

    def __draw_cell(self, i: int, j: int) -> None:
        """Draw the Cell and update the Window."""

        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self) -> None:
        """Display the moves on the Window."""

        assert self.__window is not None, "window is None"
        self.__window.redraw()
        time.sleep(0.05)
