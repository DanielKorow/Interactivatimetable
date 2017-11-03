import calendar, datetime
from datetime import datetime

today = datetime.today()
number_of_month = today.strftime("%m")
year = today.strftime("%Y")
cal = calendar.Calendar(firstweekday=0)
weekCalendar = cal.monthdatescalendar(year=int(year), month=int(number_of_month))
for i in weekCalendar:
    print("Новая неделя")
    for a in i:
        print(a)
