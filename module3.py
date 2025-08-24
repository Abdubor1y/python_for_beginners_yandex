#Module_3. Conditional operators

#1
password = input()
if password == 'Python':
    print('Ты выбрал правильный путь')
else:
    print('Попробуй изучить Python!')

#2
password = input()
if password == 'Turtle' or password == 'Черепаха':
    print('Верно')
else:
    print('Неверно')

#3
a = input()
b = input()
c = input()

if a == 'красный' and b == 'оранжевый' and c == 'желтый':
    print('Ты знаешь порядок цветов радуги')
else:
    print('Первые 3 цвета радуги: красный, оранжевый, желтый')

#4
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

#5
x = int(input())
y = int(input())
z = int(input())

if (x > y and y > z) or (x < y and y < z):
    print(y)
elif (y > x and x > z) or (y < x and x < z):
    print(x)
else:
    print(z)

#6
a = input()
first_word = len(a)
b = input()
second_word = len(b)
c = input()
third_word = len(c)

if first_word > second_word and first_word > third_word:
    print(a)
elif second_word > first_word and second_word > third_word:
    print(b)
elif third_word > first_word and third_word > second_word:
    print(c)
else:
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

#7
text = input()
if (
        '0' in text or '1' in text or '2' in text or
        '3' in text or '4' in text or '5' in text or
        '6' in text or '7' in text or '8' in text or
        '9' in text
):
    print('В строке есть цифры')
else:
    print('В строке нет цифр')

#8
import turtle
sign = turtle.Turtle()
square_color = input()
triangle_color = input()
length = int(input())

sign.color(square_color)
sign.goto(0, length)
sign.goto(length, length)
sign.goto(length, 0)
sign.goto(0, 0)

sign.pu()
sign.goto(length * 2, 0)
sign.pd()

sign.color(triangle_color)
sign.goto(length * 3, 0)
sign.goto(length * 2.5, length * (3 ** 0.5) / 2)
sign.goto(length * 2, 0)

turtle.done()

#9
import turtle
tortoise = turtle.Turtle()
direction = input()
s = int(input())

tortoise.pu()
tortoise.goto(0, 0)
tortoise.pd()

if direction == 'up':
    tortoise.goto(5 * s, 0)
    tortoise.goto(5 * s, 15 * s)
    tortoise.goto(10 * s, 15 * s)
    tortoise.goto(2.5 * s, 30 * s)
    tortoise.goto(-5 * s, 15 * s)
    tortoise.goto(0, 15 * s)
    tortoise.goto(0, 0)
else:
    tortoise.speed(1)
    tortoise.goto(5 * s, 0)
    tortoise.goto(5 * s, -15 * s)
    tortoise.goto(10 * s, -15 * s)
    tortoise.goto(2.5 * s, -30 * s)
    tortoise.goto(-5 * s, -15 * s)
    tortoise.goto(0, -15 * s)
    tortoise.goto(0, 0)
turtle.done()