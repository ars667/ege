# создаём множитель масштаба
k = 30

# добавляем модуль черепашка
import turtle
from turtle import *

# создвём объект черпашки t
t = Turtle()

# это нужно для ускорения
turtle.tracer(0)

#  создаём экран для черепашки
s = t.screen

# создание сетки координат
t.penup()
for i in range(-100 * k, 100 * k, k):
    for j in range(-100 * k, 100 * k, k):
        t.goto(i, j)
        t.dot()
t.goto(0, 0)
x = y = 0

# опускаем хвост и чётко выполняем задание
t.pendown()
for i in range(10):
    x += 3 * k
    y += 6 * k
    t.goto(x, y)
    x += 7 * k
    y += -2 * k
    t.goto(x, y)
    x += -10 * k
    y += -4 * k
    t.goto(x, y)
turtle.update()
s.mainloop()
