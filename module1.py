#Module_1. Introduction to Python. Input and output of data

#1
print('Hello, world!')

#2
print('Hello, world!')
print('Welcome to Python!')

#3
print('### # # ### ### #   ###')
print(' #  # # # #  #  #   #  ')
print(' #  # # ##   #  #   ###')
print(' #  # # # #  #  #   #  ')
print(' #  ### # #  #  ### ###')

#4
name = input()
print(name, name)

#5
print('What is your name?')
name = input()
print('What is your surname?')
surname = input()
print('What is your age?')
age = input()
print('Имя:', name, 'Фамилия:', surname, 'Возвраст:', age, 'лет')

#6
print('First input?')
a = input()
print('second input?')
b = input()
print('Third input?')
c = input()
print(b, c, a)

#7
import turtle
tortoise = turtle.Turtle()
tortoise.color('red')
tortoise.fd(200)
tortoise.lt(120)
tortoise.color('red')
tortoise.fd(200)
tortoise.lt(120)
tortoise.color('red')
tortoise.fd(200)
tortoise.lt(120)
turtle.done()

#8
import turtle
tortoise = turtle.Turtle()
tortoise.color('brown')
tortoise.fd(200)
tortoise.lt(90)
tortoise.color('brown')
tortoise.bk(200)
tortoise.lt(90)
tortoise.color('brown')
tortoise.fd(200)
tortoise.lt(90)
tortoise.color('brown')
tortoise.bk(200)
tortoise.lt(90)
tortoise.color('black')
tortoise.lt(60)
tortoise.fd(200)
tortoise.lt(240)
tortoise.fd(200)
turtle.done()

