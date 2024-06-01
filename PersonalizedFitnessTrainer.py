# This program is to create a personlized fitness trainer.
# It is very tedious, but awarding at the end. The goal is
# to add an api if you want to make it official and a working
# application.

import tkinter as tk
from tkinter import messagebox
import random
import json

class FitnessTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Fitness Trainer")
        self.root.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        
        self.age_label = tk.Label(self.root, text="Age:")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack(pady=5)
        
        self.weight_label = tk.Label(self.root, text="Weight (kg):")
        self.weight_label.pack(pady=5)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack(pady=5)
        
        self.height_label = tk.Label(self.root, text="Height (cm):")
        self.height_label.pack(pady=5)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.pack(pady=5)
        
        self.goal_label = tk.Label(self.root, text="Fitness Goal:")
        self.goal_label.pack(pady=5)
        self.goal_entry = tk.Entry(self.root)
        self.goal_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self.root, text="Generate Workout Plan", command=self.generate_plan)
        self.submit_button.pack(pady=20)
        
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)
    
    def generate_plan(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()
        goal = self.goal_entry.get()
        
        if not (name and age and weight and height and goal):
            messagebox.showerror("Input Error", "Please fill out all fields")
            return
        
        try:
            age = int(age)
            weight = float(weight)
            height = float(height)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid age, weight, and height")
            return
        
        # Placeholder for workout plan
        plan = self.create_workout_plan(goal)
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Workout Plan for {name}:\n\n{plan}")
        
        # Fetch user progress from wearable device (mock data)
        progress = self.fetch_wearable_data()
        self.result_text.insert(tk.END, f"\n\nUser Progress:\n{progress}")
    
    def create_workout_plan(self, goal):
        # Placeholder for a more sophisticated workout plan generation logic
        exercises = ["Push-ups", "Squats", "Burpees", "Lunges", "Plank"]
        plan = ""
        for exercise in exercises:
            reps = random.randint(10, 20)
            sets = random.randint(3, 5)
            plan += f"{exercise}: {sets} sets of {reps} reps\n"
        return plan
    
    def fetch_wearable_data(self):
        # Placeholder for Fitbit API integration (mock data)
        data = {
            "steps": 5000,
            "calories_burned": 200,
            "active_minutes": 30
        }
        return json.dumps(data, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrainerApp(root)
    root.mainloop()