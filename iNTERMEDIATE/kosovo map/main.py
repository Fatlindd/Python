import turtle
import pandas
import random

# Step 1: Convert your image to GIF format and provide the path to the file
robot_location = "location.gif"

# Step 2: Register the image as a turtle shape
turtle.register_shape(robot_location)

screen = turtle.Screen()
screen.title("Kosovo Map")
screen.setup(width=900, height=800)
image = "kosovo.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("kosovo_cities.csv")
all_cities = data.city.to_list()
guessed_cities = []
wrong_cities = []

def check_answer(robot, city ,city_data):
    user_input = screen.textinput(title="Kosovo Map",
                                  prompt="What is the name of the city?").title()
    if user_input == "Exit":
        for city in all_cities:
            if city not in guessed_cities:
                wrong_cities.append(city)
        new_data = pandas.DataFrame(wrong_cities)
        new_data.to_csv('cities_to_learn.csv')
    elif user_input == city:
        guessed_cities.append(city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(city_data.x), int(city_data.y))
        robot.hideturtle()
        t.write(city)
        reset_score()
    else:
        wrong_cities.append(city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(city_data.x), int(city_data.y))
        robot.hideturtle()
        t.write('X')
        reset_score()


score = turtle.Turtle()
score.hideturtle()
score.penup()
def reset_score():
    correct = f"{len(guessed_cities)}/37 Cities Correct"
    incorrect = f"{len(wrong_cities)}/37 Cities Incorrect"
    score.clear()
    score.goto(-410, 360)
    score.write(correct, align="left", font=("Arial", 14, "normal"))
    score.goto(-410, 330)
    score.write(incorrect, align="left", font=("Arial", 14, "normal"))

def set_location():    
    city = random.choice(all_cities)
    print(city)
    if city not in guessed_cities and city not in wrong_cities:
        city_data = data[data.city == city]
        robot = turtle.Turtle()
        robot.shape(robot_location)
        robot.penup()
        robot.goto(int(city_data.x), int(city_data.y))
        check_answer(robot, city, city_data)

while len(guessed_cities + wrong_cities) < 37:
    set_location()

screen.exitonclick()