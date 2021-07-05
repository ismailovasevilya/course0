import datetime
import sys

def getdate():
    year = int(input)
    month = int(input)
    day = int(input)
    date1 = datetime.date(year, month, day)
    return date1

def main():
    date = getdate()
    time_add = datetime.timedelta(int(input()))
    res_date = date + time_add
    print(res_date.year, res_date.month, res_date.day)
