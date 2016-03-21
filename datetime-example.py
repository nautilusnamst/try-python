import datetime

today = datetime.date.today()
print(today)
print(today.strftime("%d.%m.%Y"))
print(today.strftime("%Y-%m-%d"))

now = datetime.datetime.now()
print(now)
print(now.strftime("%d.%m.%Y %I:%M %p"))
