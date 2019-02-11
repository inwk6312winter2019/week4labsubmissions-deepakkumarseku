import turtle

class rectangle():
    """Represents a rectangle.
           attributes: width, height.
        """


class circle():
    """Represents a circle.
           attributes: radius.
        """
    radius=50

def draw_rect(r):
    """ Draws a rectangle with given width and height using turtle"""
    for i in range(2):
        turtle.fd(r.width)
        turtle.lt(90)
        turtle.fd(r.height)
        turtle.lt(90)

def draw_circle(c):
    """Draws a circle with given radius using turtle"""
    turtle.circle(c.radius)

def main():
    r = rectangle()
    r.width=50
    r.height=200
    c = circle()
    c.radius=50
    print(draw_rect(r))
    turtle.reset()
    print(draw_circle(c))
    turtle.mainloop()

if __name__ == '__main__':
    main()
