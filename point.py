import random

class Point:
    """
    Represents a 2D point.
    """ #needs capital P
    def __init__(self,x,y) :
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x #define x attribute via self.x
        self.y = y #and assign the value x to it

    def __str__(self):
        """
        Magic method that is called when we say we print an instance.
        :return: <x,y>
        """
        return  f"point({self.x}, {self.y})"

    def __repr__(self):
        """
        Makes sure that it is in the correct format/ representation used.
        :return: Same format as __str__
        """
        return self.__str__() #use the same way of printing as str

    def distance_orig(self):
        """
        Calculated the distance of the point from the origin using Pythagorean theorem
        :return: Distance as a float
        """
        return (self.x**2 + self.y**2)**0.5 #square root of the sum of x

    def __gt__(self,other):
        """
        Compares points based off their distance from the origin
        :param other: Another Point instance.
        :return: True if the point if further from (0,0).
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self,other):
        """
        Checks if points are equidistant from the origin.
        :param other: Another Point instance.
        :return: True if equidistant.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance

if __name__ == "__main__":
    #now we need to instantiate it (creates a part within another thing)
    p = Point(1, 2) #p is an instance of 1 and 2
    p2 = Point(2,3)
    p4 = Point(4.4, -55)
    print(f"p.x={p.x} and p.y= {p.y}")
    print(f"p4.x={p4.x} and p4.y={p4.y}")
    p.x = 20 #can change the attributes of the instance
    print(f"p.x={p.x} and p.y= {p.y}")
    print(p)

    #create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10,10), #x value
                            random.randint(-10,10))) #y value
    print("I got these 5 random points:")
    for p in points:
        print(p) # can also just print(points)
    p = Point(3,4)
    print(p.distance_orig()) #expect 5 answers
    p2 = Point (1,1)
    print(f"I am comparing p > p2: {p>p2}") # expecting to have true
    print("The sorted list of points is:")
    points.sort()
    print(points)