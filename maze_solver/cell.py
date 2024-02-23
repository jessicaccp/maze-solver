from point import Point
from window import Window
from line import Line


class Cell:
    """A class used to represent a Cell of a Maze."""

    has_top_wall: bool
    has_right_wall: bool
    has_bottom_wall: bool
    has_left_wall: bool
    __x1: float
    __x2: float
    __x3: float
    __y1: float
    __y2: float
    __y3: float
    __window: Window | None

    def __init__(self, point1: Point, point2: Point,
                 window: Window | None = None):

        # Start with all four walls
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

        # Calculate the center point of the Cell given the coordinates
        # of two corners
        self.__x1 = min(point1.x, point2.x)
        self.__x2 = max(point1.x, point2.x)
        self.__x3 = self.__x1 + (self.__x2 - self.__x1) / 2
        self.__y1 = min(point1.y, point2.y)
        self.__y2 = max(point1.y, point2.y)
        self.__y3 = self.__y1 + (self.__y2 - self.__y1) / 2

        # Window in which the Cell is displayed
        self.__window = window

    def draw(self) -> None:
        """Draw the Cell walls."""

        assert self.__window is not None, "window is None"

        if self.has_top_wall:
            self.__window.draw_line(Line(
                Point(self.__x1, self.__y1),
                Point(self.__x2, self.__y1)))

        if self.has_bottom_wall:
            self.__window.draw_line(Line(
                Point(self.__x1, self.__y2),
                Point(self.__x2, self.__y2)))

        if self.has_right_wall:
            self.__window.draw_line(Line(
                Point(self.__x2, self.__y1),
                Point(self.__x2, self.__y2)))

        if self.has_left_wall:
            self.__window.draw_line(Line(
                Point(self.__x1, self.__y1),
                Point(self.__x1, self.__y2)))

    def __draw_move(self, cell: 'Cell', undo: bool = False) -> None:
        """Draw a move from a Cell to another on the Window."""

        assert self.__window is not None, "window is None"

        # Define the color of the Line
        color = "gray" if undo else "red"

        self.__window.draw_line(Line(
            Point(self.__x3, self.__y3),
            Point(cell.__x3, cell.__y3)), color)
