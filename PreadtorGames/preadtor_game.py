
import numpy as np


class Cube:
    def __init__(self, name, size):
        self.name = name
        self._size = size
        self._x = np.random.randint(0, self._size)
        self._y = np.random.randint(0, self._size)

        self._action_array = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

    def __str__(self):
        return f'{self.name} :({self._x}, {self._y})'

    def __sub__(self, other: "Cube"):
        return self._x - other._x, self._y - other._y

    def __eq__(self, other: "Cube"):
        return self._x == other._x and self._y == other._y

    def action(self, choose: int = None):
        if choose:
            self._move(*self._action_array[choose])
        else:
            self._move(*self._action_array[np.random.randint(0, len(self._action_array))])

    def _move(self, x: int, y: int):
        x = x if x is not None else np.random.randint(-1, 2)
        y = y if y is not None else np.random.randint(-1, 2)
        self._x += x
        self._y += y

        if self._x < 0:
            self._x = 0
        elif self._x >= self._size:
            self._x = self._size - 1

        if self._y < 0:
            self._y = 0
        elif self._y >= self._size:
            self._y = self._size - 1
