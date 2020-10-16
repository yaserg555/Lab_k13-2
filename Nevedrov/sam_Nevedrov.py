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
a = int(input('A:'))
b = int(input('B:'))
c = int(input('C:'))
if a + b == c or b + c == a or a + c == b and a >= 0 and b >= 0 and c >= 0:
    print('yes')
else:
    print('no')
