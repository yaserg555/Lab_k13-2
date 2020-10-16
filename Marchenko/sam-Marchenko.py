a = input()
b = input()
c = input()
P = a + b + c
print(f'Периметр трикутника: {P}')

x = float(input())
y = float(input())
print(f'({x};{y})')

x = input()
y = input()
z = input()
if x + y == z or x + z == y or y + z == x:
    print('Yes')

x = input()
y = input()
z = input()
t = input()
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and t % 2 == 0:
    print((max(x, y, z, t)))
elif y % 2 == 0 and z % 2 == 0 and t % 2 == 0:
    print((max(y, z, t)))
elif x % 2 == 0 and z % 2 == 0 and t % 2 == 0:
    print((max(x, z, t)))
elif z % 2 == 0 and t % 2 == 0:
    print((max(z, t)))
else:
    print('not found')

k = int(input())
a = [range(10, 100)]
print(a[k])
