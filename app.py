import threading
import tkinter as tk
from tkinter import ttk
from scraper import scrape_books
from scoring import QualityScorer
from database import Database


class App:
    def __init__(self, root):
        self.root = root
        root.title("Books to Scrape Scraper")

        self.url_entry = tk.Entry(root, width=60)
        self.url_entry.insert(0, "http://books.toscrape.com/")
        self.url_entry.pack()

        self.btn_scrape = tk.Button(root, text="Lets Go", command=self.start_scraping)
        self.btn_scrape.pack(pady=5)

        self.tree = ttk.Treeview(root, columns=("Title", "Price", "Images", "Score"), show="headings", height=12)
        for col in ("Title", "Price", "Images", "Score"):
            self.tree.heading(col, text=col)
        self.tree.pack()

        self.log = tk.Label(root, text="", fg="red")
        self.log.pack(pady=5)

    def start_scraping(self):
        threading.Thread(target=self._scrape_thread).start()

    def _scrape_thread(self):
        listings = scrape_books(self.url_entry.get())
        scorer = QualityScorer()
        db = Database()
        for row in self.tree.get_children():
            self.tree.delete(row)

        for listing in listings:
            points, missing = scorer.score(listing)

            db.add({
                "title": listing.title,
                "price": listing.price,
                "description": listing.description,
                "images": ",".join(listing.images),
                "score": points,
                "missing": "; ".join(missing)
            })

            self.tree.insert("", "end",
                             values=(listing.title, listing.price, len(listing.images), points))

        self.log.config(text=f"{len(listings)} listings found and saved.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

