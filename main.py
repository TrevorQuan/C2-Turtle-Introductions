import turtle
import random
 #"turtle" class
turtle.shape("turtle")
turtle.color("black")
turtle.speed(30)
turtle.pensize(5)
turtle.fillcolor("green")
turtle.begin_fill()
#for count in range(100):
turtle.forward(15)
turtle.right(10) # degrees
turtle.end_fill()

  turtle.penup()
  turtle.left(90)
  turtle.forward(100)
  turtle.pendown()
  turtle.circle(100)

Trev = turtle.Turtle()
Trev.shape("turtle")
Trev.color("light brown")
Trev.fillcolor("brown")
Trev.penup()
Trev.forward(300)
Trev.pendown()
for count in range(4):
  Trev.fillcolor("brown")
  turtle.begin_fill()
  Trev.forward(100)
  Trev.right(90)
  turtle.end_fill()
Trev.left(45)
Trev.forward(50)
Trev.right(45)
Trev.forward(25)
Trev.right(45)
Trev.forward(50)

Star = turtle.Turtle
Star.shape("turtle")
for i in range(5):
  Star.forward(100)
  Star.right(144)