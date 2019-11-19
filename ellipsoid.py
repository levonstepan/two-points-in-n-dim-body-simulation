from body import Body
from box import Box


class Ellipsoid(Body):
    def __init__(self, radii):
        self._radii = radii

    @property
    def dimension(self):
        return len(self._radii)

    @property
    def diameter(self):
        return 2 * max(self._radii)

    def is_inside(self, point):
        return sum((x / r) ** 2 for x, r in zip(point, self._radii)) <= 1

    def get_bounding_box(self):
        lower_left = tuple(-r for r in self._radii)
        upper_right = tuple(r for r in self._radii)
        return Box(lower_left, upper_right)
