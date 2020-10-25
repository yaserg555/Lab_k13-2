from math import cos, log


a = input()
b = input()
c = input()
P = a + b + c
print(f'Периметр трикутника: {P}')


x = float(input())
y = float(input())
print(f'({x};{y})')


x = float(input())
y = float(input())
z = log(x + y, 89)
print(z)


x = int(input())
y = int(input())
z = int(input())
if x + y == z or x + z == y or y + z == x:
    print('Yes')
else:
    print('No')


x = int(input())
y = int(input())
z = int(input())
t = int(input())
m = [x, y, z, t]
b = [k for k in m if k % 2 == 0]
if x % 2 == 1 and y % 2 == 1 and z % 2 == 1 and t % 2 == 1:
    print('not found')
else:
    print(max(b))


k = int(input())
a = int(k / 2 - 1 )
my_list = list(range(10,100))
b = my_list[a]
if k % 2 == 0:
    b %= 10
else:
    b //= 10
print(b)


a = 3
b = 0
while a < 111:
    a += 2
    b += cos(a / (a + 2))
print(b)


a = [int(i) for i in input().split()]
b = set(a)
if len(a) == len(b):
    print('Все числа в последовательности уникальные')
else:
    print('Числа в последовательности не уникальные')
    
    
a = int(input())
b = int(input())              # 1 спосіб
a = a + b
b = a - b
a = a - b
print(f'a = {a}, b = {b}')

a = int(input())
b = int(input())              # 2 спосіб
a, b = b, a
print(f'a = {a}, b = {b}')
