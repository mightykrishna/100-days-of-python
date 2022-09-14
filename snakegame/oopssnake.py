from turtle import Turtle
starting_pos=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
Up=90
Right=0
Down=270
Left=180
class Snake:



    def __init__(self) :
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in starting_pos:
            self.add_segment(pos)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            newx=self.segments[seg-1].xcor()
            newy=self.segments[seg-1].ycor()
            self.segments[seg].goto(newx,newy)
            
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)
    def down(self):
        if self.head.heading()!=Up:
            self.head.setheading(Down)
    def right(self):
        if self.head.heading()!=Left:
            self.head.setheading(Right)
    def left(self):
        if self.head.heading()!=Right:
            self.head.setheading(Left)
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())