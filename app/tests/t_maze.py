import unittest
from classes.maze import Maze
from classes.window import Window


class T_Maze(unittest.TestCase):
    def test_maze_init(self):
        width = 800
        height = 600
        x1 = 10
        y1 = 10
        n_cols = 10
        n_rows = 20
        cell_size = 10
        window = Window(width, height)
        maze = Maze(x1, y1, n_cols, n_rows, cell_size, window)
        maze_cells = maze.get_cells()

        self.assertEqual(
            len(maze_cells),
            n_cols,
            "Maze with different number of columns than the specified"
        )

        self.assertEqual(
            len(maze_cells[0]),
            n_rows,
            "Maze with different number of rows than the specified"
        )

    def test_maze_get_cells(self):
        pass

    def test_maze_create_cells(self):
        pass

    def test_maze_draw_cell(self):
        pass

    def test_maze_animate(self):
        pass


def test_maze():
    maze = T_Maze()
    maze.test_maze_init()
    maze.test_maze_get_cells()
    maze.test_maze_create_cells()
    maze.test_maze_draw_cell()
    maze.test_maze_animate()
