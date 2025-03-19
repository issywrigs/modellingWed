from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        super().__init__(x,y, color)

    @classmethod # method that applies to the whole code.
    def add_color(cls, color):
        """
        Adds a new valid color for our class
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color= "red"):
        """
        Creates a new point from a tuple rather than 2 individual values
        """
        x, y =coordinate
        return AdvancedPoint(x,y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        return((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

    def distance_2_other(self,p):
        return((self.x-p.x)**2 + (self.y-p.y)**2)**0.5


AdvancedPoint.add_color("rojo")
p = AdvancedPoint (1, 2, "blue")
print(p)
print(p.distance_orig())
p2=AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p,p2))



