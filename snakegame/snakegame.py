from turtle import Screen,Turtle, penup
import time
from oopssnake import Snake
from food import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
gameon=True
while gameon:
    screen.update()
    time.sleep(0.1)
       
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameon=False
        score.game_over()


    for segment in snake.segments:
        
            if segment ==snake.head:
                pass

            elif  snake.head.distance(segment)<10:
                gameon= False
                
                score.game_over()



screen.exitonclick()