from turtle import Turtle


class Snake:

    def __init__(self):
        # parts of the snake's body
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


