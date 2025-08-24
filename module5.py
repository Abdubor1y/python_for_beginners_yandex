#Module_5. While loop

#1
number = int(input())
while number > 0:
    print(number)
    number = int(input())

#2
password = input()
while len(password) < 8:
    print('Слишком простой пароль')
    password = input()
print('Хороший пароль')

#3
size_0 = int(input())
size_MAX = int(input())

size = size_0
while size < size_MAX:
    print(size)
    size *= 2

#4
length = int(input())

while length // 8 > 0:
    length //= 8
print(length)

#5
count = 0
sum_temp = 0
temperature = int(input())
while temperature >= 0:
    if temperature > 20:
        sum_temp = sum_temp + temperature
        count += 1
    temperature = int(input())
print(sum_temp // count)

#6
height = int(input())

while height != 0:
    if height % 10 == 5 and height % 3 == 0:
        print(height)
    height = int(input())

#7
import turtle
color = input()
color_2 = input()
N = int(input())
K = int(input())

mike = turtle.Turtle()
mike.speed(0)
mike.shape('turtle')
mike.pu()
mike.goto(-350, 0)
mike.setheading(0)
mike.color(color_2, color)

size = N
while size > 0:
    mike.turtlesize(size)
    mike.stamp()
    mike.forward(size * K)
    size -= 1

mike.hideturtle()
turtle.done()

#8
import turtle
color = input()
color_2 = input()
turtle_shape = input()
size = int(input())
N = int(input())
line_width = int(input())

mike = turtle.Turtle()
mike.shape(turtle_shape)
mike.color(color_2, color)
mike.pensize(line_width)
mike.speed(0)
mike.pu()
mike.goto(-200, 0)
mike.pd()

exterior_angle = 360 / N

count = 0
while count < N:
    mike.forward(size)
    mike.stamp()
    mike.left(exterior_angle)
    count += 1

mike.hideturtle()
turtle.done()