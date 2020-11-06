# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

a = float(input("a:"))
b = float(input("b:"))

def f(a, b):
    if (a >= b):
        print("incorrect value")
    else:
        c = random.randint(a, b)
        return c
    
print(f"{f(a, b)}")
