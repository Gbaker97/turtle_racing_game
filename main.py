from turtle import Turtle, Screen
from random import randint

screen = Screen()


def race(turtles):
    finish = False
    while not finish:
        for t in turtles:
            dist = randint(1, 5)
            t.forward(dist)
            if t.xcor() >= 300:
                finish = True
                winner = t
                return winner


def get_position(turtle, turtle_list):
    pos = 1
    for t in turtle_list:
        if t.xcor() > turtle.xcor():
            pos += 1
    if pos == 2:
        position = f"{pos}nd"
    elif pos == 3:
        position = f"{pos}rd"
    else:
        position = f"{pos}th"
    return position

def start_race():
    red = Turtle()
    orange = Turtle()
    yellow = Turtle()
    green = Turtle()
    blue = Turtle()
    purple = Turtle()

    turtles = [red, orange, yellow, green, blue, purple]
    turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    bet = screen.textinput("Make your bet",
                           "Who will win the race? Enter a colour:")
    chosen_turtle = turtles[turtle_colors.index(bet)]

    for t in turtles:
        t.shape("turtle")

    start_pos = -120
    for t in turtles:
        index = turtles.index(t)
        t.color(turtle_colors[index])
        t.penup()
        t.goto(-300, start_pos)
        start_pos += 50

    winner = race(turtles)
    winner = turtle_colors[turtles.index(winner)]
    position = get_position(chosen_turtle, turtles)

    if winner == bet.lower():
        replay = screen.textinput("Congratulations!",
                                  "Your turtle came 1st. "
                                  "Would you like to play again? "
                                  "Type 'yes' or 'no':")
    else:
        replay = screen.textinput("You lost!",
                                  f"Your turtle came {position}. "
                                  "Would you like to play again? "
                                  "Type 'yes' or 'no':")
    if replay.lower() == "yes":
        screen.clear()
        start_race()
    else:
        screen.clear()
        return


start_race()

screen.exitonclick()
