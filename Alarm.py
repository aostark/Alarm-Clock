import datetime
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import sys

root = tk.Tk()
root.title("Alarm clock")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Background
logo = Image.open("alarm.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.place(x=0, y=0)

# Alarm settings
alarm = tk.Entry(root)


# Current time
def realtime():
    day = time.strftime("%a")
    day_of_month = time.strftime("%d")
    month = time.strftime("%B")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    current_time.config(text=day + ", " + month + " " + day_of_month + "  " + hour + ":" + minute + ":" + second)
    current_time.after(1000, realtime)


def set_alarm():
    global entry1, entry2
    window = Toplevel()
    window.geometry("300x150")
    hours = Label(window, text="At what hour do you want your clock to ring?\n (24hr is preferred format)")
    hours.place(x=10, y=5)
    entry1 = Entry(window, relief=GROOVE)
    entry1.place(x=80, y=40)
    minutes = Label(window, text='At what minute do you want your clock to ring?')
    minutes.place(x=20, y=55)
    entry2 = Entry(window, relief=GROOVE)
    entry2.place(x=80, y=80)

    begin = Button(window, text="Start", relief=GROOVE)
    begin.place(x=130, y=120)
    begin.bind("<Button-1>", begin_alarm)


def begin_alarm(event):
    global entry1, entry2
    hours_set = entry1.get()
    minutes_set = entry2.get()
    while True:
        if int(hours_set) == datetime.datetime.now().hour and int(minutes_set) == datetime.datetime.now().minute:
            playsound("Alarm.mp3")
            messagebox.showinfo("Alarm!", "Time is up!")


current_time = Label(root, font=("Cambria", 16))
current_time.pack()

# Set button
set_text = tk.StringVar()
set_btn = tk.Button(root, textvariable=set_text, command=lambda: set_alarm(), font="Helvetica", bg="#20bebe",
                    fg="white", height=2, width=12)
set_text.set("Set alarm")
set_btn.place(x=150, y=330)

canvas.pack()
realtime()
root.mainloop()
