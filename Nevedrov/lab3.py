from math import pi, e, tan, atan, log, exp, ceil
from timeit import timeit, Timer
from time import time, mktime, strptime


def cout(a, b):
    print(str(a)+' '+'='+' '+str(b))


def cout2(a, b, c):
    if c == 0:
        print(str(a) + ':' + ' ' + str(b))
    else:
        print(str(a) + ':' + ' ' + str(b) + ' ' + 'and' + ' ' + str(c))


def time_input():
    m = input('Minutes:')
    h = input('Hours:')
    if m.isdigit() == 1 and h.isdigit() == 1:
        m = int(m)
        h = int(h)
        if m < 60 and h < 24:
            cout2('Time', f'{h}:{m}', 0)
        else:
            print('Invalid time')
            time_input()
    else:
        print('Invalid time')
        time_input()

def data_input():
    dd = input('Day:')
    mm = input('Month:')
    yy = input('Year:')
    try:
        valid_date = strptime(f'{mm}/{dd}/{yy}', '%m/%d/%Y')
        cout2('Date', f'{dd}.{mm}.{yy}', 0)
    except ValueError:
        print('Invalid date')
        data_input()


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
time_input()
data_input()
# 2
x = float(input('Print  x:'))
y = float(input('Print  y:'))
ctg = 1/tan(x+y)
cout('ctg(x+y)', '{:.2e}'.format(ctg))
cout('x+y/(x^2+y^2+1)', (x+y)/(x**2+y**2+1))
cout('x+y/(x^2+y^2+1)', '{:.3e}'.format((x+y)/(x**2+y**2+1)))
# 3
x2 = float(input('Print x:'))
cout('arcctg(x)', '{:.4f}'.format((acot(x2))))
# 4
cout('exp(ln(10.001/9.001)^345*exp(ln(13.001/11.001)^249/9.001^10/11.001^20', exp(log(10.001/9.001, e))**345*exp(log(13.001/11.001, e))**249/9.001**10/11.001**20)
# 5
enrollment_date = (2020, 9, 6, 0, 0, 0, 0, 0, 0)                                     # дата зачисления
end_date = (2025, 9, 6, 0, 0, 0, 0, 0, 0)                                            # дата выпуска
current_time_interval = time()
past_time_interval = current_time_interval - mktime(enrollment_date)
future_time_interval = mktime(end_date) - current_time_interval
cout2('Seconds remains', past_time_interval, future_time_interval)                    # секунды
cout2('Minutes remains', minutes(past_time_interval), minutes(future_time_interval))  # минуты
cout2('Days remains', days(past_time_interval), days(future_time_interval))           # дни
cout2('Weeks remains', weeks(past_time_interval), weeks(future_time_interval))        # недели
# 6
t1 = Timer('exp(log(10.001/9.001, e))**345*exp(log(13.001/11.001, e))**249/9.001**10/11.001**20', "from math import exp, log, e")
t2 = Timer('exp(log((10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20))', "from math import exp, log, e")
t3 = Timer('acos(cos(((10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20)))', "from math import cos, acos")
cout('exp(ln(10.001/9.001))^345*exp(ln(13.001/11.001))^249/9.001^10/11.001^20 execution speed ', t1.timeit())
cout('exp(ln((10.001/9.001)^345*(13.001/11.001)^249/9.001^10/11.001^20)) execution speed', t2.timeit())
cout('arccos(cos(((10.001/9.001)^345*(13.001/11.001)^249/9.001^10/11.001^20))) execution speed', t3.timeit())
cout('(10.001/9.001)^345*(13.001/11.001)^249/9.001^10/11.001^20 execution speed', timeit('(10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20'))
