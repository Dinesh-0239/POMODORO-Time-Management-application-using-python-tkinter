"""
Date:- 12/07/2023
Developer:- Dinesh Singh

Description:- This POMODO Application helps person to manage time by assigning work session of 25min and 5min break after
4 repeatation a long break of 20 mins and restart again.

The project is based on the python's tkinter module which provides GUI features to the project.
"""
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_lbl.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_lbl.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_lbl.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_lbl.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global  timer
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = "0" + str(sec)
    if min < 10:
        min = "0" + str(min)

    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 8 == 1:
            checkmark_lbl["text"] = ""
        elif reps % 2 == 0:
            checkmark_lbl["text"] += "✔️"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)
window.iconbitmap("AppIcon.ico")
window.resizable(False,False)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

title_lbl = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
title_lbl.grid(row=0,column=1)
Button(text="Start",relief=GROOVE,highlightthickness=0,command=start_timer).grid(row=2,column=0)
Button(text="Reset",relief=GROOVE,highlightthickness=0,command=reset_timer).grid(row=2,column=2)
checkmark_lbl = Label(fg=GREEN,bg=YELLOW,highlightthickness=0)
checkmark_lbl.grid(row=3,column=1)
window.mainloop()