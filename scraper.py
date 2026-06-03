import requests
from bs4 import BeautifulSoup
import datetime

def track_book_price():
    url = "http://books.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    first_book = soup.find("article", class_="product_pod")

    if first_book:
        title = first_book.find("h3").find("a")["title"]
        price = first_book.find("p", class_="price_color").text.strip()

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{current_time}] Book: {title}")
        print(f"Current Price: {price}")

    else:
        print("No books found.")

if __name__ == "__main__":
    track_book_price()