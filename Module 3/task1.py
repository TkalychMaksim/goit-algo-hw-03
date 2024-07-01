from datetime import datetime
def get_days_from_today(date):
    try:
        # Convert date string to datetime object
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Getting current date
        today = datetime.today().date()
        # Calculating delta
        delta = today - input_date
        # Returning delta in days
        return delta.days
    except ValueError:
        # Incorrect date format processing
        return " Incorrect date format. Enter date in format 'YYYY-MM-DD'."


