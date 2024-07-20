import random
import turtle as t


tim=t.Turtle()
t.colormode(255)
tim.speed("fastest")

def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    colour=(r,g,b)
    return colour
def draw_spiro(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(colors())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spiro(5)

screen=t.Screen()
screen.exitonclick()
