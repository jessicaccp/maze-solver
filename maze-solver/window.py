from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point


class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__bg_color = "white"
        self.__is_running = False
        self.create_root()
        self.create_canvas()

    def create_root(self):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def create_canvas(self):
        self.__canvas = Canvas(
            self.__root, bg=self.__bg_color, width=self.__width, height=self.__height)
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
