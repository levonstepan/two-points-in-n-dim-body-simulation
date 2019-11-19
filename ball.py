# import random
from ellipsoid import Ellipsoid


class Ball(Ellipsoid):
    def __init__(self, radius, dimension=3):
        radii = (radius, ) * dimension
        super().__init__(radii)


def expected_cumulative_function(x, radius):
    if x < 0:
        return 0
    d = 2 * radius
    if x > d:
        return 1
    return 8 * x ** 3 / d ** 3 + 2 * x ** 6 / d ** 6 - 9 * x ** 4 / d ** 4
