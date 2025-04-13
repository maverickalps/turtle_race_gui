import turtle as tur
tur.colormode(255)
tim = tur.Turtle()
screen = tur.Screen() 
tim.shape("turtle")
tim.color(130,120,250)
def fd():
    tim.forward(100)
    tim.circle(50)
def bk():
    tim.back(100)
tur.onkey(key = "Up", fun = fd )
tur.onkey(key = "Down", fun = bk )
tur.listen()





tur.exitonclick()   