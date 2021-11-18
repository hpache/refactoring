# Henry Pacheco Xavier Markowitz

import turtle

class draw:

    def __init__(self, num_rows, num_cols):
        self.window = None
        self.turt = None
        self.grid = [[0 for i in range(num_cols)] for i in range(num_rows)]
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.tile_size = 50
        self.x_offset = -150
        self.y_offset = 200

    def get_window(self):
        return self.window
    
    def get_turt(self):
        return self.turt
    
    def get_grid(self):
        return self.grid
    
    def get_tile_size(self):
        return self.tile_size
    
    def make_window(self, window_title, bgcolor, dimensions):

        window = turtle.getscreen()
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(dimensions["width"], dimensions["height"])
        window.tracer(0)
        self.window = window

    def make_turtle(self, shape, color, turtle_size, point):
        turt = turtle.Turtle()
        turt.speed(0)
        turt.shape(shape)
        turt.color(color)
        turt.shapesize(turtle_size["width"], turtle_size["length"])
        turt.penup()
        turt.goto(point["x"],point["y"])
        self.turt = turt

    def teleport(self, point):

        self.turt.up()
        self.turt.goto(point["x"], point["y"])
        self.turt.down()

    def draw_grid(self, point):

        self.teleport(point)

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                scaled_point = {"x": point["x"] + col * self.tile_size,
                                "y": point["y"] - row * self.tile_size}
                self.teleport(scaled_point)

                if self.grid[row][col] == 1:
                    self.turt.dot(self.tile_size-5, "red")
                
                elif self.grid[row][col] == 2:
                    self.turt.dot(self.tile_size-5, "yellow")
                
                else:
                    self.turt.dot(self.tile_size-5, "white")

class game(draw):

    def __init__(self, num_rows, num_cols):
        draw.__init__(self,num_rows, num_cols)
        self.x_offset = -150
        self.y_offset = 200
        self.player_1_turn = True
        
        
    def check_winner(self, grid, player):

        if self.check_rows(grid, player) == True:
            return True
        elif self.check_cols(grid, player) == True:
            return True
        elif self.check_diagonals(grid, player) == True:
            return True
        else:
            return False

    def check_rows(self, grid, player):

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
                    
    def check_cols(self, grid, player):

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

    def check_diagonals(self, grid, player):

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if row + 3 < len(grid) and col + 3 < len(grid[row]):
                    if grid[row][col] == player\
                    and grid[row+1][col+1] == player\
                    and grid[row+2][col+2] == player\
                    and grid[row+3][col+3] == player:
                        return True

    def make_move(self, x, y):

        row = int(abs((y - self.y_offset - 25) // (50) + 1))
        col = int(abs((x - self.x_offset - 25) // (50) + 1))

        if self.player_1_turn == True:
            self.grid[row][col] = 1
        else:
            self.grid[row][col] = 2

        self.draw_grid({"x":self.x_offset, "y":self.y_offset})
        self.window.update()

        if self.check_winner(self.grid, 1):
            print("player 1 won")
        if self.check_winner(self.grid, 2):
            print("player 2")
        
        if self.player_1_turn == True:
            self.player_1_turn = False
        else:
            self.player_1_turn = True

    def play(self):
        self.window.onscreenclick(self.make_move)
        self.window.listen()



def main():

    play_game = game(5,7)
    play_game.make_window("Connect 4", "light sky blue", {"width":800, "height":600})  
    play_game.make_turtle('classic', "white", {"width":1, "length":1}, {"x":0, "y":0})
    window = play_game.get_window()
    grid = play_game.get_grid()

    
    
    play_game.draw_grid({"x":play_game.x_offset, "y":play_game.y_offset})

    play_game.play()

    while True:

        selected_row = int(input("enter row, player "+ str(play_game.player_1_turn) +": "))
        selected_col = int(input("enter col, player "+ str(play_game.player_1_turn) +": "))

        if grid[selected_row][selected_col] == 0:

            if play_game.player_1_turn == 1:
                grid[selected_row][selected_col] = 1
            else:
                grid[selected_row][selected_col] = 2

        play_game.draw_grid({"x":play_game.x_offset, "y":play_game.y_offset})
        window.update()

        if play_game.check_winner(grid,1):
            print("player 1 won")
        if play_game.check_winner(grid,2):
            print("player 2 won")

        if play_game.player_1_turn == True:
            play_game.player_1_turn = False
        else:
            play_game.player_1_turn = True

        
        

        


        

if __name__ == "__main__":
	main()