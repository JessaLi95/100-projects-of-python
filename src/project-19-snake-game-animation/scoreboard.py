from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_highest_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.goto(0, 250)
        self.ht()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("snake_highest_score.txt", mode="w") as new_data:
            new_data.write(str(self.high_score))
        self.score = 0
        self.update_score()
