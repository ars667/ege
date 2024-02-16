from turtle import *

# создаём множитель масштаба
k = 50

# создаём объект черепашки
t = Turtle()
screen = Screen()

t.speed(0)

t.penup()

# сетка

for i in range(-5 * k, 5 * k, k):
    for j in range(-5 * k, 5 * k, k):
        t.goto(i, j)
        t.dot()
t.goto(-5*k, 5*k)

t.pendown()
# фигура
for i in range(11):
    t.forward(4*k)
    t.right(60)
screen.mainloop()

