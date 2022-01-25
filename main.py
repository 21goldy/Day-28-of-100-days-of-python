from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1/2
SHORT_BREAK_MIN = 1/2
LONG_BREAK_MIN = 1/2
REPS = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(time)
    timer.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    check_box.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        timer.config(text="Break", font=(FONT_NAME, 30, "bold"), fg=RED, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
        check_box.config(text="")
    elif REPS % 2 == 0:
        timer.config(text="Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
        check_box.config(text="")
    else:
        timer.config(text="Work Time", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_box.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Pomodoro window

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer_label

timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(row=1, column=1)

# canvas_setup

canvas = Canvas(width=205, height=250, bg=YELLOW)
tomato = PhotoImage(file="images/tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

# start_button

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=YELLOW, command=start_timer)
start_button.grid(row=3, column=0)
start_button.config(padx=20)

# reset_button

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=YELLOW, command=reset_timer)
reset_button.grid(row=3, column=2)
reset_button.config(padx=20)

# check_box

check_box = Button(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
check_box.grid(row=3, column=1)
check_box.config(padx=20)

# keeps the window on

window.mainloop()
