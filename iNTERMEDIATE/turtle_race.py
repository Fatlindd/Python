from turtle import Turtle, Screen
import random

# check if the race has started
is_race_on = False

screen = Screen()
# set the size and position of the main window
screen.setup(width=500, height=400)

# pop up a dialog window for input of a string
user_input = screen.textinput(title="Give your choice", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    # Turtle() class have shape attribute in __init__() method.
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # goto(x, y) position on window because we have more than one turtle
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    # if user input is set to one color then tell that race start
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()