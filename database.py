import sqlite3

class Database:
    def __init__(self, sqlite_db="listings.db"):
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
