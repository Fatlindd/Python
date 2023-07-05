from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # hide the turtle shape just display text
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ This method is created because without it when snake eat food always overwritten
            the score in scoreboard """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ method tells the user that the game is over """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ method increments the score by 1 and deletes the drawing of the turtle object, and
            replaces it with a new one by calling the update_scoreboard() method. """
        self.score += 1
        self.clear()
        self.update_scoreboard()
