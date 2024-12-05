from datetime import datetime, timedelta
from datetime import time

# print(datetime.today())
# print(datetime.now())
# today = datetime.today()
# print(today.strftime("%d.%m.%Y"))
# print(today.strftime("%d/%m/%y"))
# print(today.strftime("%d %B %Y (%A)"))
# print(today.strftime("%d.%m.%Y %H:%M"))
# print(type(today.strftime("%d.%m.%Y %H:%M")))

# print(datetime.today().year)
# print(datetime.today().month)
# print(datetime.today().day)
# print(datetime.today().hour)
# print(datetime.today().minute)
# print(datetime.today().second)
# print(datetime.today().microsecond)

# current_time = time(16, 25, 30)
# print(current_time.hour)
#
# birthday = "2024-12-31"
# birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
# print(birthday_date)

today = datetime.now()
deadline = 15
deadline = timedelta(days=deadline)
print(today+deadline)

