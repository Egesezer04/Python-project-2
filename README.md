# Listing Quality Scoring System

A modern Python application that scrapes listing data (real estate, vehicles, books, etc.), analyzes listing quality, stores results in SQLite, and presents them in a clean Tkinter GUI.

---

## 🚀 Features

### ✅ Web Scraping

* Dynamic page loading using **Selenium**
* HTML parsing with **BeautifulSoup**
* Automatically extracts the **first 10 product listings**
* Uses **threading** to keep the GUI responsive

### ✅ Object‑Oriented Business Logic

* `BaseModel` — shared base structure
* `Listing` — unified listing model
* `AbstractScorer` — scoring interface
* `QualityScorer` — full scoring algorithm
* Clean, modular, extensible architecture
* Quality factors include:

  * Title
  * Price
  * Description
  * Image Count

### ✅ SQLite Database

* Automatic table creation
* Saves: title, price, description, images, score, missing fields
* Safe SQL insert using dictionary binding

### ✅ Tkinter GUI

* URL input field
* **“Let’s Go”** scrape button
* Interactive table (TreeView)
* Log output window
* Background threading support

---

## 🏗️ Project Architecture Overview

```
/ project
│── app.py               # Main Tkinter App
│── scraper.py           # Selenium + BS4 logic
│── models.py            # BaseModel & Listing
│── scorer.py            # AbstractScorer & QualityScorer
│── database.py          # SQLite handler
│── README.md            # This file
```

### Main Components

* **BaseModel** → Unique ID structure
* **Listing** → Listing object
* **AbstractScorer** → Enforced scoring interface
* **QualityScorer** → Quality scoring rules
* **Database** → SQLite operations
* **App** → Tkinter GUI

---

## 📊 Quality Scoring Logic

| Criterion   | Points | Notes                |
| ----------- | ------ | -------------------- |
| Title       | 0–10   | 0 if missing         |
| Price       | 0–20   | Low-price warning    |
| Description | 0–20   | Based on text length |
| Images      | 0–20   | 0, 1–2, or 3+ images |

Score = sum of all criteria.

---
## Requirements
 * **Python 3.10/Python 3.11
 * **Tkinter (Python ile birlikte gelir)  
 * **Selenium  
 * **BeautifulSoup4  
 * **Webdriver Manager
 


## 🛠️ Installation

### 1️⃣ Install dependencies

```bash
pip install selenium bs4 webdriver-manager
```

### 2️⃣ Run the project

```bash
python app.py
```

### 3️⃣ GUI will open

type a URL → click **“Let’s Go”**

---

## 🌐 Scraping Workflow

1. ChromeDriver installs automatically via `webdriver-manager`
2. Selenium loads webpage
3. BeautifulSoup parses the HTML
4. First 10 products are extracted
5. A `Listing` object is generated
6. Each listing is scored
7. Data is saved to SQLite + displayed in GUI

---

## 🖥️ How to Use the GUI

* Enter any product/listing URL (default: *books.toscrape.com*)
* Press **Let’s Go**
* Scraper fetches & evaluates first 10 items
* Quality score + missing fields appear instantly

---

## 📦 Technologies Used

* **Tested on Windows 11, and Google Chrome (latest version) using ChromeDriver via Webdriver Manager

* **Python 3.10+**
* **Selenium WebDriver**
* **BeautifulSoup (bs4)**
* **SQLite3**
* **Tkinter GUI**
* **Object-Oriented Architecture**
* **Threading**




