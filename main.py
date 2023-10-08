from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # 25
SHORT_BREAK_MIN = 5  # 5
LONG_BREAK_MIN = 20  # 20

# ---------------------------- TIMER RESET ------------------------------- # 
counter = 0
timer = None


def reset():
    window.after_cancel(timer)
    bg_canvas.itemconfig(time_label, text="0:00")
    main_label.config(text="Timer", font=("Courier", 55), fg=PINK)
    checkbox_1.config(text=" ")
    checkbox_2.config(text=" ")
    global counter
    counter = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global counter
    counter += 1

    if counter == 1 or counter == 3:
        main_label.config(text="Work", fg=RED)
        countdown(WORK_MIN * 60)
    if counter == 2 or counter == 4:
        main_label.config(text="Break", fg=GREEN)
        countdown(SHORT_BREAK_MIN * 60)
    if counter == 5:
        main_label.config(text="Long Break", font=("Courier", 30), fg=YELLOW)
        countdown(LONG_BREAK_MIN * 60)
    if counter == 2:
        checkbox_1.config(text="✔")
    if counter == 4:
        checkbox_2.config(text="✔")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    bg_canvas.itemconfig(time_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(500, 500)
window.title("Pomodoro Productivity Timer")

window.after(1000, countdown)

background = PhotoImage(file="tomato.png")

bg_canvas = Canvas(width=500, height=500)
bg_canvas.pack(fill="both", expand=True)
bg_canvas.place(x=145, y=125)
bg_canvas.create_image(3, 0, image=background, anchor="nw")
time_label = bg_canvas.create_text(105, 137, text="0:00", font=("Arial", 75))

main_label = Label(text="Work", font=("Courier", 55), fg=RED)
main_label.place(x=175, y=45)

button_start = Button(text="Start", command=start_timer)   # add command later
button_start.place(x=90, y=365)

button_reset = Button(text="Reset", command=reset)    # add command later
button_reset.place(x=330, y=365)

checkbox_1 = Label(text="     ")
checkbox_1.place(x=202, y=370)
checkbox_2 = Label(text=" ")
checkbox_2.place(x=224, y=370)
# checkbox_3 = Label(text=" ")
# checkbox_3.place(x=244, y=370)
# checkbox_4 = Label(text=" ")
# checkbox_4.place(x=264, y=370)

window.mainloop()
