from datetime import date, datetime


def get_date_input():
    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            inputted_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return inputted_date
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    # if object is not serializable save as a string
    return str(obj)
