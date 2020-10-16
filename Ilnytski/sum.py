import math

a = float(input("Уведіть довжини стороти 1: "))
b = float(input("Уведіть довжини сторони 2: "))
c = float(input("Уведіть довжини сторони 3: "))
print(a + b + c)

x = float(input("Уведіть координату x точки: "))
y = float(input("Уведіть координату y точки: "))
print(f"[{x},{y}]")

#task 6

x = float(input())
y = float(input())

print(math.log(x + y) / math.log(89))

#task 7

a = float(input())
b = float(input())
c = float(input())

if (a + b == c or a + c == b or b + c == a):
    print("Yes")
else:
    print("No")

#task 8

a = [0,0,0,0]

for i in range(4):
    a[i] = float(input())

for i in range(3):
    for j in range(i+1, 4):
        if a[j] < a[i]:
            x = a[i]
            a[i] = a[j]
            a[j] = x
max = -1
for i in range(3, -1, -1):
    if (a[i] % 2 == 0):
        max = a[i]
        break
if (max == -1):
    print("No")
else:
    print(max)
#task 8
k = int(input())

start = 10
s = ''
while (len(s) < k):
    s += str(start)
    start = start + 1
print(s[k-1])
#task 9
sum = 0
a = 3
while(a<=111):
    sum += math.cos(a / (a + 2))
    a += 2
print(str(sum))
#task 10 ready )

#task 11

a = []
n = int(input())

for i in range(n):
    x = int(input())
    a.append(x)
st = set(a)

if (len(st) != len(a)):
    print("No")
else:
    print("Yes")

#task 12
x = float(input())
y = float(input())

x1 = x
y1 = y

x2 = x
y2 = y

x3 = x
y3 = y

x = x + y
y = x - y
x = x - y

print(x, y)

temp = x1 + y1
x1 = temp - x1
y1 = temp - y1

print(x1, y1)

x,y = y,x

print(x1, y1)

x2 = x2*y2
y2 = x2 / y2
x2 = x2 / y2

print(x2, y2)

