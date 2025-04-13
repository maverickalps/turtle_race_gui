import turtle 
tim = turtle.Turtle()


def fd():
    tim.forward(10)
def bk():
    tim.back(10)
def anticlck():
    tim.left(10)
def clck():
    tim.right(10)
def clear():
    tim.reset()
turtle.onkey(key = "w" , fun = fd )
turtle.onkey(key = "s" , fun = bk)
turtle.onkey(key = "a" , fun = anticlck)
turtle.onkey(key = "d" , fun = clck)
turtle.onkey(key = "c" , fun =clear )
turtle.listen()

turtle.exitonclick()