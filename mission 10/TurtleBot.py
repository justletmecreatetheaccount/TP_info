import turtle
import Robot



class TurtleBot (Robot.Robot):
    def __init__(self, nom, x, y):
        super().__init__(nom)
        self.turtle = turtle.Turtle()
        self.turtle.speed("slowest")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.setx(x)
        self.turtle.sety(y)

    def move_forward(self, distance):
        self.add_history("forward", distance)
        self.turtle.pendown()
        self.turtle.forward(distance)
        self.turtle.penup()

    def move_backward(self, distance):
        self.add_history("backward", distance)
        self.turtle.pendown()
        self.turtle.backward(distance)
        self.turtle.penup()

    def turn_left(self):
        self.add_history("left", 90)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.penup()

    def turn_right(self):
        self.add_history("right", 90)
        self.turtle.pendown()
        self.turtle.right(90)
        self.turtle.penup()


if __name__ == '__main__':

    # create robot called R2-D2 at position (100,100) and facing East,
    # to be more or less in the center of the window
    r2d2 = TurtleBot("R2-D2",100,100)



    #R2-D2@(100, 100) angle: 0.0

    r2d2.move_forward(50)
    r2d2.turn_left()

    #R2-D2@(150, 100) angle: 270.0
    r2d2.move_forward(50)
    r2d2.turn_left()

    #R2-D2@(150.0, 50.0) angle: 180.0
    r2d2.move_forward(50)
    r2d2.turn_left()

    #R2-D2@(100.0, 50.0) angle: 90.0
    r2d2.move_forward(50)

    #R2-D2@(100, 100) angle: 90.0
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.unplay()
    #r2d2.turtle.done()
    input('Press any key to exit')