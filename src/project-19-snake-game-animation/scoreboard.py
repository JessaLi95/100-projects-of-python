from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.ht()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align=ALIGNMENT, font=FONT)