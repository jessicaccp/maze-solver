from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    __width: float
    __height: float
    __bg_color: str
    __is_running: bool
    __root: Tk
    __canvas: Canvas

    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height
        self.__bg_color = "white"
        self.__is_running = False
        self.__create_root()
        self.__create_canvas()

    def __create_root(self) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.__close)

    def __create_canvas(self) -> None:
        self.__canvas = Canvas(
            self.__root, bg=self.__bg_color, width=self.__width, height=self.__height)
        self.__canvas.pack(fill=BOTH, expand=1)

    def __redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.__redraw()

    def __close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.__canvas, fill_color)
