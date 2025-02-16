import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 24
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    timer_lab.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_lab.config(text="")
    window.after_cancel(timer)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60


def start_timer():
    global reps
    reps += 1
    if reps%8 == 0:
        count_down(long_break_sec)
        timer_lab.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_lab.config(text="Work", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_lab.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global timer
    mnt = math.floor(seconds/60)
    scn = seconds % 60
    if scn < 10:
        scn = f"0{scn}"
    canvas.itemconfig(timer_text, text=f"{mnt}:{scn}")
    if seconds > 0:
       timer =  window.after(1000, count_down,  seconds -1)
    else:
        start_timer()
        if reps%2 == 0:
            check_lab.config(text=f"{check_lab["text"] + "✔"}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="./tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_lab = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timer_lab.grid(column=1, row=0)

check_lab = Label(fg=GREEN, bg=YELLOW)
check_lab.grid(column=1, row=3)

start_but = Button(text="Start", command=start_timer, highlightthickness=0)
start_but.grid(column=0, row=2)

reset_but = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_but.grid(column=2, row=2)


window.mainloop()