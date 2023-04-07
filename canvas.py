import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, w, h, color=[0, 0, 0]):
        self.w = w
        self.h = h
        self.color = color

        self.data = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        self.data[:] = self.color

    def background(self, color):
        if color == 'black':
            self.color = [0, 0, 0]
        elif color == 'white':
            self.color = [255, 255, 255]
        else:
            return 'Error: Only white or black backgrounds available.'


def save_canvas(canvas_data, filename):
    img = Image.fromarray(canvas_data, 'RGB')
    img.save(filename)
