# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


n = float(input(f"n:"))


def f(n):
    while n != 0:
        t = n % 10
        if t == 1:
            return True
        n = (n - t)/10
    return False


print(f"result: {f(n)}")


m = float(input(f"m:"))


def f2(m):
    f, f1 = 0, 1
    while m >= f:
        f1, f = f + f1, f1
    return f


print(f"result: {f2(m)}")

"""0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610"""
