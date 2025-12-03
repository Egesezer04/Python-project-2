from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from models import Listing

def scrape_books(url: str):
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    driver.quit()

    cards = soup.select("article.product_pod")[:10]
    listings = []

    for card in cards:
        title_tag = card.select_one("h3 a")
        title = title_tag["title"] if title_tag else "No title"

        price_tag = card.select_one(".price_color")
        price = float(price_tag.get_text().replace("£", "").strip()) if price_tag else 0

        img_tag = card.select_one("img")
        images = [img_tag["src"]] if img_tag else []

        listings.append(Listing(title, price, "BooksToScrape", images))

    return listings