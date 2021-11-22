'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

import turtle


class Paddle:
    # implements a Pong game paddle

    def __init__(self, x_position, y_position, draw):
        ''' initializes a paddle with a position '''

        self.x_position = x_position
        self.y_position = y_position

        self.turt = draw.make_turtle("square", "white", {"width":5, "length":1}, {"x":self.x_position, "y":self.y_position})

    def sety(self, y):
        self.turt.sety(y)
        self.y_position = y

    def up(self):
        y = self.turt.ycor()
        y += 20
        self.sety(y)


    def down(self):
        y = self.turt.ycor() #Get the current y coordinate
        y -= 20             #add 20px could also be y=y+20
        self.sety(y)
    

    def get_x_position(self):

        return self.x_position

    
    def get_y_position(self):

        return self.y_position


    def get_turtle_xcor(self):
        
        return self.turt.xcor()

    
    def get_turtle_ycor(self):
        
        return self.turt.ycor()



class Ball:
    # implements a Pong game ball

    def __init__(self, draw):
        ''' intializes a ball with default direction and position '''

        self.turt = draw.make_turtle("square", "white", {"width":1, "length":1}, {"x":0, "y":0})
        self.ball_dx = 0.925 #speed in x direction
        self.ball_dy = 0.925 #speed in y direction
        self.x_position = 0
        self.y_position = 0


    def move_ball(self):


        self.setx(self.turt.xcor() + self.ball_dx)
        self.sety(self.turt.ycor() + self.ball_dy)


        if self.turt.ycor() > 290:
            self.top_bounce()

        elif self.turt.ycor() < -290:
            self.bottom_bounce()
    

    def top_bounce(self):
    
        self.turt.sety(290)
        self.ball_dy *= -1


    def bottom_bounce(self):
        
        self.turt.sety(-290)
        self.ball_dy *= -1

    
    def get_turtle_xcor(self):
        
        return self.turt.xcor()

    
    def get_turtle_ycor(self):
        
        return self.turt.ycor()


    def teleport(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


    def setx(self, x_cor):
        ''' sets the ball x position '''
        self.turt.setx(x_cor)
        self.x_position = x_cor
    
    def sety(self, y_cor):
        ''' sets the ball x position '''
        self.turt.sety(y_cor)
        self.y_position = y_cor


class Draw:

    def __init__(self) -> None:
        pass

    def make_window(self, window_title, bgcolor, dimensions):

        window = turtle.getscreen()
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(dimensions["width"], dimensions["height"])
        window.tracer(0)
        return window


    def make_turtle(self, shape, color, turtle_size, point):
        turt = turtle.Turtle()
        turt.speed(0)
        turt.shape(shape)
        turt.color(color)
        turt.shapesize(turtle_size["width"], turtle_size["length"])
        turt.penup()
        turt.goto(point["x"],point["y"])
        return turt

class Pong:
    
    score_format = "Player A: {}    Player B: {}"
    align = "center"
    font = ("Courier", 24, "normal")

    def __init__(self, paddles, ball, window, turt):
        self.score_player1 = 0
        self.score_player2 = 0
        self.paddle_1 = paddles['player_1']
        self.paddle_2 = paddles['player_2']
        self.ball = ball
        self.window = window
        self.turt = turt
    

    def set_key_bindings(self):
        self.window.onkeypress(self.paddle_1.up, "w") #when you press w run paddle_1_up
        self.window.onkeypress(self.paddle_1.down, "s")
        self.window.onkeypress(self.paddle_2.up, "Up")
        self.window.onkeypress(self.paddle_2.down, "Down")


    def update_ball(self):
        self.ball.move_ball()


    def update_player1_score(self):
        self.score_player1 += 1
    
    
    def update_player2_score(self):
        self.score_player2 += 1
    

    def update_scoreboard(self):
        self.turt.clear()
        self.turt.write(self.score_format.format(self.score_player1, self.score_player2), align = self.align, font= self.font)


    def ball_reset(self):
        self.ball.teleport(0, 0)
        self.ball.ball_dx *= -1
    
    
    def play(self):

        self.window.update()
        self.update_ball()

        if self.ball.get_turtle_xcor() > 350:
            self.update_player1_score()
            self.update_scoreboard()
            self.ball_reset()
        
        elif self.ball.get_turtle_xcor() < -350:
            self.update_player2_score()
            self.update_scoreboard()
            self.ball_reset()


        # Paddle and ball collisions
        if self.ball.get_turtle_xcor() < -340 and self.ball.get_turtle_xcor() > -350 and self.ball.get_turtle_ycor() < self.paddle_1.get_turtle_ycor() + 50 and self.ball.get_turtle_ycor() > self.paddle_1.get_turtle_ycor() - 50:
            self.ball.setx(-340)
            self.ball.ball_dx *= -1.5
        
        elif self.ball.get_turtle_xcor() < 340 and self.ball.get_turtle_xcor() > 350 and self.ball.get_turtle_ycor() < self.paddle_2.get_turtle_ycor() + 50 and self.ball.get_turtle_ycor() > self.paddle_2.get_turtle_ycor() - 50:
            self.ball.setx(340)
            self.ball.ball_dx *= -1.5

    

def main():
    ''' the main function where the game events take place '''
    draw_game = Draw()
    window = draw_game.make_window("Pong - A CS151 Reproduction!", "black", {'width': 800, 'height' : 600})
    pen = draw_game.make_turtle("square", "white", {'width' : 1, 'length' : 1}, {'x' : 0, 'y' : 260})
    

    # paddels
    paddle_1 = Paddle(-350, 0, draw_game)
    paddle_2 = Paddle(350, 0, draw_game)

    # ball
    ball = Ball(draw_game)

    # Pen
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    pen.hideturtle()

    # game object
    game = Pong({"player_1": paddle_1, "player_2": paddle_2}, ball, window, pen)

    # Keyboard bindings
    window.listen() #Listen for keyboard input
    game.set_key_bindings()
    

    # Main game loop
    while True:
        
        game.play()





if __name__ == "__main__":
	main()