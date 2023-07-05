"""
1️⃣. Create a snake body
2️⃣. Move the snake
3️⃣. Control the snake
4️⃣. Detect collision with food
5️⃣. Create a scoreboard
6️⃣. Detect collision with wall
7️⃣. Detect collision with tail
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# turn turtle animation on/off
# Because when the snake moves on the screen, it looks as if it is divided into parts,
# so the animation must be stopped, the process should be completed for a while, and
# an update should be made to show the animation again as changed.
screen.tracer(0)

# snake object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    """ Until we call update the screen is not going to refresh
        and it's not going to show us what's been happening in our code. """
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    # food turtle is 10x10 pixels.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
