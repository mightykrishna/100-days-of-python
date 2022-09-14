from tkinter import *
import math
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="TIMER")
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    countdown(work_sec)
    if reps%8==0:
        countdown(long_break_sec)
        title_label.config(text="BREAk",fg=RED)
    elif reps%2==0:
        countdown(short_break_sec)
        title_label.config(text="BREAk",fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="WORK",fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if  count_sec<10:
        count_sec=f"0{count_sec}"
    if count_sec==0:
        count_sec="00"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks="✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("time watcher")
window.config(padx=100,pady=100,bg=YELLOW)







title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"))
title_label.grid(column=1,row=0)

canvas=Canvas(width=500,height=400,bg=YELLOW,highlightthickness=0)
saurah_img=PhotoImage(file="291718.png")
canvas.create_image(300,350,image=saurah_img)
timer_text=canvas.create_text(250,80,text="00.00",fill="red",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


window.mainloop()
