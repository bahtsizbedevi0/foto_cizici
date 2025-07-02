import numpy as np
import turtle
import time
import os
from PIL import Image

points = np.load("foto.npy")

max_y = points[:,1].max()
points[:,1] = max_y - points[:,1]

center = points.mean(axis=0)
points = points.astype(float)
points -= center

scale = 1.5
points *= scale

screen = turtle.Screen()
screen.setup(width=1980, height=1080)
screen.bgcolor("white")
screen.tracer(False)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

for i, (x, y) in enumerate(points):
    t.goto(x, y)
    t.dot(2, "black"),
    if i % 90 == 0:
        screen.update()

screen.update()


turtle.done()
