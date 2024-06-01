# So I created a JobScraper application where you can enter City and State Abbreviation.
# I know that some websites have this thing where they deny access to your request.
# But it does work! Just need to bypass those permissions.

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Listings Scraper")
        self.root.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Keyword:").pack(pady=10)
        self.keyword_entry = tk.Entry(self.root, width=50)
        self.keyword_entry.pack(pady=5)

        tk.Label(self.root, text="Location:").pack(pady=10)
        self.location_entry = tk.Entry(self.root, width=50)
        self.location_entry.pack(pady=5)

        tk.Button(self.root, text="Scrape Jobs", command=self.scrape_jobs).pack(pady=20)

        self.tree = ttk.Treeview(self.root, columns=("Title", "Company", "Location"), show="headings")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Company", text="Company")
        self.tree.heading("Location", text="Location")
        self.tree.pack(expand=True, fill='both')

    def scrape_jobs(self):
        keyword = self.keyword_entry.get()
        location = self.location_entry.get()
        if not keyword or not location:
            messagebox.showerror("Error", "Please enter both keyword and location")
            return

        url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            messagebox.showerror("Error", f"Failed to retrieve data: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard')

        self.tree.delete(*self.tree.get_children())
        for job in job_cards:
            title_elem = job.find('h2', class_='title')
            company_elem = job.find('span', class_='company')
            location_elem = job.find('div', class_='location')
            
            title = title_elem.text.strip() if title_elem else 'N/A'
            company = company_elem.text.strip() if company_elem else 'N/A'
            location = location_elem.text.strip() if location_elem else 'N/A'
            
            self.tree.insert("", tk.END, values=(title, company, location))

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()