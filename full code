import sqlite3
import threading
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BaseModel:
    def __init__(self):
        self.id = None

class Listing(BaseModel):
    def __init__(self, title: str, price: float = 0, description: str = "", images: List[str] = None):
        super().__init__()
        self.title = title
        self.price = price
        self.description = description
        self.images = images or []

    def summary(self, detailed=False):
        if detailed:
            return f"Title: {self.title}, Price: {self.price}, Description: {self.description}, Images: {len(self.images)}"
        return f"Title: {self.title}, Price: {self.price}, Images: {len(self.images)}"

class AbstractScorer(ABC):
    @abstractmethod
    def score(self, listing: Listing):
        pass

class QualityScorer(AbstractScorer):
    def score(self, listing: Listing):
        points = 0
        missing = []

        points += self._score_title(listing.title, missing)
        points += self._score_price(listing.price, missing)
        points += self._score_description(listing.description, missing)
        points += self._score_images(len(listing.images), missing)

        return max(0, min(100, points)), missing

    @staticmethod
    def _score_title(title, missing):
        if title:
            return 10
        missing.append("Title missing")
        return 0

    @staticmethod
    def _score_price(price, missing):
        if price is None:
            missing.append("Price missing")
            return 0
        if price < 10:
            missing.append("Price may be low")
        return 20

    @staticmethod
    def _score_description(description, missing):
        length = len(description)
        if length >= 100:
            return 20
        if length >= 20:
            return 10
        missing.append("Description too short")
        return 0

    @staticmethod
    def _score_images(count, missing):
        if count >= 3:
            return 20
        if count >= 1:
            return 10
        missing.append("No images")
        return 0

class Database(BaseModel):
    def __init__(self, sqlite_db="listings.db"):
        super().__init__()
        self.conn = sqlite3.connect(sqlite_db)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            description TEXT,
            images TEXT,
            score REAL,
            missing TEXT
        )
        """)
        self.conn.commit()

    def add(self, data):
        self.cursor.execute("""
        INSERT INTO listings (title, price, description, images, score, missing)
        VALUES (:title, :price, :description, :images, :score, :missing)
        """, data)
        self.conn.commit()

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
        options = Options()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(self.url_entry.get())

        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
        )

        # Get HTML and parse with BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        driver.quit()

        # First 10 books
        cards = soup.select("article.product_pod")[:10]
        listings = []

        for card in cards:
            title_tag = card.select_one("h3 a")
            title = title_tag["title"] if title_tag else "No title"

            price_tag = card.select_one(".price_color")
            price = float(price_tag.get_text().replace("£", "").strip()) if price_tag else 0

            img_tag = card.select_one("img")
            images = [img_tag["src"]] if img_tag else []

            listings.append(Listing(title=title, price=price, description="BooksToScrape", images=images))

        # Database and scorer
        db = Database()
        scorer = QualityScorer()

        # Clear treeview
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
            self.tree.insert("", "end", values=(listing.title, listing.price, len(listing.images), points))

        self.log.config(text=f"{len(listings)} listings found and saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
