from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(10)

def move_backward():
  tim.back(10)

def turn_right():
  tim.right(10)

def turn_left():
  tim.left(10)

def clear():
  tim.reset()

def jump():
  if tim.isdown():
    tim.up()
  else:tim.down()

screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.onkey(jump, "space")
screen.exitonclick()