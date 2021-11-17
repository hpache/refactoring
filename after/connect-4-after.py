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

def check_winner(grid, player):

    if check_rows(grid, player) == True:
        return True
    elif check_cols(grid, player) == True:
        return True
    elif check_diagonals(grid, player) == True:
        return True
    else:
        return False

def check_rows(grid, player):

    count = 0

    for row in range(len(grid)):
        count = 0
        for col in range(len(grid[0])):
            if grid[row][col] == player:
                count += 1
                if count == 4:
                    return True
                else:
                    count = 0
                
def check_cols(grid, player):

    count = 0

    for col in range(len(grid[0])):
        count = 0
        for row in range(len(grid)):
            if grid[row][col] == player:
                count += 1
                if count == 4:
                    return True
                else:
                    count = 0

def check_diagonals(grid, player):

    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):

            if row + 3 < len(grid) and col + 3 < len(grid[row]):
                if grid[row][col] == 1\
                and grid[row+1][col+1] == 1\
                and grid[row+2][col+2] == 1\
                and grid[row+3][col+3] == 1:
                    return True


# setting up the window
window = make_window("Connect 4", "light sky blue", 800, 600)


# the grid
grid = []

for rows in range(5):
    grid.append([0]*7)

# drawing_turtle
my_turtle = make_turtle('classic', "white", 1, 1, 0, 0 )

x_offset = -150
y_offset = 200
tile_size = 50

player_1_turn = True

def make_move(point, player_1_turn):

    row = int(abs((point['x'] - y_offset - 25) // (50) + 1))
    col = int(abs((point['y'] - x_offset - 25) // (50) + 1))

    if player_1_turn == True:
        grid[row][col] = 1
    else:
        grid[row][col] = 2

    if player_1_turn == True:
        player_1_turn = False
    else:
        player_1_turn = True

window.onscreenclick(make_move)
window.listen()

def main():

    global player_1_turn
    
    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)
    while True:

        selected_row = int(input("enter row, player "+ str(turn) +": "))
        selected_col = int(input("enter col, player "+ str(turn) +": "))

        if grid[selected_row][selected_col] == 0:

            if player_1_turn == True:
                grid[selected_row][selected_col] = 1
            else:
                grid[selected_row][selected_col] = 2

        draw_grid(grid, my_turtle, -150, 200, 50)
        window.update()

        if check_winner(grid, 1):
            print("player 1 won")

        elif check_winner(grid, 2):
            print("player 2 won")

        if player_1_turn == True:
            player_1_turn = False
        else:
            player_1_turn = True

if __name__ == "__main__":
	main()