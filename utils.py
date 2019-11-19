import math


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
