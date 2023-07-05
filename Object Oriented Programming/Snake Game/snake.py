from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # parts of the snake's body
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ method which determines the position of each turtle object """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """ method that creates a turtle object and determines the color, the position that comes
            as an argument from the create_snake method and adds the created object to self.segments. """
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ method that add a new segment to the snake after eating food. """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ method moves the segments of the snake from position 2 to 1 and so on, and finally
            pushes the head of the snake by 20 pixels. """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheding(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheding(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheding(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheding(RIGHT)

