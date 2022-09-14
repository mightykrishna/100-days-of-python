THEME_COLOR = "#375362"
FONT_NAME="Courier"
from tkinter import *
from turtle import right
from quiz_brain import QuizBrain
class Quiz:
    def __init__(self,quiz_brain: QuizBrain) :
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("quiz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.title_label=Label(text="Score",fg="black",font=(FONT_NAME,35,"bold"))
        self.title_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0)
        
        self.question_txt=self.canvas.create_text(150,125,width=280,text="SOME questions",fill=THEME_COLOR,font=("Arial",20,"bold"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        right_img=PhotoImage(file="images/true.png")
        self.correct_button=Button(image=right_img,highlightthickness=0,command=self.true_pressed)
        self.correct_button.grid(row=2,column=0)


        wrong_img=PhotoImage(file="images/false.png")
        self.wrong_button=Button(image=wrong_img,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_txt,text=q_text)

    def true_pressed(self):
        self.quiz.check_answer("True")

    def false_pressed(self):
        self.quiz.check_answer("False")