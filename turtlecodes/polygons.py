import turtle as t
import random
tim=t.Turtle()

colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","wheat","SeaGreen"]
tim.speed("fastest")
def draw_polygon(sides):
    angle=360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for shape in range(3,15):
    tim.color(random.choice(colours))
    draw_polygon(shape)