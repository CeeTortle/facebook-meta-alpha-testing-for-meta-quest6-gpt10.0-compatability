#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
# create two empty lists of turtles, adding to them later
def rng(x,y,pl):
  if x>y-pl and x<y+pl:
    return True
  else:
    return False
  
horiz_turtles = []
vert_turtles = []
listx=[]
listy=[]
speedx=[]
speedy=[]
speed1,speed2=0,0
for i in range(6):
  listx.append(0)
  listy.append(0)
  speedx.append(0)
  speedy.append(0)
# use interesting shapes and colors
import random
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
horizr_colors = ["red", "blue", "green", "orange", "purple", "gold"]
tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  print(ht)
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
while True:
  for t in range(6):
    speed1=speedx[t]+0.2
    speed2=speedy[t]+0.4
    if speed1>10:
      speed1=10
    if speed2>10:
      speed2=10
    horiz_turtles[t].forward(speed1)
    horiz_turtles[t].shape(turtle_shapes[t])
    vert_turtles[t].shape(turtle_shapes[t])
    listx.insert(t,horiz_turtles[t].xcor())
    listy.insert(t,horiz_turtles[t].ycor())
    vert_turtles[t].forward(speed2)
    speedx[t]=speed1
    speedy[t]=speed2
    for x in range(6):
      if rng(vert_turtles[t].xcor(),listx[x],15):
        for y in range(6):
          if rng(vert_turtles[t].ycor(),listy[y],15):
            vert_turtles[t].forward(-20)
            horiz_turtles[y].forward(-20)
            vert_turtles[t].fillcolor(random.choice(horizr_colors))
            horiz_turtles[y].fillcolor(random.choice(horizr_colors))
            vert_turtles[t].shape("circle")
            horiz_turtles[y].shape("circle")
            speedx[t]=0
            speedy[t]=0
            




  


wn = trtl.Screen()
wn.mainloop()
