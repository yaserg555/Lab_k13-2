print('Молодой человек, а не подскажите ли какой сегодня день?')
d=input()
print('a номер месяца?')
m=input()
print('я вообще своего рода путешественик во времени, по-этому скажите какой год?')
y=input()

if len(d) == 1:
    d="0"+d
if len(m) == 1:
    m="0"+m
print(f'{d}.{m}.{y}')

from math import tan, pi, atan
x=float(input())
y=float(input())
print(f'{1/tan(x+y):.2f}')
print(f'{1/tan(x+y):.2e}')

x=float(input())
print(f'{pi/2-atan(x):.4f}')
