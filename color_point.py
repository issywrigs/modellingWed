

from point import Point

class ColorPoint(Point):
    """
    2D point including it's colour
    """
    def __init__(self, x,y, color):
        """
        Creates a point with colour
        :param x: x coordinate
        :param y: y coordinate
        :param color: Colour as a string
        :raises TypeError: If x or y are not numeric.
        """
        # raise an exception if we try to have not a number
        if not isinstance(x,(int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y,(int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y)  # this replaces self.x and self.y
        self.color = color

    @property
    def __str__(self):
        """
        Returns a string of the colour with the coordinate
        :return: <Colour: x,y>
        """
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint (1, 2, "red")
p.color = "rojo"
p.x = 200

print(p.distance_orig())
print(p)

#p = ColorPoint( 1, 2, "red")
#print(p)
#colors = ["red", "green", "blue", "yellow", "black", "magenta",
         # "cyan", "white", "burgundy", "periwinkle", "marsala"]

#color_points = []
#for i in range(10):
    #color_points.append(
      #  ColorPoint(random.randint(-10,10),
              #     random.randint(-10,10),
                 #  random.choice(colors)))

#print(color_points)
#color_points.sort()
#print(color_points)


