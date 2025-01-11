import turtle

turtle.Screen().bgcolor("white")

board=turtle.Turtle()

#triangle
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)


#square
i = 0
for i in range(4):
    board.forward(100)
    board.left(90)

board.forward(100)

  #rectangle
i=0
for i in range(2):
    board.forward(100)
    board.left(90)

    board.forward(200)
    board.left(90)


turtle.done()