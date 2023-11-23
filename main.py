from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=750, height=500)


def race(turtle_list):
    """Loops turtles moving forward until one gets to finish line. Takes list of turtle objects."""
    finish = False
    while not finish:
        for t in turtle_list:
            dist = randint(1, 5)
            t.forward(dist)
            if t.xcor() >= 300:
                finish = True
                winner = t
                return winner


def get_position(chosen_turtle, turtle_list):
    """Returns the position of the turtle in the race that the user bet on"""
    pos = 1
    for t in turtle_list:
        if t.xcor() > chosen_turtle.xcor():
            pos += 1
    if pos == 2:
        position = f"{pos}nd"
    elif pos == 3:
        position = f"{pos}rd"
    else:
        position = f"{pos}th"
    return position

def start_race():
    """Main logic for race, asks for bet, creates all turtle objects and sets them to start line."""
    """Game will restart if the user wants to replay."""
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
        index = turtles.index(t)
        t.color(turtle_colors[index])

    start_pos = -120
    for t in turtles:
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
