def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example usage
yyyy = int(input())
print(f"{yyyy} is a leap year: {is_leap_year(yyyy)}")
