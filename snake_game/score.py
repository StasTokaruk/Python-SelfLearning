from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 14, 'bold'))

    def score_add(self):
        self.clear()
        self.goto(0, 260)
        self.score+=1
        self.write(f'Score: {self.score}', align='center', font=('Arial', 14, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 14, 'bold'))