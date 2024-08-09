from turtle import Turtle


class Coord(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-260, 260)

    def show_coord(self, x, y, bool):
        if bool == True:
            self.clear()
            self.goto(-260, 260)
            self.write(f"x = {round(x)} y = {round(y)}", align='left')
        else:
            pass