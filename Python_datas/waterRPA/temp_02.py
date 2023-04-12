import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
year = year - 20
day = day -1
print(f'{year}-{month}-{day}')