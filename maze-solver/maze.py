from window import Window
from cell import Cell
from point import Point


class Maze:
    def __init__(self, x1, y1, n_cols, n_rows, cell_size, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__n_rows = n_rows
        self.__n_cols = n_cols
        self.__cell_size = cell_size
        self.__window = window
        self._create_cells()

    def _create_cells(self):
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

        for col in self.__cells:
            for cell in col:
                cell.draw()
