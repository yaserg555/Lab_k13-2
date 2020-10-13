from math import pi, e, tan, atan, log, exp, ceil
from timeit import timeit, Timer
from time import time, mktime


def cout(a, b):
    print(str(a)+' '+'='+' '+str(b))


def cout2(a, b, c):
    print(str(a)+':'+' '+str(b)+' '+'and'+' '+str(c))


def acot(a):
    b = pi / 2 - atan(a)
    return b


def minutes(a):
    b = ceil(a/60)
    return b


def days(a):
    b = ceil(a/60/60/24)
    return b


def weeks(a):
    b = ceil(a/60/60/24/7)
    return b


print('''                                        
Виконавець: Нєвєдров
            Олексій
            Дмитрович
     Група: К-13(2)
     ''')
# 1
dd = input('Day:')
mm = input('Month:')
yy = input('Year:')
cout('dd.mm.yy', f'{dd}.{mm}.{yy}')
# 2
x = float(input('Print  x:'))
y = float(input('Print  y:'))
ctg = 1/tan(x+y)
cout('ctg(x+y)', '{:.2e}'.format(ctg))
# 3
x2 = float(input('Print x:'))
cout('arcctg(x)', '{:.4f}'.format((acot(x2))))
# 4
cout('exp(log(10.001/9.001, e))**345*exp(log(13.001/11.001, e))**249/9.001**10/11.001**20', exp(log(10.001/9.001, e))**345*exp(log(13.001/11.001, e))**249/9.001**10/11.001**20)
# 5
enrollment_date = (2020, 9, 6, 0, 0, 0, 0, 0, 0)                             # дата зачисления
end_date = (2025, 9, 6, 0, 0, 0, 0, 0, 0)                                    # дата выпуска
current_time_interval = time()
past_time_interval = current_time_interval - mktime(enrollment_date)
future_time_interval = mktime(end_date) - current_time_interval
cout2('seconds', past_time_interval, future_time_interval)                    # секунды
cout2('minutes', minutes(past_time_interval), minutes(future_time_interval))  # минуты
cout2('days', days(past_time_interval), days(future_time_interval))           # дни
cout2('weeks', weeks(past_time_interval), weeks(future_time_interval))        # недели
# 6
t1 = Timer('exp(log(10.001/9.001, e))**345*exp(log(13.001/11.001, e))**249/9.001**10/11.001**20', "from math import exp, log, e")
t2 = Timer('exp(log((10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20, e))', "from math import exp, log, e")
cout('exp(log(10.001/9.001, e))**345*exp(log(13.001/11.001, e))**249/9.001**10/11.001**20 execution speed ', t1.timeit())
cout('exp(log((10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20, e) execution speed', t2.timeit())
cout('(10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20 execution speed', timeit('(10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20'))
