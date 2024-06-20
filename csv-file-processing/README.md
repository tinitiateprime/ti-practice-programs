# Data Handling - CSV File Processing
* Write a function to read a CSV file, filter out rows based on a certain condition, and write the filtered data to a new CSV file. For this example, filter out rows where the value in the 'age' column is less than 30.

# CSV Filter Script
This project consists of a Python script that filters rows from a CSV file based on a specified column and threshold value. The filtered rows are then written to an output CSV file.

## Files

- `filter_csv.py`: Contains the main code for filtering rows in a CSV file.
- `input.csv`: The input CSV file containing data to be filtered (this file should be provided by the user).
- `output.csv`: The output CSV file containing filtered data.

## Functions
### `filter_csv(input_file, output_file, column_name, threshold)`
Filters rows from a CSV file based on a specified column and threshold value.

#### Arguments

- `input_file` (str): The path to the input CSV file.
- `output_file` (str): The path to the output CSV file.
- `column_name` (str): The name of the column to filter on.
- `threshold` (int): The threshold value for filtering.

#### Description

- Opens the input CSV file for reading and the output CSV file for writing.
- Creates a CSV reader object to read the input file.
- Creates a CSV writer object to write to the output file.
- Writes the header row to the output file.
- Iterates over each row in the input file.
- Checks if the value in the specified column is greater than or equal to the threshold.
- Writes the row to the output file if it meets the condition.

## Usage

- Ensure you have a CSV file named `input.csv` in the same directory as the script, or provide the correct path to the input file.
- Modify the script to set the `input_file`, `output_file`, `column_name`, and `threshold` values as needed.
- Run the script:
```bash
python filter_csv.py
```