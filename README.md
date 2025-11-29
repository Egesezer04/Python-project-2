📘 Listing Quality Scoring System
A Quality Analyzer for Real Estate / Vehicle / Book Listings using Web Scraping, Selenium, SQLite, OOP, and GUI
This project is a Python-based application designed to scrape listing data from the web and evaluate the quality of each listing. It uses modern software principles such as object-oriented programming, abstraction, scoring logic, web scraping (Selenium + BeautifulSoup), SQLite database management, and a Tkinter graphical interface.

🚀 Features ✅ Web Scraping
• Dynamic page loading using Selenium
• HTML parsing with BeautifulSoup
•Automatically extracts the first 10 product listings
•Uses threading to keep the GUI responsive

✅ Object-Oriented Business Logic
•BaseModel — shared base class
•Listing — structured listing model
•AbstractScorer — scoring interface using abstraction
•QualityScorer — full scoring algorithm
•Modular, clean, and extensible architecture
•Quality evaluation based on:
•Title
•Price
•Description
•Image count

✅ SQLite Database
•Automatic table creation
•Stores Title, Price, Description, Images, Score, Missing Fields
•Safe dictionary-based SQL insert

✅ Tkinter GUI
•URL input field
• “Lets Go” scrape button
•Table (TreeView) to display listings
•Log message section
•Threading support to prevent freezing

🏗️ Project Architecture Overview
• BaseModel
Shared ID structure
• Listing
Listing data model
• AbstractScorer
Abstract scoring interface
• QualityScorer
Listing quality scoring logic
• Database
SQLite management
• App (Tkinter)
Graphical user interface


📊 Quality Scoring Logic
Criterion	Points	Explanation
Title	10	0 if missing
Price	20	Warning if unusually low
Description	0–20	Based on length
Images	0–20	0, 1–2, or 3+ images

🛠️ Installation
1️⃣ Install required package
•pip install selenium bs4 webdriver-manager


2️⃣ Run the project
•python app.py

3️⃣ GUI opens
•click Lets Go


🌐 Scraping Workflow
•ChromeDriver installs automatically via webdriver-manager
•Selenium loads the webpage
•BeautifulSoup parses HTML
•First 10 products are extracted
•A Listing object is created for each

🖥️ How to Use the GUI
•Enter any URL (default: books.toscrape.com)
•Click Lets Go
•App scrapes the first 10 items
•Each listing is scored for quality
•Results are saved to SQLite
•Results appear instantly in the table

