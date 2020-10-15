# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from math import tan, pi, atan, log, exp, cos, sin
from decimal import Decimal

day = input("число: ")
month = input("місяць: ")
year = input("рік: ")
if int(day) > 31:
    print("помилка")
elif int(day) <= 0:
    print("помилка")
elif int(month) > 12:
    print("помилка")
elif int(month) <= 0:
    print("помилка")
elif int(month) == 2 and int(day) == 30 or int(day) == 31:
    print("помилка")
else:
    print(f"дата: {day}.{month}.{year}")

a = float(input("a:"))
b = float(input("b:"))
c = cos(a+b) / sin(a+b)
print(f"ctg(x+y)={c:.2e}")


x = float(input("x: "))
y = atan(1/x)
print(f"arcctg(x)={y:.4f}")

"x^y=Exp(ln(x)*y)"

d = (exp(log(10.001/9.001) * 345) * exp(log(13.001/11.001) * 249)) / (exp(log(9.001) * 10) * exp(log(11.001) * 20))
print(f"(10.001**345*13.0001**249)/(9.001**355*11.001**269)={d}")
