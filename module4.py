#Module_4. For loop

#1
n = int(input())
for i in range(n):
    print(n)
    n -= 1
print('Дзынь')

#2
n = int(input())
total = 0
for i in range(n):
    numbers = int(input())
    if numbers % 5 == 0:
        total += numbers
print(total)

#3
x = int(input())
y = int(input())
z = int(input())
total = 0

for i in range(x, y + 1, z):
    print(i)
    total += 1
print('Всего кочек: ', total)

#4
h = int(input())
step_up = int(input())
step_down = int(input())
position = 0

for i in range(0, h + 1, step_up):
    position = i
    print(position)
print(position)

for i in range(position - step_down, 0, - step_down):
    position = i
    print(position)
print(0)

#5
N = int(input())
K = int(input())

for i in range(K, N + 1, K):
    print(i, end=' км ')

#6
a = int(input())
b = int(input())
x1 = int(input())
x2 = int(input())

for i in range(x1, x2 + 1):
    solution = a * i + b
    print('x = ', i, ', ax + b = ', solution, sep='', end='')
    if solution == 0:
        print(' - корень уравнения')
    else:
        print()
    
#7
N = int(input())

for i in range(N):
    if i == 0:
        spaces = ' ' * (N - 1)
        print(spaces + '/\\')
    else:
        spaces = ' ' * (N - 1 - i)
        middle_spaces = ' ' * (2 * i)
        print(spaces + '/' + middle_spaces + '\\')

#8
N = int(input())

if 1 <= N <= 15:
    for i in range(1, N + 1):
        print('\t' * (i - 1) + str(i))

#9
import turtle

mike = turtle.Turtle()

color_any = input()
length_beam = int(input())
number_beam = int(input())

mike.pd()
mike.color(color_any)
mike.speed(10)

angle = 360 / number_beam

for i in range(number_beam):
    mike.fd(length_beam)
    mike.bk(length_beam)
    mike.rt(angle)

mike.ht()
turtle.done()

#10
import turtle

tony = turtle.Turtle()

color_any = input()
N = int(input())
S = int(input())

tony.speed(10)
tony.pu()
tony.goto(-100, -100)
tony.setheading(0)
tony.pd()

tony.color(color_any)
tony.begin_fill()

for i in range(N):
    tony.left(90)
    tony.forward(S)
    tony.right(90)
    tony.forward(S)

for i in range(N - 1):
    tony.right(90)
    tony.forward(S)
    tony.left(90)
    tony.forward(S)

tony.right(90)
tony.forward(S)
tony.right(90)
tony.goto(-100, -100)

tony.end_fill()
tony.hideturtle()
turtle.done()