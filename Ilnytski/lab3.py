from datetime import datetime
from math import exp, log, e
import math


correct_data = False
while (not correct_data):
    try:
        date = input("Day: ")
        month = input("Month: ")
        year = input("Year: ")
        if (len(date) == 1):
            date = "0" + date
        if (len(month) == 1):
            month = "0" + month
        if (len(year) == 1):
            year = "0" + year
        datetime_str = date + "-" + month + "-" + year
        date_time_obj = datetime.strptime(datetime_str, '%d-%m-%y')
        print(f"{date}/{month}/{year}")
        correct_data = True
    except:
        print("Wrong date. Try again )")


x = float(input("Enter x: "))
y = float(input("Enter y: "))
if (x + y == 0):
    print("Infinity")
else:
    res = 1 / math.tan(x + y)
    print(f'{res:.2e}')

x1 = float(input("Enter x1: "))

res1 = -math.atan(x1) + math.pi / 2;
print(f'{res1:.4f}')

print(exp(345*log(10.001 / 9.001) - 10*log(9.001) + 249*log(13.001 / 11.001) - 20*log(11.001)))

def expression(x, y):
    return (x + y) / (x**2 + y**2 + 1)
print(f"{expression(2, 3):.3f}")
print(f"{expression(1, 1):.3f}")


correct_time = False
while (not correct_time):
    try:
        hour = input("Enter hour: ")
        minute = input("Enter minutes: ")
        hh = int(hour)
        mm = int(minute)
        if(len(hour) > 2 or len(minute) > 2 or mm >= 60 or mm < 0 or hh < 0 or hh > 23):
            raise Exception("Unexisting time")
        if (len(hour) == 1):
            hour = "0" + hour
        if (len(minute) == 1):
            minute = "0" + minute
        print(hour + ":" + minute)
        correct_time = True
    except:
        print("Wrong time. Try again )")

print(e, math.tan(math.pi / 2))
