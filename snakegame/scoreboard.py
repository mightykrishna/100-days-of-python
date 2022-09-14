from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",8,"normal"))
        self.hideturtle()
        
    def update_score(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",8,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GameOver",align="center",font=("Arial",8,"normal"))
