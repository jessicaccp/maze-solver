import unittest
import random
import sys

from tests.t_cell import T_Cell
from tests.t_line import T_Line
from tests.t_maze import T_Maze
from tests.t_point import T_Point
from tests.t_window import T_Window

from classes.point import Point
from classes.window import Window


def main():
    if len(sys.argv) < 2:
        raise Exception("missing argument")

    option = sys.argv[1]

    match (option):
        case "cell":
            cell_point1 = None
            cell_point2 = None
            cell_window = Window()
            t_cell = T_Cell(cell_point1, cell_point2, cell_window)
            # unittest.main(t_cell)

        case "line":
            line_point1 = Point()
            line_point2 = Point()
            t_line = T_Line(line_point1, line_point2)

        case "maze":
            maze_x1 = None
            maze_y1 = None
            maze_n_cols = None
            maze_n_rows = None
            maze_cell_size = None
            maze_window = Window()
            t_maze = T_Maze()

        case "point":
            point_x = None
            point_y = None
            t_point = T_Point()

        case "window":
            window_width = random.randint(0, 1000)
            window_height = random.randint(0, 1000)
            t_window = T_Window(window_width, window_height)

        case _:
            raise Exception("invalid argument")


if __name__ == "__main__":
    main()
