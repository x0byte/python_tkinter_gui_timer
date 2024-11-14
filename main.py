from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame

pygame.mixer.init()


total_seconds = 0
is_Paused = False

def play_music():
    pygame.mixer.music.load("Assets/beeping_sound.mp3")
    
    pygame.mixer.music.play(loops=3)


def update_timer():
    global total_seconds

    if is_Paused: return

    if total_seconds > 0:
        total_seconds -= 1
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        #update the label in each iteration
        timer_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        root.after(1000, update_timer)

    else:
        play_music()
        timer_label.config(text="TIME'S UP!", font=("Helvetica", 15, "bold"))

def start_coutdown():
    global total_seconds
    total_seconds = convert_input_to_seconds()
    update_timer()

def convert_input_to_seconds():
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
    except ValueError:
        print("Invalid input, please enter numeric values.")
        return 0  
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

root = Tk()
root.geometry("450x350")
root.minsize(450, 350)
root.maxsize(450, 350)
root.title("Countdown Timer")
root.configure(background="gray10")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

input_frame = Frame(root, background="gray10")
input_frame.grid(row=0, column=0, columnspan=3, rowspan=3, sticky="nsew")

# Title label centered in the grid
lbl_title = Label(input_frame, text="COUNTDOWN TIMER", font=("Helvetica", 15, "bold"), background="grey10", foreground="white")
lbl_title.grid(row=0, column=0, columnspan=3, sticky="nsew", ipady=23)

lbl_hours = Label(input_frame, text="HOURS", font=("Helvetica", 10, "bold"), background="gray10", foreground="white")
lbl_hours.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

lbl_minutes = Label(input_frame, text="MINUTES", font=("Helvetica", 10, "bold"), background="gray10", foreground="white")
lbl_minutes.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

lbl_seconds = Label(input_frame, text="SECONDS", font=("Helvetica", 10, "bold"), background="gray10", foreground="white")
lbl_seconds.grid(row=1, column=2, padx=20, pady=5, sticky="nsew")

# Hour entry 
hours_entry = Entry(input_frame, width=10, background="gray14",foreground="white", justify="center",borderwidth=0, relief="flat", highlightthickness=0, font=("Helvetica", 14))
hours_entry.grid(row=2, column=0, padx=20, pady=5, ipady=10, sticky="nsew")
hours_entry.insert(0, "0")

# Minute entry 
minutes_entry = Entry(input_frame, width=10, background="gray14",foreground="white", justify="center",borderwidth=0, relief="flat", highlightthickness=0, font=("Helvetica", 14))
minutes_entry.grid(row=2, column=1, padx=20, pady=5, ipady=10, sticky="nsew")
minutes_entry.insert(0, "0")

# Second entry 
seconds_entry = Entry(input_frame, width=10, background="gray14", foreground="white", justify="center",borderwidth=0, relief="flat", highlightthickness=0, font=("Helvetica", 14))
seconds_entry.grid(row=2, column=2, padx=20, pady=5, ipady=10, sticky="nsew")
seconds_entry.insert(0, "30")

# Start button 
start_button = Button(input_frame, command=lambda:start_coutdown(), text="Start", font=("Helvetica", 12, "bold"), bg="limegreen", fg="white",borderwidth=0, relief="flat", highlightthickness=0)
start_button.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="nsew", ipady=10)


timer_label = Label(input_frame, font=("Helvetica", 20), fg="white", background="gray10")
timer_label.grid(row=4, column=0, columnspan=3, pady=20)


input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)
input_frame.grid_columnconfigure(2, weight=1)

root.mainloop()
