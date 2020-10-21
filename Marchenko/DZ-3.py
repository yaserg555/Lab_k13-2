from decimal import Decimal


     # 1
def func(a, b):
    return f'Good morning, {a} {b}!'


print('What is your name?')
v = input()
print('What is your surname?')
m = input()
print(func(v, m))


def func2(x, y, z):
    return x != y and x != z and y != z

     # 2
k = input('x = ')
s = input('y = ')
t = input('z = ')
print(f'Змінні попарно різні: {func2(k, s, t)}')

     # 3
def func3(a: Decimal, b: Decimal):
    return a == b


g = Decimal(input('перше дійсне значення = '))
h = Decimal(input('друге дійсне значення = '))
print(f'Два дійсних значення рівні: {func3(g, h)}')

      #4
def func1(a, b, c):
    return float(a) == float(b) == float(c)


n = [float(i) for i in input('a, b, c для першого рівняння: ').split(', ')]     # a,b,c для першого рівняння
p = [float(i) for i in input('a, b, c для другого рівняння: ').split(', ')]     # a,b,c для другого рівняння
k1 = n[0] / p[0]
k2 = n[1] / p[1]
k3 = n[2] / p[2]
print(f'Колінеарні: {func1(k1, k2, k3)}')
