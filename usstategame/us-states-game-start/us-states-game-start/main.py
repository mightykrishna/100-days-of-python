import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#HOW TO GET ANY COORDINATE IN ONE CLICK IN TURTLES
#def get_mouse_click(x,y):
#    print(x,y)
#
#
#turtle.onscreenclick(get_mouse_click)
#
#turtle.mainloop()

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]
while(len(guessed_states)<50):
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="What is The another state's name").title()
    
    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        newdata=pandas.DataFrame(missing_states)
        newdata.to_csv("states_to_learn.csv")

        break
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    


screen.exitonclick()