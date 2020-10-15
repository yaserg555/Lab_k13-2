day = input("Виберіть число ")
month = input("Виберіть місяць ")
year = input("Виберіть рік ")
if day <= 0:
    print("Така дата не існує")
elif day > 31:
    print("Така дата не існує")
elif month <= 0:
    print("Така дата не існує")
elif month > 12:
    print("Така дата не існує")
else:
print(f"дата: {day}.{month}.{year}")


x = float(input("Введіть перше значення "))
y = float(input("Введіть друге значення "))
import math
from math import cos, sin, atan, pi
z = cos(x+y)/sin(x+y)
print("%.2f" % z)

a = float(input("Введіть значення "))
if a != 0:
    b = atan (1/a)
    print("%.4f" % b)
else:
    print("1.5708")
    
d = (exp(log(10.001/9.001) * 345) * exp(log(13.001/11.001) * 249)) / (exp(log(9.001) * 10) * exp(log(11.001) * 20))
print(d)

    
