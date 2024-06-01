# Here we are creating a visualization of a DNA Sequence
# You can either upload a file or copy and paste the sequence
# you want information about and want to visually see it.

import tkinter as tk
from tkinter import filedialog, messagebox
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to analyze DNA sequence
def analyze_sequence(seq):
    seq = Seq(seq)
    gc_content = gc_fraction(seq) * 100  # Convert fraction to percentage
    codon_usage = {}
    for i in range(0, len(seq) - 2, 3):
        codon = str(seq[i:i+3])
        if codon in codon_usage:
            codon_usage[codon] += 1
        else:
            codon_usage[codon] = 1
    return gc_content, codon_usage

# Function to visualize GC content
def visualize_gc_content(gc_content):
    plt.figure(figsize=(6, 4))
    plt.bar(['GC Content'], [gc_content])
    plt.ylabel('Percentage')
    plt.title('GC Content')
    plt.ylim(0, 100)
    plt.show()

# Function to visualize codon usage
def visualize_codon_usage(codon_usage):
    codons = list(codon_usage.keys())
    counts = list(codon_usage.values())
    plt.figure(figsize=(12, 6))
    sns.barplot(x=codons, y=counts, palette='viridis')
    plt.xlabel('Codon')
    plt.ylabel('Count')
    plt.title('Codon Usage')
    plt.xticks(rotation=90)
    plt.show()

# Function to visualize DNA sequence
def visualize_dna_sequence(seq):
    colors = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'orange'}
    fig, ax = plt.subplots(figsize=(12, 1))
    for i, nucleotide in enumerate(seq):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=colors.get(nucleotide, 'black')))
        ax.text(i + 0.5, 0.5, nucleotide, ha='center', va='center', color='white')
    ax.set_xlim(0, len(seq))
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

# Main application class
class DNAAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Sequence Analyzer")
        self.root.geometry("600x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.sequence_label = tk.Label(self.root, text="DNA Sequence:")
        self.sequence_label.pack(pady=5)
        self.sequence_entry = tk.Text(self.root, height=10, width=50)
        self.sequence_entry.pack(pady=5)
        
        self.load_button = tk.Button(self.root, text="Load Sequence from File", command=self.load_sequence)
        self.load_button.pack(pady=5)
        
        self.analyze_button = tk.Button(self.root, text="Analyze Sequence", command=self.analyze_sequence)
        self.analyze_button.pack(pady=5)
        
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)
    
    def load_sequence(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return
        try:
            with open(file_path, 'r') as file:
                sequence = file.read().replace('\n', '')  # Remove any newline characters
                self.sequence_entry.delete(1.0, tk.END)
                self.sequence_entry.insert(tk.END, sequence)
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred while reading the file: {e}")
    
    def analyze_sequence(self):
        seq = self.sequence_entry.get(1.0, tk.END).strip()
        if not seq:
            messagebox.showerror("Input Error", "Please enter a DNA sequence")
            return
        
        try:
            gc_content, codon_usage = analyze_sequence(seq)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"GC Content: {gc_content:.2f}%\n\n")
            self.result_text.insert(tk.END, "Codon Usage:\n")
            for codon, count in codon_usage.items():
                self.result_text.insert(tk.END, f"{codon}: {count}\n")
            
            visualize_gc_content(gc_content)
            visualize_codon_usage(codon_usage)
            visualize_dna_sequence(seq)
        except Exception as e:
            messagebox.showerror("Analysis Error", f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DNAAnalyzerApp(root)
    root.mainloop()