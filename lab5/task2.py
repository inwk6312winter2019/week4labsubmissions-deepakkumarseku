import turtle
import copy
from sample1 import point
turtle.pen(fillcolor="black", pencolor="red", pensize=10)

class rectangle():
    """Represents a rectangle.
       attributes: width, height, corner.
    """
def find_center(r):
    """Find the center of a rectangle
        r: Rectangle object.
        
        returns: center coordinates
    """
    cx=r.corner.x+(r.width/2)
    cy=r.corner.y+(r.height/2)
    return cx,cy

def move_rectangle(r,dx,dy):
    """Move the Rectangle by modifying its corner object.
        r: Rectangle object.
        dx: change in x coordinate (can be negative).
        dy: change in y coordinate (can be negative).
        returns:rectangle object
        """

    r.corner.x=r.corner.x+dx
    r.corner.y=r.corner.y+dy
    turtle.setx(r.corner.x)
    turtle.sety(r.corner.y)
    for i in range(2):
        turtle.fd(r.width)
        turtle.lt(90)
        turtle.fd(r.height)
        turtle.lt(90)
    return r

def move_rectangle1(r,dx,dy):
    """Move the Rectangle and return a new Rectangle object.
        r: Rectangle object.
        dx: change in x coordinate (can be negative).
        dy: change in y coordinate (can be negative).
        returns: new Rectangle
        """
    new = copy.deepcopy(r)
    move_rectangle(new, dx, dy)

    return new


def main():
    r = rectangle()
    r.width = 100.0
    r.height = 200.0
    r.corner = point()
    r.corner.x=50.0
    r.corner.y=50.0
    print("Center coordinates of rectangle:", find_center(r))
    r1=move_rectangle(r, 10, 5)
    print("Existing Rectangle new position corner coordinates:",r1.corner.x,r1.corner.y )
    r2=move_rectangle1(r, 100, 150)
    print("New Rectangle corner coordinates:",r2.corner.x,r2.corner.y )
    turtle.mainloop()

if __name__ == "__main__":
    main()
