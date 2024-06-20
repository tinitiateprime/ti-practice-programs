# String Manipulation - Season Identification
* Write a function that takes a date string as input and returns the corresponding season (Spring, Summer, Autumn, Winter) in the Northern Hemisphere. The dates for the seasons are:
    * Spring: March 21 to June 20
    * Summer: June 21 to September 22
    * Autumn: September 23 to December 20
    * Winter: December 21 to March 20

# Season Detector
This project provides a function to determine the season based on a given date. The date is provided as a string in the format 'YYYY-MM-DD', and the function returns the corresponding season name.

## Files

- `season_detector.py`: Contains the main code for the season detection function.

## Functions
### `get_season(date_str)`
Determines the season based on the input date string.

#### Arguments

- `date_str` (str): The date string in the format 'YYYY-MM-DD'.

#### Returns

- `str`: The corresponding season name or 'Invalid date' if the date is invalid.

#### Description

- Parses the date string to a `datetime` object.
- Defines the start and end dates for each season.
- Iterates over the seasons and checks if the input date falls within the date range of each season.
- Returns the corresponding season name if a match is found.
- Returns 'Invalid date' if no match is found.

## Usage

- Import the `get_season` function from the `season_detector.py` file.
- Call the function with a date string in the format 'YYYY-MM-DD'.