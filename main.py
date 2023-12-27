from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#006400"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle = 0
time_spent = -1

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global run
    run = False


def time_studied():

    if time_spent == -1:
        s = "0:00"
    elif time_spent % 60 == 0:
        s = f"{str(time_spent // 60)}:00"
    elif time_spent % 60 < 10:
        s = f"{str(time_spent // 60)}:0{str(time_spent % 60)}"
    else:
        s = f"{str(time_spent // 60)}:{str(time_spent % 60)}"

    time_label = Label(text=s, font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=PINK)
    time_label.grid(column=1, row=2)
    window.after(5000, clear, time_label)


def clear(time_label):
    time_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global run
    run = True

    global cycle
    cycle += 1


    if cycle % 8 == 0:
        label.config(text="Break!")
        count_down(LONG_BREAK_MIN*60)
    elif cycle % 2 == 0:
        label.config(text="Break!")
        count_down(SHORT_BREAK_MIN*60)
    else:
        label.config(text="Study!")
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time):
    global time_spent

    if not run:
        time_spent = -1
        canvas.itemconfig(timer_text, text="0:00")
        label.config(text="Study Timer!")
        return

    if time >= 0:
        if time % 60 == 0:
            s = f"{str(time // 60)}:00"
        elif time % 60 < 10:
            s = f"{str(time // 60)}:0{str(time % 60)}"
        else:
            s = f"{str(time // 60)}:{str(time % 60)}"
        canvas.itemconfig(timer_text, text=s)
        window.after(1000, count_down, time - 1)
        time_spent += 1
    else:
        start()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Study Timer")
window.config(width=500, height=500, padx=100, pady=100, bg=PINK)

label = Label(text="Study Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=PINK)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=PINK, borderwidth=3, relief="flat", highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(105, 120, text="0:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), padx=5, pady=5, bg=YELLOW, command=start)
start_button.grid(column=0, row=2)

time_studied = Button(text="Time Spent", font=(FONT_NAME, 10, "bold"), padx=5, pady=5, bg=YELLOW, command=time_studied)
time_studied.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), padx=5, pady=5, bg=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
