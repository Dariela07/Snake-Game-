from turtle import Turtle
from food import Food
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.speed('fastest')
        self.color('white')
        # self.write('Your score is: ', move=False, align='center', font=('Arial', 20, 'normal'))
        self.score = 0
        self.high_score = 0
        with open("data.txt", 'r') as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score is: {self.score}   High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()