#  TASK 1 PROJECT: Book Data Scraper
#  Website: books.toscrape.com (safe practice site)
#  What it does: Scrapes book titles, prices, ratings, 
#                availability from multiple pages


import requests
from bs4 import BeautifulSoup
import time

# STEP 1: Convert word ratings to numbers
# e.g. "Three" -> 3
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# STEP 2: Scrape a single page and return list of books
def scrape_page(url):
    """
    Takes a URL, fetches the HTML, finds all books on that page,
    and returns them as a list of dictionaries.
    """
    books = []

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200 = OK)
    if response.status_code != 200:
        print(f"  [!] Failed to fetch: {url}")
        return books

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers — each book is inside <article class="product_pod">
    book_cards = soup.find_all("article", class_="product_pod")

    for card in book_cards:
        # --- Title ---
        # The title is inside <h3><a title="Book Title">
        title = card.find("h3").find("a")["title"]

        # --- Price ---
        # Price is inside <p class="price_color">
        price_text = card.find("p", class_="price_color").text.strip()
        # Remove the £ symbol and convert to float
        price = float(price_text.replace("£", "").replace("Â", ""))

        # --- Rating ---
        # Rating is a CSS class like "star-rating Three"
        rating_class = card.find("p", class_="star-rating")["class"]
        # rating_class looks like ["star-rating", "Three"]
        rating_word = rating_class[1]
        rating = RATING_MAP.get(rating_word, 0)

        # --- Availability ---
        availability = card.find("p", class_="availability").text.strip()

        # Store everything in a dictionary
        books.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "availability": availability
        })

    return books


# STEP 3: Scrape multiple pages
def scrape_books(num_pages=5):
    """
    Scrapes the given number of pages from books.toscrape.com
    Returns all books as a combined list.
    """
    base_url = "https://books.toscrape.com/catalogue/"
    all_books = []

    print(f"\n Starting scraper — will scrape {num_pages} page(s)\n")

    for page_num in range(1, num_pages + 1):
        # Build the URL for each page
        if page_num == 1:
            url = "https://books.toscrape.com/catalogue/page-1.html"
        else:
            url = f"{base_url}page-{page_num}.html"

        print(f"  Scraping page {page_num}: {url}")
        books = scrape_page(url)
        all_books.extend(books)
        print(f"  Found {len(books)} books on this page")

        # Be polite — wait 1 second between requests
        # (Don't hammer servers with too many requests too fast)
        time.sleep(1)

    print(f"\n Done! Total books collected: {len(all_books)}\n")
    return all_books


# STEP 4: Run it (only when this file is run directly)
if __name__ == "__main__":
    # Scrape 3 pages (3 x 20 books = 60 books)
    books = scrape_books(num_pages=3)

    # Print first 5 results as a preview
    print("--- Preview (first 5 books) ---")
    for book in books[:5]:
        print(f"  {book['title'][:50]:<50} | £{book['price_gbp']:.2f} | {book['rating']}★ | {book['availability']}")
