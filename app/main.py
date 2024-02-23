from classes.maze import Maze
from classes.window import Window

def main():
    w = Window(800, 600)
    m = Maze(100, 100, 5, 2, 100, w)
    w.wait_for_close()
    
main()