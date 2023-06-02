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
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    screen.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(time, text="00:00")
    tick.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global rep
    rep += 1
    work_time = WORK_MIN * 60
    short_time = SHORT_BREAK_MIN * 60
    long_time = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        count_down(long_time)
        timer_label.config(text="Break", foreground=RED)
    elif rep % 2 == 0:
        count_down(short_time)
        timer_label.config(text="Break", foreground=PINK)
    else:
        count_down(work_time)
        timer_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(rep/2)):
            mark += "✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Pomodoro Timer")
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
time = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 32,"bold"), fill="white")
canvas.grid(column=2,row=2)

timer_label = Label(text="Timer")
timer_label.config(font=(FONT_NAME, 50), foreground=GREEN, background=YELLOW )
timer_label.grid(column=2,row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1,row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3,row=3)

tick = Label()
tick.config(background=YELLOW, foreground=GREEN)
tick.grid(column=2,row=4)
screen.mainloop()
