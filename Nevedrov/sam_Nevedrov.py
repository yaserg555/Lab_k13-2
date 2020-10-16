print('Алексей')
#3
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
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
