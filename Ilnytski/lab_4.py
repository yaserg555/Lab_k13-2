import math

def welcome(n, s):
    print(f'Вітаю, {n} {s}')


name = input("Ім'я: ")
surname = input("Прізвище: ")
welcome(name, surname)

x, y, z = int(input()), int(input()), int(input())
if(x == y == z):
    print("Yes")
else:
    print("No")

e = 10e-10
r1, r2 = float(input()), float(input())

if (abs(r1 - r2) < e):
    print("Equal")
else:
    print("Not equal")

print("Прямі")

a1, b1, c1 = int(input()), int(input()), int(input())

a2, b2, c2 = int(input()), int(input()), int(input())

if(a1 * b2 == a2 * b1):
    if(c1 == c2):
        print("Накладаються")
    else:
        print("Колінеарні")
else:
    print("Перетинаються")
