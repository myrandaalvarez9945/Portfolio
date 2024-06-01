import os
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt

DATABASE_DIR = r"C:\Users\Myranda\OneDrive\Portfolio\EventPlannerManagement"
DATABASE_PATH = os.path.join(DATABASE_DIR, "event_planner.db")

os.makedirs(DATABASE_DIR, exist_ok=True)

def create_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS rsvps (
            id INTEGER PRIMARY KEY,
            event_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            response TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )"""
    )
    conn.commit()
    conn.close()

class EventPlannerApp(tk.Frame):
    def __init__(self, root, width=800, height=600):
        super().__init__(root, width=width, height=height)  # Call the parent class (tk.Frame) constructor
        self.root = root
        self.root.title("Event Planner")
        self.pack(expand=True, fill='both')  # Ensure the Frame expands to fill the root window

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Title", "Date", "Time", "Location", "Description"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Description", text="Description")
        self.tree.pack(expand=True, fill='both')

        self.add_button = tk.Button(self, text="Add Event", command=self.add_event)
        self.add_button.pack(side='left', padx=10, pady=10)

        self.update_button = tk.Button(self, text="Update Event", command=self.update_event)
        self.update_button.pack(side='left', padx=10, pady=10)

        self.delete_button = tk.Button(self, text="Delete Event", command=self.delete_event)
        self.delete_button.pack(side='left', padx=10, pady=10)

        self.refresh_button = tk.Button(self, text="Refresh", command=self.load_events)
        self.refresh_button.pack(side='left', padx=10, pady=10)

        self.invite_button = tk.Button(self, text="Send Invitations", command=self.send_invitations)
        self.invite_button.pack(side='left', padx=10, pady=10)

        self.rsvp_button = tk.Button(self, text="Track RSVPs", command=self.track_rsvps)
        self.rsvp_button.pack(side='left', padx=10, pady=10)

        self.load_events()

    def add_event(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Event")

        tk.Label(add_window, text="Title:").grid(row=0, column=0, padx=10, pady=10)
        title_entry = tk.Entry(add_window)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        date_entry = tk.Entry(add_window)
        date_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Time (HH:MM):").grid(row=2, column=0, padx=10, pady=10)
        time_entry = tk.Entry(add_window)
        time_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Location:").grid(row=3, column=0, padx=10, pady=10)
        location_entry = tk.Entry(add_window)
        location_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Description:").grid(row=4, column=0, padx=10, pady=10)
        description_entry = tk.Entry(add_window)
        description_entry.grid(row=4, column=1, padx=10, pady=10)

        def save_event():
            title = title_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            location = location_entry.get()
            description = description_entry.get()

            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO events (title, date, time, location, description) VALUES (?, ?, ?, ?, ?)",
                           (title, date, time, location, description))
            conn.commit()
            conn.close()
            add_window.destroy()
            self.load_events()

        tk.Button(add_window, text="Save", command=save_event).grid(row=5, columnspan=2, pady=10)

    def update_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an event to update")
            return

        item_id = self.tree.item(selected_item)["values"][0]
        title = self.tree.item(selected_item)["values"][1]
        date = self.tree.item(selected_item)["values"][2]
        time = self.tree.item(selected_item)["values"][3]
        location = self.tree.item(selected_item)["values"][4]
        description = self.tree.item(selected_item)["values"][5]

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Event")

        tk.Label(update_window, text="Title:").grid(row=0, column=0, padx=10, pady=10)
        title_entry = tk.Entry(update_window)
        title_entry.grid(row=0, column=1, padx=10, pady=10)
        title_entry.insert(0, title)

        tk.Label(update_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        date_entry = tk.Entry(update_window)
        date_entry.grid(row=1, column=1, padx=10, pady=10)
        date_entry.insert(0, date)

        tk.Label(update_window, text="Time (HH:MM):").grid(row=2, column=0, padx=10, pady=10)
        time_entry = tk.Entry(update_window)
        time_entry.grid(row=2, column=1, padx=10, pady=10)
        time_entry.insert(0, time)

        tk.Label(update_window, text="Location:").grid(row=3, column=0, padx=10, pady=10)
        location_entry = tk.Entry(update_window)
        location_entry.grid(row=3, column=1, padx=10, pady=10)
        location_entry.insert(0, location)

        tk.Label(update_window, text="Description:").grid(row=4, column=0, padx=10, pady=10)
        description_entry = tk.Entry(update_window)
        description_entry.grid(row=4, column=1, padx=10, pady=10)
        description_entry.insert(0, description)

        def save_update():
            new_title = title_entry.get()
            new_date = date_entry.get()
            new_time = time_entry.get()
            new_location = location_entry.get()
            new_description = description_entry.get()

            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("UPDATE events SET title = ?, date = ?, time = ?, location = ?, description = ? WHERE id = ?",
                           (new_title, new_date, new_time, new_location, new_description, item_id))
            conn.commit()
            conn.close()
            update_window.destroy()
            self.load_events()

        tk.Button(update_window, text="Save", command=save_update).grid(row=5, columnspan=2, pady=10)

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an event to delete")
            return

        item_id = self.tree.item(selected_item)["values"][0]

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM events WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()
        self.load_events()

    def load_events(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, date, time, location, description FROM events")
        records = cursor.fetchall()
        for record in records:
            self.tree.insert("", tk.END, values=record)
        conn.close()

    def send_invitations(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an event to send invitations")
            return

        item_id = self.tree.item(selected_item)["values"][0]
        title = self.tree.item(selected_item)["values"][1]

        invite_window = tk.Toplevel(self.root)
        invite_window.title(f"Send Invitations - {title}")

        tk.Label(invite_window, text="Recipient Emails (comma separated):").grid(row=0, column=0, padx=10, pady=10)
        emails_entry = tk.Entry(invite_window, width=50)
        emails_entry.grid(row=0, column=1, padx=10, pady=10)

        def send_invites():
            emails = emails_entry.get().split(",")
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT title, date, time, location, description FROM events WHERE id = ?", (item_id,))
            event = cursor.fetchone()
            conn.close()

            subject = f"Invitation: {event[0]}"
            message = f"""
            You are invited to the following event:

            Title: {event[0]}
            Date: {event[1]}
            Time: {event[2]}
            Location: {event[3]}
            Description: {event[4]}

            Please RSVP by replying to this email.
            """

            try:
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart

                sender_email = "your_email@example.com"
                sender_password = "your_password"

                for email in emails:
                    msg = MIMEMultipart()
                    msg["From"] = sender_email
                    msg["To"] = email.strip()
                    msg["Subject"] = subject

                    msg.attach(MIMEText(message, "plain"))

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, email.strip(), msg.as_string())
                    server.quit()

                messagebox.showinfo("Success", "Invitations sent successfully")
                invite_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send invitations: {e}")

        tk.Button(invite_window, text="Send Invitations", command=send_invites).grid(row=1, columnspan=2, pady=10)

    def track_rsvps(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an event to track RSVPs")
            return

        item_id = self.tree.item(selected_item)["values"][0]
        title = self.tree.item(selected_item)["values"][1]

        rsvp_window = tk.Toplevel(self.root)
        rsvp_window.title(f"Track RSVPs - {title}")

        tree = ttk.Treeview(rsvp_window, columns=("ID", "Name", "Email", "Response"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.heading("Response", text="Response")
        tree.pack(expand=True, fill='both')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, response FROM rsvps WHERE event_id = ?", (item_id,))
        records = cursor.fetchall()
        for record in records:
            tree.insert("", tk.END, values=record)
        conn.close()

if __name__ == "__main__":
    create_database()
    root = tk.Tk()
    app = EventPlannerApp(root)
    root.mainloop()