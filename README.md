# Task 1 Project — Book Data Scraper
**Subject:** Data Collection using Web Scraping  
**Site scraped:** books.toscrape.com (safe, legal practice site)  
**Language:** Python 3  

---

## What this project does

This project scrapes book data (title, price, rating, availability)
from multiple pages of books.toscrape.com and saves it as a CSV dataset.
It also includes basic data analysis and filtering.

---

## Project structure

```
book_scraper/
│
├── scraper.py         ← Core scraper (fetches + parses HTML)
├── save_data.py       ← Runs scraper, saves CSV, prints analysis
├── filter_data.py     ← Load CSV and filter/search the data
├── requirements.txt   ← Libraries needed
└── README.md          ← This file
```

---

## How to set up and run

### Step 1 — Install libraries
Open terminal in this folder and run:
```
pip install -r requirements.txt
```

### Step 2 — Run the scraper and save data
```
python save_data.py
```
This will:
- Scrape 3 pages (60 books)
- Save them to `books_dataset.csv`
- Print analysis in the terminal

### Step 3 — Filter and search the data
```
python filter_data.py
```
This loads the saved CSV and runs example filters.

---

## Libraries used and why

| Library | Why we used it |
|---|---|
| `requests` | Fetches the HTML of a webpage |
| `BeautifulSoup (bs4)` | Parses HTML and lets us find specific tags |
| `pandas` | Saves data to CSV and helps with analysis |
| `time` | Adds a 1-second delay between requests (polite scraping) |

---

## Concepts demonstrated

- Sending HTTP GET requests
- Parsing HTML with CSS class selectors
- Extracting text and attributes from tags
- Handling multi-page navigation
- Saving structured data to CSV
- Basic data filtering with pandas

---

## Sample output

```
Starting scraper — will scrape 3 page(s)

  Scraping page 1: https://books.toscrape.com/catalogue/page-1.html
  Found 20 books on this page
  Scraping page 2: ...
  ...

Done! Total books collected: 60

==================================================
  DATASET ANALYSIS
==================================================

  Total books scraped   : 60
  Average price (£)     : 35.07
  Cheapest book (£)     : 10.00
  Most expensive (£)    : 59.69
  Average star rating   : 3.0

  Books by rating:
    5★  ████████████ (12)
    4★  ██████████ (10)
    3★  ████████████████ (16)
    2★  ████████████ (12)
    1★  ██████████ (10)
```

---

## References

- https://books.toscrape.com — practice scraping site
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/ — BeautifulSoup docs
- https://requests.readthedocs.io — requests docs
- https://pandas.pydata.org/docs/ — pandas docs
