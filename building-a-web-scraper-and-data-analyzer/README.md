# Building a Web Scraper and Data Analyzer
* Write a Python program to scrape data from a website, store the data in a CSV file, and perform some analysis on the data. For this example, scrape book information (title, price, and availability) from a bookstore website, save it to a CSV file, and then calculate the average price of the books.

# Book Scraper and Analyzer
This project consists of a Python script that scrapes book details from a website and saves them to a CSV file. Additionally, it provides a function to calculate the average price of the books from the CSV file. The project uses the `requests` library to fetch web pages and `BeautifulSoup` from the `bs4` library to parse HTML content.

## Files

- `book_scraper.py`: Contains the main code for scraping book details and analyzing book prices.
- `books.csv`: The output CSV file containing scraped book details.

## Functions
### `scrape_books_to_csv(url, csv_file)`
Scrapes book details from a given website and saves them to a CSV file.

#### Arguments

- `url` (str): The URL of the website to scrape.
- `csv_file` (str): The path to the output CSV file.

#### Description

- Sends an HTTP GET request to the provided URL.
- Parses the HTML content using BeautifulSoup.
- Finds all book entries in the HTML.
- Writes the title, price, and availability of each book to the CSV file.

### `clean_price(price)`
Removes all non-numeric characters except for the decimal point from a price string.

#### Arguments

- `price` (str): The price string to clean.

#### Returns

- `str`: The cleaned price string.

### `analyze_book_prices(csv_file)`
Calculates the average price of books from a CSV file containing book details.

#### Arguments

- `csv_file` (str): The path to the input CSV file.

#### Returns

- `float`: The average price of the books.

#### Description

- Reads the CSV file.
- Cleans and converts the price of each book to a float.
- Calculates the total price and the number of books.
- Computes the average price.

## Usage

- Ensure you have the required libraries installed:

```bash
pip install requests beautifulsoup4

```
- Run the script:

```bash
python book_scraper.py

```
- The script will scrape book details from the specified URL and save them to `books.csv`. It will also calculate and print the average book price.