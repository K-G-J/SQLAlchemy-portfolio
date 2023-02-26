import datetime


def clean_date(date_str):
    try:
        return_date = datetime.datetime.strptime(date_str,  '%Y-%m')
        if datetime.datetime.combine(return_date, datetime.time.min) > datetime.datetime.now():
            return
    except (ValueError, IndexError):
        return
    else:
        return return_date
