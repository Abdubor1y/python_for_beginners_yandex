#Module_2. Data types. Basic mathematical operations

#1
a = input() + ','
b = input() + ','
c = input() + '.'
print('Необходимо положить в чемодан:', a, b, c)

#2
symbol = input()
x = 10 * symbol
y = symbol + ' ' * 8 + symbol
z = symbol + ' Turtle ' + symbol
w = symbol + ' ' * 8 + symbol
d = 10 * symbol

print(x)
print(y)
print(z)
print(w)
print(d)

#3
x = int(input())
print(str(x) * x)

#4
x = int(input())
y = int(input())

print(str(x) + " + " + str(y) + " = " + str(x + y))
print(str(x) + " - " + str(y) + " = " + str(x - y))
print(str(x) + " * " + str(y) + " = " + str(x * y))
print(str(x) + " // " + str(y) + " = " + str(x // y))
print(str(x) + " % " + str(y) + " = " + str(x % y))
print(str(x) + " ** " + str(y) + " = " + str(x ** y))

#5
n = int(input())
k = int(input())

print(n // k)

#6
a = int(input())
b = int(input())
c = int(input())
x = float(input())
print(a * x ** 2 + b * x + c)

#7
import turtle
tortoise = turtle.Turtle()
length = int(input())
x = input()

tortoise.color(x)
tortoise.lt(45)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
tortoise.lt(90)
tortoise.fd(length)
turtle.done()