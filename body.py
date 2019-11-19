import abc


class Body(abc.ABC):
    @property
    @abc.abstractmethod
    def dimension(self):
        pass

    @property
    @abc.abstractmethod
    def diameter(self):
        pass

    @property
    @abc.abstractmethod
    def get_bounding_box(self):
        pass

    @abc.abstractmethod
    def is_inside(self, point):
        pass

    def get_random_point(self):
        bounding_box = self.get_bounding_box()
        point = bounding_box.get_random_point()
        while not self.is_inside(point):
            point = bounding_box.get_random_point()
        return point
