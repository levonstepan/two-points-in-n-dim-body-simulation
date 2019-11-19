import random
from body import Body
from utils import distance


class Box(Body):
    def __init__(self, lower_left, upper_right):
        self._lower_left = lower_left
        self._upper_right = upper_right

    @property
    def lower_left(self):
        return self._lower_left

    @property
    def upper_right(self):
        return self._upper_right

    @property
    def dimension(self):
        return len(self.lower_left)

    @property
    def diameter(self):
        return distance(self.lower_left, self.upper_right)

    def is_inside(self, point):
        return all(
            a <= x <= b for a, b, x in
            zip(self.lower_left, self.upper_right, point)
        )

    def get_bounding_box(self):
        return self

    def get_random_point(self):
        return tuple(
            random.uniform(a, b) for a, b in
            zip(self.lower_left, self.upper_right)
        )
