# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


x = input(f"Напишите одну букву")
def f(x):
    bykva = ["A", "B", "C", "D", "E", "F"]
    return x in bykva


print(f"Лежит ли буква в шестнадцатеричной системе счисления? {f(x)}")


x = float(input(f"x:"))


def f(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    elif x == 0:
        return 0


print(f"res: {f(x)}")

a = float(input(f"a:"))
b = float(input(f"b:"))
c = float(input(f"c:"))

def f(a, b, c):
    k = float((b**2)-4*a*c)
    if k < 0:
        return -1
    elif k == 0:
        return -b/2*a, b/2*a
    elif k > 0:
        return float((-b+(math.sqrt(k))/(2*a))), float((-b-(math.sqrt(k))/(2*a)))

print(f"x1, x2 = {f(a, b, c)}")


a = float(input(f"Длинна= "))
b = float(input(f"Ширина = "))
c = float(input(f"Высота = "))
x = float(input(f"Длинна окна = "))
y = float(input(f"Ширина окна = "))


def check(a, b, c, x, y):
    return (x > a and x > c and y > a and y > c) or (x > b and x > a and y > b and y > a) or (x > b and x > c and y > b and y > c)
print(f"Пролазит? {check(a, b, c, x, y)}")
