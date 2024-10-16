#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.goto(0,-20)
x.circle(20)
x.goto(0,-55)
x.circle(10)
w = 4
y = 70
z = 90 / w
x.pensize(5)
for h in range(2):
    for n in range(w):
        x.penup()
        x.goto(0,0)
        x.setheading((z*n)+(h*180)-35)
        if h==0:
            what=-1
        else:
            what=1
        x.pendown()
        x.circle(150*what,75)

for l in range(2):
    x.penup()
    x.goto(0,-55)
    x.setheading((-100*l)-45)
    x.forward(10)
    x.color("red")
    x.pendown()
    x.forward(1)
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()