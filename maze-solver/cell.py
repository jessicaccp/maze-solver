from point import Point
from window import Window
from line import Line


class Cell:
    def __init__(self, point1, point2, window):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

        self.__x1 = min(point1.x, point2.x)
        self.__x2 = max(point1.x, point2.x)
        self.__y1 = min(point1.y, point2.y)
        self.__y2 = max(point1.y, point2.y)

        self.__window = window
        self.draw()

    def draw(self):
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

    def get_middle(self, option):
        match option:
            case "x":
                return self.__x1 + (self.__x2 - self.__x1) / 2
            case "y":
                return self.__y1 + (self.__y2 - self.__y1) / 2
            case _:
                raise ValueError

    def draw_move(self, cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"

        self.__window.draw_line(Line(
            Point(self.get_middle("x"), self.get_middle("y")),
            Point(cell.get_middle("x"), cell.get_middle("y"))), color)
