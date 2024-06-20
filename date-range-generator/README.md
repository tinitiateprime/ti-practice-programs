# Date Manipulation - Date Range Generator
* Write a function that takes a start date and an end date as inputs and generates a list of all dates within that range, inclusive.

# Date Range Generator
This project consists of a Python function that generates a list of dates within a given date range. The dates are provided as strings in the format 'YYYY-MM-DD', and the function returns a list of dates within the specified range.

## Files

- `date_range_generator.py`: Contains the main code for generating the date range.

## Functions
### `generate_date_range(start_date, end_date)`
Generates a list of dates within a given date range.

#### Arguments

- `start_date` (str): The start date in the format 'YYYY-MM-DD'.
- `end_date` (str): The end date in the format 'YYYY-MM-DD'.

#### Returns

- `list`: A list of date strings within the specified range.

#### Description

- Parses the input date strings to datetime objects using the `strptime()` method.
- Calculates the difference between the start and end dates.
- Uses a list comprehension to generate the list of dates within the range.
- Converts each date back to a string in the 'YYYY-MM-DD' format using the `strftime()` method.
- Returns the resulting list of dates.

## Usage

- Import the `generate_date_range` function from the `date_range_generator.py` file.
- Call the function with the desired start and end dates.