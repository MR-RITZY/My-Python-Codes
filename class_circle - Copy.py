class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self._radius*self._radius
    @property
    def diameter(self):
        return 2*self._radius
    @property
    def circumference(self):
        return 2*3.14*self._radius
    @property
    def radius(self):
        pass
    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError('Invalid operand literal for Circle class')
        self._radius = r
