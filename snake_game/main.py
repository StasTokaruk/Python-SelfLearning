from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score
from show_coord import Coord

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
coord=Coord()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    coord.show_coord(snake.segments[0].xcor(), snake.segments[0].ycor(), True)
    if snake.segments[0].distance(food) < 15:
        score.score_add()
        food.refresh()


screen.exitonclick()