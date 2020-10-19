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

x = input()
y = input()
z = input()
if x + y == z or x + z == y or y + z == x:
    print('Yes')

x = int(input())
y = int(input())
z = int(input())
t = int(input())
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and t % 2 == 0:
    print((max(x, y, z, t)))
elif y % 2 == 0 and z % 2 == 0 and t % 2 == 0:
    print((max(y, z, t)))
elif x % 2 == 0 and z % 2 == 0 and t % 2 == 0:
    print((max(x, z, t)))
elif z % 2 == 0 and t % 2 == 0:
    print((max(z, t)))
elif y % 2 == 0 and t % 2 == 0:
    print((max(y, t)))
elif x % 2 == 0 and y % 2 == 0:
    print((max(x, y)))
elif x % 2 == 0 and z % 2 == 0:
    print((max(x, z)))
elif x % 2 == 0 and t % 2 == 0:
    print((max(x, t)))
elif x % 2 == 0:
    print(x)
elif y % 2 == 0:
    print(y)
elif z % 2 == 0:
    print(z)
elif t % 2 == 0:
    print(t)
else:
    print('not found')


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

