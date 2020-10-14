from math import tan, pi, atan, log, exp
from datetime import datetime
from timeit import timeit


print('-1-')
day = str(input()).zfill(2)
month = str(input()).zfill(2)                                                                        # x, y = 1, 2; (x + y)/(x ** 2 + y ** 2 + 1) = 0.5
year = str(input())[-2:]
if int(year) % 4 != 0 and int(month) == 2 and int(day) == 29:
    print('Такої дати не існує')
elif int(month) == 2 and (int(day) == 30 or int(day) == 31):
    print('Такої дати не існує')
elif 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
    print(f'{day}.{month}.{year}')
else:
    print('Такої дати не існує')
print('-2-')
x = float(input())                                            
y = float(input())
z = 1 / tan(x + y)
print(f'ctg(x+y)={z:.2e}')
print('-3-')
x = float(input())
y = pi / 2 - atan(x)
print(f'arcctg(x)={y:.4f}')
print('-4-')
x = (exp(log(10.001/9.001) * 345) * exp(log(13.001/11.001) * 249)) / (exp(log(9.001) * 10) * exp(log(11.001) * 20))
print(f'(10.001^345*13.0001^249)/(9.001^355*11.001^269)={x}')
print('-5-')
now = datetime.now()
then = datetime(2020, 9, 21, 8, 40, 0)
future = datetime(2024, 6, 30, 12, 0)
dif1 = now - then
dif2 = future - now
print('Минуло:')
print('тижні: ' + str(dif1.days // 7))
print('дні: ' + str(dif1.days))
print('години: ' + str(dif1.days * 24 + dif1.seconds // 3600))
print('хвилини: ' + str(dif1.days * 1440 + dif1.seconds // 60))
print('секунди: ' + str(dif1.days * 86400 + dif1.seconds))
print('Залишилось:')
print('тижні: ' + str(dif2.days // 7))
print('дні: ' + str(dif2.days))
print('години: ' + str(dif2.days * 24 + dif2.seconds // 3600))
print('хвилини: ' + str(dif2.days * 1440 + dif2.seconds // 60))
print('секунди: ' + str(dif2.days * 86400 + dif2.seconds))

def func(x):
    print(f'execution time of {x}')


a = '(((10.001/9.001)**345)*((13.001/11.001)**249))/((9.001**10)*(11.001**20))'
b = '(Decimal(10.001) ** 345 * Decimal(13.001) ** 249) / (Decimal(9.001) ** 355 * Decimal(11.001) ** 269)'
c = '(exp(log(10.001/9.001) * 345) * exp(log(13.001/11.001) * 249)) / (exp(log(9.001) * 10) * exp(log(11.001)* 20))'
print(timeit('func(a)', setup='from __main__ import func, a', number=1))
print(timeit('func(b)', setup='from __main__ import func, b', number=1))
print(timeit('func(c)', setup='from __main__ import func, c', number=1))
