import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup

def track_book_price():
    #url
    url = "http://books.toscrape.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    first_book = soup.find("article", class_="product_pod")
    
    if first_book:
        title = first_book.find("h3").find("a")["title"]
        price = first_book.find("p", class_="price_color").get_text().strip()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{current_time}] Book: {title} | Current Price: {price}")
        
        # ─── NEW CSV HOOK ──────────────────────────────────────────────────
        # Check if the CSV file already exists on your computer
        file_exists = os.path.isfile("price_history.csv")
        
        # Open (or create) a file named price_history.csv in "append" mode
        with open("price_history.csv", mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            # If it's a brand new file, write the column headers first
            if not file_exists:
                writer.writerow(["Timestamp", "Book Title", "Price"])
                
            # Write our freshly scraped data row into the spreadsheet
            writer.writerow([current_time, title, price])
            
        print("Successfully saved data row to price_history.csv!")
        # ───────────────────────────────────────────────────────────────────
    else:
        print("Could not find any books on the page.")

if __name__ == "__main__":
    track_book_price()
