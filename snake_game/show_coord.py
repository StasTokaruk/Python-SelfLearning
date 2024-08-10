from turtle import Turtle


class Coord():
    def __init__(self):
        self.coord_write = Turtle()
        self.cwf = Turtle()
        self.coord_write.penup()
        self.coord_write.hideturtle()
        self.coord_write.color('white')
        self.cwf.penup()
        self.cwf.hideturtle()
        self.cwf.color('white')
    def show_coord(self, x, y, bool):
        if bool == True:
            self.coord_write.clear()
            self.coord_write.goto(-260, 260)
            self.coord_write.write(f"x = {round(x)} y = {round(y)}", align='left')
        else:
            pass

    def show_coord_food(self, x, y, bool):
        if bool == True:
            self.cwf.clear()
            self.cwf.goto(260, 260)
            self.cwf.write(f"Food: x = {round(x)} y = {round(y)}", align='Right')