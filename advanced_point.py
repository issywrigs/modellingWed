from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    """
    A point with both colour and distance calculated in 2D.
    """
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __init__(self, x, y, color):
        """
        Creates an advanced point if the colour is valid from the list above.
        :param x: x coordinate
        :param y: y coordinate
        :param color: from COLORS list
        :raises TypeError: If color is not allowed
        """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x=x
        self._y= y
        self._color= color

    @property
    def x(self):
        """
        Gets an x value.
        """
        return self._x # getter method

    @x.setter
    def x(self, value):
        """
        Sets x a value.
        """
        self._x = value # 'setter' method

    @property
    def y(self):
        """
        Gets a y value.
        """
        return self._y

    @classmethod # method that applies to the whole code.
    def add_color(cls, color):
        """
        Adds a new valid color for our class.
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color= "red"):
        """
        Creates a new point from a tuple rather than 2 individual values.
        """
        x, y =coordinate
        return AdvancedPoint(x,y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Returns the distance between 2 points using Pythagoras.
        """
        return((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

    def distance_2_other(self,p):
        """
        Returns the distance from this point to another.
        """
        return((self.x-p.x)**2 + (self.y-p.y)**2)**0.5


AdvancedPoint.add_color("rojo")
p = AdvancedPoint (1, 2, "blue")
p._x = 11
print(p.x)
print(p)
print(p.distance_orig())
p2=AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p,p2))



