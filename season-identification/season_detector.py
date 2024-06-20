from datetime import datetime

def get_season(date_str):
    """
    This function takes a date string in the format 'YYYY-MM-DD' and returns the corresponding season.

    Parameters:
    date_str (str): The date string in the format 'YYYY-MM-DD'.

    Returns:
    str: The corresponding season name or 'Invalid date' if the date is invalid.

    The function uses the datetime module to parse the date string and convert it to a datetime object.
    It then defines the start and end dates for each season.
    It iterates over the seasons and checks if the input date falls within the date range of each season.
    If a match is found, it returns the corresponding season name.
    If no match is found, it returns 'Invalid date'.
    """
    date = datetime.strptime(date_str, '%Y-%m-%d')  # Parse the date string
    year = date.year
    # Define the start and end dates for each season
    seasons = {
        "Spring": (datetime(year, 3, 21), datetime(year, 6, 20)),
        "Summer": (datetime(year, 6, 21), datetime(year, 9, 22)),
        "Autumn": (datetime(year, 9, 23), datetime(year, 12, 20)),
        "Winter": (datetime(year, 12, 21), datetime(year + 1, 3, 20))
    }
    
    for season, (start, end) in seasons.items():
        # Check if the date falls within the current season's date range
        if start <= date <= end or (start.year == date.year and end.year == date.year + 1 and date >= start):
            return season
    return "Invalid date"

# Example usage:
date_str = '2023-10-15'  # Input date
print(get_season(date_str))  # Print the corresponding season