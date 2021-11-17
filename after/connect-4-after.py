# Henry Pacheco Xavier Markowitz


import turtle

def make_window(window_title, bgcolor, dimensions):

    window = turtle.getscreen()
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(dimensions["width"], dimensions["height"])
    window.tracer(0)
    return window 

def make_turtle(shape, color, turtle_size, point):
    turt = turtle.Turtle()
    turt.speed(0)
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(turtle_size["width"], turtle_size["length"])
    turt.penup()
    turt.goto(point["x"],point["y"])
    return turt


def teleport(turt, point):

    turt.up()
    turt.goto(point["x"], point["y"])
    turt.down()

def draw_grid(grid, turt, point, tile_size):

    teleport(turt, point)

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            scaled_point = {"x": point["x"] + col * tile_size,
                            "y": point["y"] - row * tile_size}
            teleport(turt, scaled_point)

            if grid[row][col] == 1:
                turt.dot(tile_size-5, "red")
            
            elif grid[row][col] == 2:
                turt.dot(tile_size-5, "yellow")
            
            else:
                turt.dot(tile_size-5, "white")
