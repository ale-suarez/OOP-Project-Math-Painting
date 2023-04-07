import numpy as np


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:(self.side + self.x), self.y:(self.side + self.y)] = self.color


class Rectangle:

    def __init__(self, w, h, x, y, color):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:(self.h + self.x), self.y:(self.w + self.y)] = self.color


def draw_random_shapes(canvas, canvas_x, canvas_y, n_objects=100):
    if n_objects > 1000:
        n_objects = 1000
    for i in range(n_objects + 1):
        x = np.random.randint(0, canvas_x)
        y = np.random.randint(0, canvas_y)
        h = np.random.randint(0, canvas_x)
        w = np.random.randint(0, canvas_y)
        red = np.random.randint(0, 250)
        blue = np.random.randint(0, 250)
        green = np.random.randint(0, 250)
        Rectangle(x=x, y=y, h=h, w=w, color=[red, blue, green]).draw(canvas)
