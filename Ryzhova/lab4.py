import math

def welcome(a, b):
    print(f'Вітаю, {a} {b}')


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

k1, l1, n1 = int(input()), int(input()), int(input())

k2, l2, n2 = int(input()), int(input()), int(input())

if(k1 * l2 == n2 * l1):
    if(n1 == n2):
        print("Прямі накладаються")
    else:
        print("Прямі колінеарні")
else:
    print("Прямі перетинаються")
