import math
class point():
    """"Represents a point in 2-D space."""

def distance_between_points(p1,p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

def main():
    point1 = point()
    point2 = point()
    point1.x = 5
    point1.y = 10
    point2.x = 10
    point2.y = 15
    print(distance_between_points(point1, point2))

if __name__ == '__main__':
    main()
