#1
from math import sqrt
S = int(input())

print(round(sqrt(S) * 4, 2))

#2
from math import pi, pow
r = int(input())
h = int(input())

V = pi * pow(r, 2) * h
print(round(V, 3))

#3
from math import ceil
N = int(input())
K = int(input())

print(ceil(N / K))

#4
from math import lcm
t1 = int(input())
t2 = int(input())

print(lcm(t1, t2))

#5
from math import gcd
A = int(input())
B = int(input())
C = int(input())

print(gcd(A, B, C))

#6
from math import sin, radians

a = int(input())
b = int(input())

max = a
for angle in range(a, b + 1):
    if sin(radians(angle)) > sin(radians(max)):
        max = angle
print(max)

#7
import turtle
from math import cos, radians, sin, pi

archimed = turtle.Turtle()
n = int(input())
a = float(input())
b = float(input())
color1 = input()
color2 = input()

archimed.color(color1)
for teta in range(n):
    r = a + b * radians(teta)
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    archimed.goto(x, y)

archimed.pu()
archimed.goto(0, 0)
archimed.pd()

archimed.color(color2)
for teta in range(n):
    r = a + b * radians(teta)
    x = r * cos(radians(teta) + pi)
    y = r * sin(radians(teta) + pi)
    archimed.goto(x, y)

turtle.done()

#8
import turtle
import math

step = int(input())
t_max = int(input())

screen = turtle.Screen()
turtle.speed(0)
turtle.hideturtle()
turtle.color("black")
turtle.penup()

t = 0
x = t * math.cos(t)
y = t * math.sin(t)
turtle.goto(x, y)
turtle.pendown()

while t <= t_max:
    x = t * math.cos(t)
    y = t * math.sin(t)
    turtle.goto(x, y)
    t += step

turtle.done()