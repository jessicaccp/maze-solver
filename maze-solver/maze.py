from window import Window
from cell import Cell
from point import Point


class Maze:
    __x1: float
    __y1: float
    __n_rows: int
    __n_cols: int
    __cell_size: float
    __window: Window
    __cells: list[list[Cell]]

    def __init__(self, x1: float, y1: float, n_cols: int, n_rows: int, cell_size: float, window: Window):
        self.__x1 = x1
        self.__y1 = y1
        self.__n_rows = n_rows
        self.__n_cols = n_cols
        self.__cell_size = cell_size
        self.__window = window
        self.__create_cells()

    def __create_cells(self) -> None:
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
        self.__cells[i][j].draw()

    def __animate(self):
        pass
