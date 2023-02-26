import datetime


def clean_date(date_str):
    try:
        split_date = date_str.split('/')
        return_date = datetime.date(
            int(split_date[2]), int(split_date[0]), int(split_date[1]))
        if datetime.datetime.combine(return_date, datetime.time.min) > datetime.datetime.now():
            return
    except (ValueError, IndexError):
        return
    else:
        return return_date
