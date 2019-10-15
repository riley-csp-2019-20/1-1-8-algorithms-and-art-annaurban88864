
import turtle as trtl
 
boat = trtl.Turtle()
boat.fillcolor("brown")
#creating boat
boat.pencolor("brown")
boat.penup()
boat.goto(-100,-100)
boat.pendown()
boat.setheading(135)
boat.begin_fill()
boat.forward(50)
boat.right(135)
boat.forward(185)
boat.right(135)
boat.forward(50)
boat.right(45)
boat.forward(115)
boat.end_fill()

#creating mast
boat.pencolor("black")
boat.penup()
boat.goto(-45,-65)
boat.pendown()
boat.setheading(90)
boat.forward(110)
boat.right(90)
boat.forward(5)
boat.right(90)
boat.forward(110)
boat.penup()
boat.pencolor("purple")
boat.setheading(90)
boat.forward(110)
boat.right(90)
boat.forward(5)
boat.pendown()
boat.right(45)
boat.forward(145)
boat.right(135)
boat.forward(103)
boat.right(90)
boat.forward(102)
boat.penup()
boat.left(90)
boat.forward(15) 
boat.left(45)
boat.pendown()
boat.forward(145)
boat.left(135)
boat.forward(103)
boat.left(90)
boat.forward(103)
boat.penup()
boat.forward(5)
boat.pendown()
boat.fillcolor("purple")
boat.begin_fill()
boat.forward(10)
boat.right(115)
boat.forward(20)
boat.right(148)
boat.forward(20)
boat.end_fill()

# create code for the water
boat.penup()
boat.goto(-185,-100)
boat.pendown()


count = 0
 
while count < 10:
    boat.pencolor("blue")
    boat.setheading(45)
    boat.forward(20)
    boat.setheading(315)
    boat.forward(20)
    count += 1
 
 
 
wn = trtl.Screen()
wn.mainloop()


