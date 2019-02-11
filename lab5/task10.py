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
        """Adds a point."""
        return point(self.x+other.x,self.y+other.y)

def main():
    p1=point(10)
    p2=point(10,20)
    print(p1)
    print(p2)
    print(p1+p2)

if __name__ == '__main__':
    main()
