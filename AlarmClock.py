# When I first made this application, I realized that it froze
# my VS Code. I did fix it with multithreading which is very
# useful. 
# But here we are going to make an alarm clock. It does work
# but the sound doesn't go off and I think to make the sound go off,
# we need to sync it with the system time that way it will work properly.

import pygame
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import threading

# Initialize Pygame
pygame.mixer.init()

def set_alarm():
    alarm_time = entry.get()
    try:
        valid_time = time.strptime(alarm_time, '%H:%M')
        alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time,))
        alarm_thread.daemon = True
        alarm_thread.start()
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format")

def check_alarm(alarm_time):
    current_time = datetime.now().strftime('%H:%M')
    while current_time != alarm_time:
        current_time = datetime.now().strftime('%H:%M')
        time.sleep(1)
    play_alarm()

def play_alarm():
    pygame.mixer.music.load("AlarmClockCreator\alarm_sound.mp3")  # Make sure you have an alarm sound file in the same directory
    pygame.mixer.music.play()
    messagebox.showinfo("Alarm", "Wake up!")

# GUI Setup
root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Set Alarm (HH:MM)").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=20)

root.mainloop()