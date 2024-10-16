#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
x=ladybug
w = 3
y = 50
z = 90 / w
x.pensize(5)
for h in range(2):
    for n in range(w):
        x.goto(0,-35)
        x.setheading((z*n)+(h*180)-30)
        x.forward(y)
# and body
x.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 2
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
for h in range(num_dots):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  xpos = ypos + 40
  ypos = xpos - 15

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()