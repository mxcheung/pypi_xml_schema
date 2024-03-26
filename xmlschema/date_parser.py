from datetime import datetime

def parse_date(date_str):
    # Define possible date formats
    date_formats = ['%Y%m%d', '%y%m%d', '%Y%m', '%y%m']

    # Try parsing with each format
    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.date()
        except ValueError:
            pass

    # If none of the formats match
    raise ValueError("Invalid date format")

# Example usage
date_string = "220327"  # This can be 6 or 8 digits
parsed_date = parse_date(date_string)
print(parsed_date)
