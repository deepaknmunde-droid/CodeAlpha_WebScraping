
#  filter_data.py
#  Load the saved CSV and filter/search your dataset
#  Run save_data.py first to generate books_dataset.csv


import pandas as pd

# Load the CSV we created earlier
df = pd.read_csv("books_dataset.csv")
print(f"Loaded {len(df)} books from books_dataset.csv\n")


# FILTER 1: Books under a certain price
def books_under_price(max_price):
    result = df[df["price_gbp"] < max_price]
    print(f"Books under £{max_price}:")
    print(result[["title", "price_gbp", "rating"]].to_string(index=False))
    print(f"\nTotal: {len(result)} books\n")

# FILTER 2: Books with a specific star rating
def books_by_rating(stars):
    result = df[df["rating"] == stars]
    print(f"Books with {stars}-star rating:")
    print(result[["title", "price_gbp", "rating"]].to_string(index=False))
    print(f"\nTotal: {len(result)} books\n")

# FILTER 3: Search books by keyword in title
def search_by_title(keyword):
    result = df[df["title"].str.contains(keyword, case=False, na=False)]
    print(f"Books with '{keyword}' in the title:")
    if result.empty:
        print("  No results found.")
    else:
        print(result[["title", "price_gbp", "rating"]].to_string(index=False))
    print(f"\nTotal: {len(result)} books\n")


# Try them out
if __name__ == "__main__":
    print("="*50)

    books_under_price(10.00)

    books_by_rating(5)

    search_by_title("the")
