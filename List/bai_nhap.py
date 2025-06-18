import turtle as t

import colorsys

t.bgcolor("black")
t.speed(0)
color = ("cyan", "white")
for i in range(5000):
    t.color(color[i % 2])
    t.fd(i)
    t.rt(45)
    t.circle(65, 139)
    t.fd(150 - i)
    t.backward(60)
t.done()