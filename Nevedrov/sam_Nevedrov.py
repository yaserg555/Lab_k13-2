print('Алексей')
#3
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
p = a+b+c
print(f'{p}')
#4
x = int(input('x:'))
y = int(input('y:'))
print(f'{x,y}')
#6
A = int(input('A:'))
B = int(input('B:'))
C = int(input('C:'))
if A + B == C or B + C == A or A + C == B and A >= 0 and B >= 0 and C >= 0:
    print('yes')
else:
    print('no')
#7
def check(a, b):
    if a > b:
        return a
    else:
        return b


def check2(a):
    if a % 2 == 1:
        return 0
    else:
        return a


a = int(input('A:'))
b = int(input('B:'))
c = int(input('C:'))
d = int(input('D:'))
if a%2 == 1 and b%2 == 1 and c%2==1 and d%2 == 1:
    print('not found')
else:
    print(check(check(check(check2(a), check2(b)), check2(c)), check2(d)))
#8
k = int(input('k:'))
if k % 2 == 0:
    print(f'{int((k/2)%10)}')
else:
    print(f'{k // 10 + 1}')
#9
from math import cos
c = 3
p = 0
while (c < 111):
    p = cos(Decimal((c/)c+2)) + p
    c = c + 2
print(f'{p}')
#11
sequence = [int(i) for i in input('Print your number sequence through space:').split()]
if len(sequence) == len(set(sequence)):
    print('Numbers in sequence are unique')
else:
    print('Numbers in sequence are not unique')
#12
while True:
    try:
        a = int(input('Print first number'))
        b = int(input('Print second number'))
        break
    except ValueError:
        print('numbers type couldn\'t be string')
# 1
a = a + b
b = a - b
a = a - b
print(f'a = {a}, b = {b}')
#2
a, b = b, a
print(f'a = {a}, b = {b}')
