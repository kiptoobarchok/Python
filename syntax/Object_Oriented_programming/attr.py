#!/usr/bin/python3
import math


class point:
    """
    defining a class  that represents a point in a 2D  geometric coordinates
    (cartesian plane)
    """
    def __init__(self):
        pass

    def move(self, x, y):
        """
        moves the point to a new point
        in a cartesian plane(2D)
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the points to the origin(0, 0) in the plane
        """
        self.move(0, 0)

    def distance(self, other_point):
        """
        calculates the distance between two points in the plane.

        It calculates the distance btw this point and the second one
        passed as parameter, using pythagora's theorem

        distance is returned as float
        """ 
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2
        )

    


a = point()
b = point()

a.move(3, 4)
b.move(7, 7)

print(a.x, a.y)
print(b.x, b.y)

print(a.distance(b))



