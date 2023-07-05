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

