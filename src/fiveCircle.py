import turtle

t = turtle.Pen()

t.width(10)
t.color('blue')
t.circle(50)

t.penup()
t.goto(120, 0)
t.pendown()
t.color('yellow')
t.circle(50)

t.penup()
t.goto(240, 0)
t.pendown()
t.color('red')
t.circle(50)

t.penup()
t.goto(60, -30)
t.pendown()
t.color('black')
t.circle(50)

t.penup()
t.goto(180, -30)
t.pendown()
t.color('black')
t.circle(50)