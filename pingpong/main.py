from turtle import Turtle,Screen
from paddleclass import Paddle
from ballclass import Ball
import time
from scoreclass import Score
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PingPong")
screen.tracer(0)

rp=Paddle((350,0))
lp=Paddle((-350,0))
ball=Ball()
score=Score()


screen.listen()
screen.onkey(rp.go_up,"Up")
screen.onkey(rp.go_down,"Down")

screen.onkey(lp.go_up,"w")
screen.onkey(lp.go_down,"s")
gameon=True
while gameon:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(rp)<50 and ball.xcor()>320:
        ball.bounce_x()
    if ball.distance(lp)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380   :
        ball.reset_pos()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_point()





screen.exitonclick()