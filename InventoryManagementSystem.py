# Everything works on the inventory management system; I do want
# to make it better that way we can sell it to companies, a
# bookstore, so it will be easier for users to use it and not have
# any trouble. I want to add more functionalities to the note app,
# but I think it will take time before this one is ready.
# It does save into a database using SQLite3 to save everything that was entered.

import os
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt

DATABASE_DIR = r"C:\Users\Myranda\OneDrive\Portfolio\InventoryManagement"
DATABASE_PATH = os.path.join(DATABASE_DIR, "inventory.db")

os.makedirs(DATABASE_DIR, exist_ok=True)

def create_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (item_id) REFERENCES inventory(id)
        )"""
    )
    conn.commit()
    conn.close()

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack(expand=True, fill='both')

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack(side='left', padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Item", command=self.update_item)
        self.update_button.pack(side='left', padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Item", command=self.delete_item)
        self.delete_button.pack(side='left', padx=10, pady=10)

        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.load_inventory)
        self.refresh_button.pack(side='left', padx=10, pady=10)

        self.sell_button = tk.Button(self.root, text="Sell Item", command=self.sell_item)
        self.sell_button.pack(side='left', padx=10, pady=10)

        self.visualize_inventory_button = tk.Button(self.root, text="Visualize Inventory", command=self.visualize_inventory)
        self.visualize_inventory_button.pack(side='left', padx=10, pady=10)

        self.visualize_sales_button = tk.Button(self.root, text="Visualize Sales", command=self.visualize_sales)
        self.visualize_sales_button.pack(side='left', padx=10, pady=10)

        self.load_inventory()

    def add_item(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Item")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
        quantity_entry = tk.Entry(add_window)
        quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Price:").grid(row=2, column=0, padx=10, pady=10)
        price_entry = tk.Entry(add_window)
        price_entry.grid(row=2, column=1, padx=10, pady=10)

        def save_item():
            name = name_entry.get()
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())

            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
            conn.commit()
            conn.close()
            add_window.destroy()
            self.load_inventory()

        tk.Button(add_window, text="Save", command=save_item).grid(row=3, columnspan=2, pady=10)

    def update_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to update")
            return

        item_id = self.tree.item(selected_item)["values"][0]
        name = self.tree.item(selected_item)["values"][1]
        quantity = self.tree.item(selected_item)["values"][2]
        price = self.tree.item(selected_item)["values"][3]

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Item")

        tk.Label(update_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(update_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        name_entry.insert(0, name)  # Insert current name

        tk.Label(update_window, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
        quantity_entry = tk.Entry(update_window)
        quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        quantity_entry.insert(0, quantity)  # Insert current quantity

        tk.Label(update_window, text="Price:").grid(row=2, column=0, padx=10, pady=10)
        price_entry = tk.Entry(update_window)
        price_entry.grid(row=2, column=1, padx=10, pady=10)
        price_entry.insert(0, price)  # Insert current price

        def save_update():
            try:
                new_name = name_entry.get()
                new_quantity = int(quantity_entry.get())
                new_price = float(price_entry.get())

                conn = sqlite3.connect(DATABASE_PATH)
                cursor = conn.cursor()
                cursor.execute("UPDATE inventory SET name = ?, quantity = ?, price = ? WHERE id = ?", 
                               (new_name, new_quantity, new_price, item_id))
                conn.commit()
                conn.close()
                update_window.destroy()
                self.load_inventory()
            except ValueError as e:
                messagebox.showerror("Invalid input", f"Error: {e}")

        tk.Button(update_window, text="Save", command=save_update).grid(row=3, columnspan=2, pady=10)

    def delete_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete")
            return

        item_id = self.tree.item(selected_item)["values"][0]

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()
        self.load_inventory()

    def load_inventory(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        records = cursor.fetchall()
        for record in records:
            self.tree.insert("", tk.END, values=record)
        conn.close()

    def sell_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to sell")
            return

        item_id = self.tree.item(selected_item)["values"][0]
        item_name = self.tree.item(selected_item)["values"][1]

        sell_window = tk.Toplevel(self.root)
        sell_window.title(f"Sell Item - {item_name}")

        tk.Label(sell_window, text="Quantity:").grid(row=0, column=0, padx=10, pady=10)
        quantity_entry = tk.Entry(sell_window)
        quantity_entry.grid(row=0, column=1, padx=10, pady=10)

        def save_sale():
            try:
                quantity = int(quantity_entry.get())
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                conn = sqlite3.connect(DATABASE_PATH)
                cursor = conn.cursor()
                cursor.execute("SELECT quantity FROM inventory WHERE id = ?", (item_id,))
                current_quantity = cursor.fetchone()[0]

                if quantity > current_quantity:
                    messagebox.showerror("Error", "Insufficient stock")
                    return

                new_quantity = current_quantity - quantity
                cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?", (new_quantity, item_id))
                cursor.execute("INSERT INTO sales (item_id, quantity, date) VALUES (?, ?, ?)", (item_id, quantity, date))
                conn.commit()
                conn.close()
                sell_window.destroy()
                self.load_inventory()
            except ValueError as e:
                messagebox.showerror("Invalid input", f"Error: {e}")

        tk.Button(sell_window, text="Sell", command=save_sale).grid(row=1, columnspan=2, pady=10)

    def visualize_inventory(self):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name, quantity FROM inventory")
        records = cursor.fetchall()
        conn.close()

        items = [record[0] for record in records]
        quantities = [record[1] for record in records]

        plt.figure(figsize=(10, 5))
        plt.bar(items, quantities, color='blue')
        plt.xlabel('Items')
        plt.ylabel('Quantities')
        plt.title('Inventory Levels')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def visualize_sales(self):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT i.name, SUM(s.quantity) 
            FROM sales s 
            JOIN inventory i ON s.item_id = i.id 
            GROUP BY s.item_id
        """)
        records = cursor.fetchall()
        conn.close()

        items = [record[0] for record in records]
        quantities = [record[1] for record in records]

        plt.figure(figsize=(10, 5))
        plt.bar(items, quantities, color='green')
        plt.xlabel('Items')
        plt.ylabel('Quantities Sold')
        plt.title('Sales Trends')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    create_database()
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()