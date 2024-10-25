
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK_MARK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)

    title_label.config(text="Timer.")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

    global REPS 
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1

    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break.", fg=RED)

    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break.", fg=PINK)

    else:
        count_down(works_sec)
        title_label.config(text="Work.", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # if int(count_sec) > 0 and int(count_sec) < 10:
    #     count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += CHECK_MARK
        
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro.")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/home/sumon/Documents/Python/Tkinter or GUI/Pomodoro App/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
# canvas.pack()
canvas.grid(row=1, column=1)

# count_down(5)

start_button = Button(text="Start", highlightthickness=0, fg="white", bg=GREEN, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, fg="white", bg=GREEN, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(bg=YELLOW, fg=RED, highlightthickness=0)
check_mark.grid(row=2, column=1)


window.mainloop()