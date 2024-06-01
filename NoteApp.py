# This is an actual working note application that can be used.
# There can be some changes that are made to the code that way
# there is a possiblity that this will get published, but for now
# it is a work in progress if we want to meet that step.

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import font

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_note)
        file_menu.add_command(label="Open", command=self.open_note)
        file_menu.add_command(label="Save", command=self.save_note)
        file_menu.add_command(label="Save As", command=self.save_as_note)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)

        format_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Change Font", command=self.change_font)
        format_menu.add_command(label="Change Font Color", command=self.change_font_color)
        format_menu.add_command(label="Change Background Color", command=self.change_bg_color)
        format_menu.add_command(label="Change Text Background Color", command=self.change_text_bg_color)

    def new_note(self):
        self.text_area.delete(1.0, tk.END)

    def open_note(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)

    def save_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def save_as_note(self):
        self.save_note()

    def exit_app(self):
        self.root.quit()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def change_font(self):
        font_window = tk.Toplevel(self.root)
        font_window.title("Choose Font")

        tk.Label(font_window, text="Font Family:").grid(row=0, column=0, padx=10, pady=10)
        font_family = tk.StringVar(value="Arial")
        font_families = font.families()
        font_menu = tk.OptionMenu(font_window, font_family, *font_families)
        font_menu.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(font_window, text="Font Size:").grid(row=1, column=0, padx=10, pady=10)
        font_size = tk.StringVar(value="12")
        size_menu = tk.OptionMenu(font_window, font_size, *range(8, 72))
        size_menu.grid(row=1, column=1, padx=10, pady=10)

        def apply_font():
            new_font = (font_family.get(), font_size.get())
            self.text_area.config(font=new_font)
            font_window.destroy()

        tk.Button(font_window, text="Apply", command=apply_font).grid(row=2, columnspan=2, pady=10)

    def change_font_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(bg=color)
            
    def change_text_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(insertbackground=color, selectbackground=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()