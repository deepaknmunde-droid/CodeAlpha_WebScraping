
#  save_data.py
#  Runs the scraper, saves data to CSV, and does basic analysis

import pandas as pd
from scraper import scrape_books   # import our scraper function


def save_to_csv(books, filename="books_dataset.csv"):
    """Saves the list of books to a CSV file using pandas."""
    df = pd.DataFrame(books)
    df.to_csv(filename, index=False)
    print(f" Saved {len(df)} books to '{filename}'")
    return df


def analyse(df):
    """Prints some basic stats about the dataset."""
    print("\n" + "="*50)
    print("  DATASET ANALYSIS")
    print("="*50)

    print(f"\n  Total books scraped   : {len(df)}")
    print(f"  Average price (£)     : {df['price_gbp'].mean():.2f}")
    print(f"  Cheapest book (£)     : {df['price_gbp'].min():.2f}")
    print(f"  Most expensive (£)    : {df['price_gbp'].max():.2f}")
    print(f"  Average star rating   : {df['rating'].mean():.1f}")

    print("\n  Books by rating:")
    rating_counts = df['rating'].value_counts().sort_index(ascending=False)
    for stars, count in rating_counts.items():
        bar = "█" * count
        print(f"    {stars}★  {bar} ({count})")

    print("\n  Top 5 most expensive books:")
    top5 = df.nlargest(5, "price_gbp")[["title", "price_gbp", "rating"]]
    for _, row in top5.iterrows():
        print(f"    £{row['price_gbp']:.2f}  |  {row['rating']}★  |  {row['title'][:45]}")

    print("\n  Top 5 highest rated books (cheapest first if tied):")
    top_rated = df.sort_values(
        by=["rating", "price_gbp"], ascending=[False, True]
    ).head(5)[["title", "rating", "price_gbp"]]
    for _, row in top_rated.iterrows():
        print(f"    {row['rating']}★  |  £{row['price_gbp']:.2f}  |  {row['title'][:45]}")

    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    # 1. Scrape the data
    books = scrape_books(num_pages=3)

    # 2. Save to CSV
    df = save_to_csv(books)

    # 3. Analyse
    analyse(df)
