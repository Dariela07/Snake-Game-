from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.forward(20)
tim.setheading(90)
tim.forward(20)

tim2 = Turtle()
tim2.hideturtle()
tim2.penup()
tim2.goto(0, 400)
tim2.speed('fastest')
tim2.write("Hello", move=False, align='center', font=('Arial', 20, 'normal'))
screen.exitonclick()