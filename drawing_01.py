import turtle
import math
import random


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


turtle.speed(0)
answer = 'y'
x_init = 0
y_init = 0
R = 50
r = 22
angle = 360 / 7
gotoxy(0, 0)
draw_circle(80, 'white')
gotoxy(0, 160)
draw_circle(5, 'red')

while answer not in ['N', 'n']:
    answer = turtle.textinput("Continue? ", "Y/N")
    if answer == 'y':
        for i in range(0, random.randrange(7, 100)):
            angle_rad = angle * i * math.pi / 180
            x_curr = R*math.sin(angle_rad)
            y_curr = R*math.cos(angle_rad)
            gotoxy(x_init + x_curr, y_init + y_curr + 60)
            draw_circle(r, 'brown')
            draw_circle(r, 'white')

        gotoxy(x_init + x_curr, y_init + y_curr + 60)
        draw_circle(r, 'brown')

    else:
        pass
