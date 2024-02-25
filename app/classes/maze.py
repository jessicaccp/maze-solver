from .window import Window
from .cell import Cell
from .point import Point
import time
import random


class Maze:
    """A class used to represent a Maze."""

    __x1: float
    __y1: float
    __n_rows: int
    __n_cols: int
    __cell_size: float
    __window: Window | None
    __cells: list[list[Cell]]
    __entrance: Cell
    __exit: Cell

    def __init__(self, x1: float, y1: float, n_cols: int, n_rows: int,
                 cell_size: float, window: Window | None = None,
                 seed: int | None = None):

        # The top left coordinate
        self.__x1 = x1
        self.__y1 = y1

        self.__n_rows = n_rows
        self.__n_cols = n_cols
        self.__cell_size = cell_size
        self.__window = window

        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_rec(0, 0)
        self.__reset_cells_visited()
        print(self.solve())

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

    def __break_entrance_and_exit(self) -> None:
        """Create entrance and exit of the Maze."""

        self.__entrance = self.__cells[0][0]
        self.__entrance.has_top_wall = False
        self.__draw_cell(0, 0)

        self.__exit = self.__cells[self.__n_cols - 1][self.__n_rows - 1]
        self.__exit.has_bottom_wall = False
        self.__draw_cell(self.__n_cols - 1, self.__n_rows - 1)

    def __break_walls_rec(self, i: int, j: int) -> None:
        """Break the walls of the cells to create the maze itself."""

        current = self.__cells[i][j]
        current.visited = True

        while True:
            possible_directions: list[tuple] = []

            if i - 1 >= 0:
                if not self.__cells[i - 1][j].visited:
                    possible_directions.append((i - 1, j, "left"))
            if j - 1 >= 0:
                if not self.__cells[i][j - 1].visited:
                    possible_directions.append((i, j - 1, "up"))
            if i + 1 < self.__n_cols:
                if not self.__cells[i + 1][j].visited:
                    possible_directions.append((i + 1, j, "right"))
            if j + 1 < self.__n_rows:
                if not self.__cells[i][j + 1].visited:
                    possible_directions.append((i, j + 1, "down"))

            if possible_directions == []:
                self.__draw_cell(i, j)
                return

            next_i, next_j, direction = random.choice(possible_directions)
            next: Cell = self.__cells[next_i][next_j]

            match direction:
                case "up":
                    current.has_top_wall = False
                    next.has_bottom_wall = False
                case "down":
                    current.has_bottom_wall = False
                    next.has_top_wall = False
                case "right":
                    current.has_right_wall = False
                    next.has_left_wall = False
                case "left":
                    current.has_left_wall = False
                    next.has_right_wall = False
                case _:
                    raise Exception("invalid direction")

            self.__break_walls_rec(next_i, next_j)

    def __reset_cells_visited(self) -> None:
        for list in self.__cells:
            for cell in list:
                cell.visited = False

    def solve(self) -> bool:
        return self.__solve_rec(0, 0)

    def __solve_rec(self, i: int, j: int) -> bool:
        current: Cell = self.__cells[i][j]

        self.__animate()
        current.visited = True

        if current == self.__exit:
            return True

        # right
        if i + 1 < self.__n_cols and not current.has_right_wall:
            next = self.__cells[i + 1][j]
            if not next.visited:
                current.draw_move(next)
                if self.__solve_rec(i + 1, j):
                    return True
                next.draw_move(current)

        # down
        if j + 1 < self.__n_rows and not current.has_bottom_wall:
            next = self.__cells[i][j + 1]
            if not next.visited:
                current.draw_move(next)
                if self.__solve_rec(i, j + 1):
                    return True
                next.draw_move(current)

        # left
        if i - 1 >= 0 and not current.has_left_wall:
            next = self.__cells[i - 1][j]
            if not next.visited:
                current.draw_move(next)
                if self.__solve_rec(i - 1, j):
                    return True
                next.draw_move(current)

        # top
        if j - 1 >= 0 and not current.has_top_wall:
            next = self.__cells[i][j - 1]
            if not next.visited:
                current.draw_move(next)
                if self.__solve_rec(i, j - 1):
                    return True
                next.draw_move(current)

        return False
