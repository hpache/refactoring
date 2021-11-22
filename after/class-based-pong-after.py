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

    def __init__(self, x_position, y_position, turt):
        ''' initializes a paddle with a position '''

        self.x_position = x_position
        self.y_position = y_position

        self.turt = turt

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


    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()



class Ball:
    # implements a Pong game ball

    def __init__(self, turt):
        ''' intializes a ball with default direction and position '''

        self.turt = turt
        self.ball_dx = 0.0925 #speed in x direction
        self.ball_dy = 0.0925 #speed in y direction
        self.x_position = 0
        self.y_position = 0


    def move_ball(self):


        self.setx(self.turt.xcor() + self.ball_dx)
        self.sety(self.turt.ycor() + self.ball_dy)


        if self.turt.ycor() > 290:
            self.top_bounce

        elif self.turt.ycor() < -290:
            self.bottom_bounce
    

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
    
    __score_format__ = "Player A: {}    Player B: {}"
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
    
    def set_bindings(self):
        self.window.onkeypress(paddle_1.up, "w") #when you press w run paddle_a_up
        self.window.onkeypress(paddle_1.down, "s")
        self.window.onkeypress(paddle_2.up, "Up")
        self.window.onkeypress(paddle_2.down, "Down")

    def update_ball(self):
        self.ball.move()

    def check_left_border(self, font):
        self.score_player1 += 1
        self.turt.clear()
        self.turt.write(self.__score_format__.format(self.score_player1, self.score_player2), align = self.align, font= self.font)
        self.ball.goto(0, 0)
        self.ball.ball_dx *= -1
    

def main():
    ''' the main function where the game events take place '''
    draw_game = Draw()
    window = draw_game.make_window("Pong - A CS151 Reproduction!", "black", {'width': 800, 'height' : 600})
    pen = draw_game.make_turtle("square", "white", {'width' : 1, 'height' : 1}, {'x' : 0, 'y' : 260})
    

    # paddels
    paddle_1 = Paddle(-350, 0, pen)
    paddle_2 = Paddle(350, 0, pen)

    # ball
    ball = Ball(pen)

    # Pen
    
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    pen.hideturtle()

    # Keyboard bindings
    window.listen() #Listen for keyboard input
    

    # Main game loop
    while True:
        window.update() #This is the update to offset the wn.tracer(0)

        ball.move()

        # Border checking    
        # Left and right
        if ball.xcor() > 350:
            

        elif ball.xcor() < -350:
            score_player2 += 1
            pen.clear()
            pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.ball_dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
            ball.setx(-340)
            ball.ball_dx *= -1.5
        
        elif ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
            ball.setx(340)
            ball.ball_dx *= -1.5




if __name__ == "__main__":
	main()