#Module_7. Functions in Python

#1
def choose_name():
    name1 = input()
    name2 = input()
    if name1 > name2:
        print(name1)
    else:
        print(name2)

#2
def timer():
    number = int(input())
    for i in range(number, -1, -1):
        print(i)

#3
def print_square(n, symbol):
    print(symbol * n)
    for i in range(n - 2):
        print(symbol + ' ' * (n - 2) + symbol)
    print(symbol * n)

#4
def turtle_command(word1, word2):
    if word2 in word1:
        print(word1)
    else:
        print(word1 + '_' + word2)

#5
def degree(x):
    if abs(x) > 15:
        return x ** 2
    elif 5 < abs(x) <= 15:
        return x ** 3
    else:
        return x ** 5
    
#6
def time_of_day(hours, minutes):
    if 5 < hours < 12 and 0 <= minutes < 60:
        return 'утро'
    elif 11 < hours < 18 and 0 <= minutes < 60:
        return 'день'
    elif 17 < hours < 24 and 0 <= minutes < 60:
        return 'вечер'
    else:
        return 'ночь'
    
#7
import turtle


sc = turtle.Screen()
sc.setup(startx=0, starty=0)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()
drawer.pensize(3)
drawer.pencolor('yellow')

stamper = turtle.Turtle()
stamper.hideturtle()
stamper.penup()
stamper.speed(0)

prev = [0.0, 0.0]


def handle_click(x, y, button_type):
    drawer.penup()
    drawer.goto(prev[0], prev[1])
    drawer.pendown()
    drawer.goto(x, y)
    drawer.penup()

    prev[0], prev[1] = x, y

    if button_type == 'left':
        stamper.color('yellow', 'brown')  # pencolor, fillcolor
        stamper.shape('turtle')
    else:
        stamper.color('yellow', 'green')
        stamper.shape('triangle')

    stamper.shapesize(5)
    stamper.goto(x, y)
    stamper.stamp()


def on_left_click(x, y):
    handle_click(x, y, 'left')


def on_right_click(x, y):
    handle_click(x, y, 'right')


sc.onscreenclick(on_left_click, btn=1)
sc.onscreenclick(on_right_click, btn=3)
sc.onscreenclick(on_right_click, btn=2)

turtle.done()