import calendar, datetime
from datetime import datetime


def week_func():
    today = datetime.today()
    number_of_month = today.strftime("%m")
    year = today.strftime("%Y")
    cal = calendar.Calendar(firstweekday=0)
    weekcalendar = cal.monthdatescalendar(year=int(year), month=int(number_of_month))
    week = []
    for i in weekcalendar:
        for a in i:
            if a == today.date():
                week = i
    return week


print(week_func())
