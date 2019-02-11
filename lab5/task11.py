class point():
    """"Represents a point in 2-D space.
        Prints X and Y coordinates
        Adds two points
        """
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "X:Y-%.2d:%.2d"%(self.x,self.y)
    def __add__(self,other):
        """Adds a Point or tuple."""
        if isinstance(other, point):
            return self.add_points(other)
        else:
            return self.add_points_tuple(other)
    def add_points(self,other):
        """Adds a point."""
        return point(self.x+other.x,self.y+other.x)
    def add_points_tuple(self,other):
        """Adds a tuple."""
        return point(self.x+other[0],self.y+other[1])

def main():
    p1=point(10)
    p2=point(10,20)
    print(p1)
    print(p2)
    print(p1+p2)
    print(p1+(20,30))

if __name__ == '__main__':
    main()
