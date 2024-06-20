import requests
from bs4 import BeautifulSoup
import csv
import re


def scrape_books_to_csv(url, csv_file):
    """
    Scrapes book details from a website and saves them to a CSV file.

    Args:
        url (str): The URL of the website to scrape.
        csv_file (str): The path to the output CSV file.
    """
    # Send an HTTP request to the URL and get the response
    response = requests.get(url)
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all book entries in the HTML
    books = soup.find_all('article', class_='product_pod')

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the header row to the CSV file
        writer.writerow(['Title', 'Price', 'Availability'])

        # Iterate over each book entry
        for book in books:
            # Extract the title, price, and availability of each book
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()
            # Write the book data to the CSV file
            writer.writerow([title, price, availability])


def clean_price(price):
    """
    Removes all non-numeric characters except for the decimal point from a price string.

    Args:
        price (str): The price string to clean.

    Returns:
        str: The cleaned price string.
    """
    # Remove all non-numeric characters except for the decimal point
    return re.sub(r'[^\d.]', '', price)


def analyze_book_prices(csv_file):
    """
    Calculates the average price of books from a CSV file containing book details.

    Args:
        csv_file (str): The path to the input CSV file.

    Returns:
        float: The average price of the books.
    """
    total_price = 0.0
    book_count = 0

    # Open the CSV file for reading
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        # Iterate over each row in the CSV file
        for row in reader:
            # Clean and convert the price to a float
            price = clean_price(row['Price'])
            try:
                price = float(price)
                total_price += price
                book_count += 1
            except ValueError:
                # Handle the case where conversion fails
                print(f"Could not convert price to float: {row['Price']}")

    # Calculate the average price of the books
    average_price = total_price / book_count if book_count else 0
    return average_price


# Example usage:
url = 'http://books.toscrape.com/'  # URL of the website to scrape
csv_file = 'books.csv'  # Path to the output CSV file
scrape_books_to_csv(url, csv_file)
average_price = analyze_book_prices(csv_file)
print(f'Average book price: ${average_price:.2f}')  # Print the average book price