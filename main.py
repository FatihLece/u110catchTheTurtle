# Catch the Turtle Game / Kaplumbaga Terbiyecisi

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ("Arial", 30, "normal")  # if capital NAME, it means (seems) it is constant!
turtleList = []
score = 0
gameOver = False

# turtle properties
gridSize = 10
xCoordinates = [-20, -10, 0, 10, 20]
yCoordinates = [-20, -10, 0, 10, 20]

# score turtle
scoreTurtle = turtle.Turtle()

# countdown turtle
countdownTurtle = turtle.Turtle()


def setupScoreTurtle():
    scoreTurtle.hideturtle()
    scoreTurtle.color("dark blue")
    scoreTurtle.penup()

    topHeight = screen.window_height()
    y = topHeight * 0.42
    scoreTurtle.setpos(0, y)

    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)


def makeTurtle(x, y):
    t = turtle.Turtle()  # third turtle!

    def handleClick(x, y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
        print(x, y)  # if necessary to check it is work

    t.onclick(handleClick)
    t.penup()
    t.shape("turtle")
    t.shapesize(3, 3)
    t.color("dark green")
    t.goto(x * gridSize, y * gridSize)
    t.pendown()  # is it necessary !? -> yes if not game will continue!
    turtleList.append(t)


def setupTurtle():
    for x in xCoordinates:
        for y in yCoordinates:
            makeTurtle(x, y)


def hideTurtle():
    for t in turtleList:
        t.hideturtle()


def showTurtleRandom():
    if not gameOver:
        hideTurtle()
        random.choice(turtleList).showturtle()
        screen.ontimer(showTurtleRandom, 750)  # recursive function


def countdown(time):
    global gameOver
    countdownTurtle.hideturtle()
    countdownTurtle.color("dark blue")
    countdownTurtle.penup()

    topHeight = screen.window_height()
    y = topHeight * 0.42
    countdownTurtle.setpos(0, y-35)
    countdownTurtle.clear()

    if time > 0:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)  # lambda is NOT necessary, we got countdown def func!
    else:
        gameOver = True
        countdownTurtle.clear()
        hideTurtle()
        countdownTurtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def startGameUp():
    turtle.tracer(0)  # animation stops!
    setupScoreTurtle()
    setupTurtle()
    hideTurtle()
    showTurtleRandom()
    countdown(10)
    turtle.tracer(1)  # result of animation


startGameUp()
turtle.mainloop()
