from classes.maze import Maze
from classes.window import Window

MAZE_X1 = 100
MAZE_Y1 = 100
MAZE_N_COLS = 20
MAZE_N_ROWS = 13
MAZE_CELL_SIZE = 30
MAZE_WINDOW = Window(800, 600)


def main():
    Maze(MAZE_X1, MAZE_Y1, MAZE_N_COLS,
         MAZE_N_ROWS, MAZE_CELL_SIZE, MAZE_WINDOW)
    MAZE_WINDOW.wait_for_close()


if __name__ == '__main__':
    main()
