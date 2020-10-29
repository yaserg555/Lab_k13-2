# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def welcome(n, s):
    print(f'Привет, {n} {s}')


name = input("Імя: ")
surname = input("Фамилия: ")
welcome(name, surname)


def func(x1, y1, z1):
    return x1 != y1 and x1 != z1


a = input('x = ')
b = input('y = ')
c = input('z = ')
print(f'Результат: {func(a, b, c)}')


def func1(x, y, epsilon=(10 ** -10)):
    return abs(x - y) <= epsilon


q = float(input('первое число = '))
p = float(input('второе число = '))
print(f'два числа равны: {func1(q, p)}')


def func2(a1, b1, a2, b2):
    return a1 * b2 == a2 * b1


x = float(input('a1 = '))
y = float(input('b1 = '))
z = float(input('a2 = '))
t = float(input('b2 = '))

print(f'результат колинеарности: {func2(x, y, z, t)}')
