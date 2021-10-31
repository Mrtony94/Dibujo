from shapes import Point, Rectangle, Circle
from canvas import Canvas

c = Canvas()
s = Rectangle(2, 4)
c.add_shape(s)
s = Circle(5, Point(1, 2))
c.add_shape(s)
c.print_shapes()
