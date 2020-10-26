### Part 1
class Canvas():
    '''Attributes height, width'''

class Rectangle():
    '''Attributes x, y -for lower left corner, height, widht'''

canvas = Canvas()
canvas.height = 500
canvas.width = 500
canvas.color = 'white'

rect = Rectangle()
rect.x = -150
rect.y = -100
rect.width = 300
rect.height = 200

def draw_rectangle(canvas, rectangle):
    from swampy.World import World
    world = World()
    c = world.ca(width=canvas.width, height=canvas.height, background=canvas.color)
    bbox = [[rectangle.x, rectangle.y],
            [rectangle.x + rectangle.width, rectangle.y + rectangle.height]]
    c.rectangle(bbox, outline='black', width=2, fill='green4')
    world.mainloop()

# draw_rectangle(canvas, rect)

### Part 2

def draw_rectangle_v2(canvas, rectangle, color):
    from swampy.World import World
    world = World()
    c = world.ca(width=canvas.width, height=canvas.height, background=canvas.color)
    bbox = [[rectangle.x, rectangle.y],
            [rectangle.x + rectangle.width, rectangle.y + rectangle.height]]
    rectangle.color = color
    c.rectangle(bbox, outline='black', width=2, fill=rectangle.color)
    world.mainloop()

# draw_rectangle_v2(canvas, rect, 'red')

### Part 3

class Point():
    '''Attributes x, y - coordinates'''

point = Point()
point.x = 3
point.y = 5

def draw_point(canvas, point):
    from swampy.World import World
    world = World()
    c = world.ca(width=canvas.width, height=canvas.height, background=canvas.color)
    c.circle([point.x, point.y], 0)
    world.mainloop()

# draw_point(canvas, point)

### Part 4

class Circle():
    """Attributes x, y -center of the circle, and r-radius"""

circle1 = Circle()
circle1.x = 0
circle1.y = 0
circle1.r = 20

def draw_circle(canvas, circle):
    from swampy.World import World
    world = World()
    c = world.ca(width=canvas.width, height=canvas.height, background=canvas.color)
    c.circle([circle.x, circle.y], circle.r)
    world.mainloop()

draw_circle(canvas, circle1)


### Part 5

def draw_czech():
    """Draws the flag with 3 triangles and 2 rectagles"""
    from swampy.World import World
    world = World()
    canvas = world.ca(width=500, height=500, background='black')
    left = [[-150,-100], [-150, 100], [0, 0]]
    upper = [[-150, 100], [0, 100], [0,0]]
    lower = [[-150, -100], [0, -100], [0,0]]
    tri_colors = ['NavyBlue', 'white', 'red']
    upper_rect = [[0, 0], [200, 100]]
    lower_rect = [[0, -100], [200, 0]]
    polygons = [left, upper, lower]
    rects = [upper_rect, lower_rect]
    for tri, color in zip(polygons, tri_colors):
        canvas.polygon(tri, fill=color)
    for rectangular, color in zip([upper_rect, lower_rect], ['white', 'red']):
        canvas.rectangle(rectangular, outline=color, fill=color)
    world.mainloop()

draw_czech()

def draw_czech_v2():
    """Draws the flag with one triangle and 2 rectangles"""
    from swampy.World import World
    world = World()
    canvas = world.ca(width=500, height=500, background='black')
    canvas.rectangle([[-150,0], [200, 100]], outline='white', fill='white')
    canvas.rectangle([[-150,-100], [200, 0]], outline='red', fill='red')
    canvas.polygon([[-150,-100], [-150, 100], [0, 0]], fill='NavyBlue')
    world.mainloop()

draw_czech_v2()
