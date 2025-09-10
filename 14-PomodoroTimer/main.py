from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Calibri"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_marks.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ''
        for _ in range(0, math.floor(reps / 2)):
            marks += '✅'
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# 1. Window Set Up:
window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100)

# 2. Canvas Set Up:
canvas = Canvas(width=200, height=224)
image = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# 3. Labels:
title_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

check_marks = Label(fg=GREEN)
check_marks.grid(column=1, row=3)

# 4. Buttons:
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
