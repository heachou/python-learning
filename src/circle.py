import turtle

t = turtle.Pen()

my_colors = ("red", "green", "yellow", "black", "pink")
t.width(2)
t.speed(10)

# for i in range(10):
#     t.penup()
#     t.goto(0, -20 * i)
#     t.pendown()
#     t.color(my_colors[i % len(my_colors)])
#     t.circle(20 * (i + 1))

#
for i in range(19):
    t.penup()
    t.goto(0, i * 20)
    t.pendown()
    t.goto(360, i * 20)

for i in range(19):
    t.penup()
    t.goto(i * 20, 0)
    t.pendown()
    t.goto(i * 20, 360)

turtle.done()
