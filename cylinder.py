from body import Body
from box import Box


class Cylinder(Body):
    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    @property
    def dimension(self):
        return 3

    @property
    def diameter(self):
        return max(2 * self.radius, self.height)

    def is_inside(self, point):
        x, y, z = point
        return (
            0 <= z <= self.height and
            x * x + y * y <= self.radius * self.radius
        )

    def get_bounding_box(self):
        lower_left = (-self.radius, -self.radius, 0)
        upper_right = (self.radius, self.radius, self.height)
        return Box(lower_left, upper_right)
