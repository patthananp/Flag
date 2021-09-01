import turtle

s = turtle.getscreen()

turtle.color("black","red")
turtle.begin_fill()
turtle.forward(300)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()

turtle.forward(30)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(30)
turtle.backward(30)

turtle.color("black","navy")
turtle.begin_fill()
turtle.backward(50)
turtle.left(90)
turtle.backward(300)
turtle.left(90)
turtle.backward(50)
turtle.end_fill()

turtle.forward(50)


turtle.forward(30)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(30)
turtle.backward(30)

turtle.color("black","red")
turtle.begin_fill()
turtle.backward(30)
turtle.right(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(30)
turtle.end_fill()

turtle.done()
