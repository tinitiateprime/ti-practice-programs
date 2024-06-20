import csv

def filter_csv(input_file, output_file, column_name, threshold):
    """
    Filter rows from a CSV file based on a specified column and threshold value.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        column_name (str): Name of the column to filter on.
        threshold (int): Threshold value for filtering.
    """
    # Open the input CSV file for reading and output CSV file for writing
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        # Create a CSV reader object to read the input file
        reader = csv.DictReader(infile)
        # Create a CSV writer object to write to the output file
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        # Write the header row to the output file
        writer.writeheader()

        # Iterate over each row in the input file
        for row in reader:
            # Check if the value in the specified column is greater than or equal to the threshold
            if int(row[column_name]) >= threshold:
                # Write the row to the output file if it meets the condition
                writer.writerow(row)


# Example usage:
# Path to the input CSV file
input_file = 'input.csv'
# Path to the output CSV file
output_file = 'output.csv'
# Filter rows where the 'age' column is >= 30
filter_csv(input_file, output_file, 'age', 30)