def number(x: str):
    for i in range(len(x)):
        if 48 > ord(x[i]) or ord(x[i]) > 57:
            print('ХАХА розумник, лише числа, зрозумiв?')
            return False
    return True


print('я вообще своего рода путешественик во времени, по-этому скажите какой год?')
y = input()
while not number(y):
    y = input()
y=int(y)
if y == 400 or (y % 100 != 0 and y % 4 == 0):
    visokos = True
else:
    visokos = False

mounth = [31, 28 + visokos, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print('a номер месяца?')
m = input()
while not number(m):
    m = input()
while int(m)>12 or int(m) == 0 :
    print('ну у кого ты видел больше 12 месяцев а?')
    m=input()
    while not number(m):
        m = input()

print('Молодой человек, а не подскажите ли какой сегодня день тогда?')
d = input()
while not number(d):
    d = input()
while int(d) > mounth[int(m) - 1] or int(d)==0:
    print(
        'так ты либо вводишь мне существующий день месяца или перезапускаешь программу и выбираешь другой год или месяц')
    d = input()
    while not number(d):
        d = input()

if len(d) == 1:
    d = "0" + d
if len(m) == 1:
    m = "0" + m
print(f'{d}.{m}.{y}')



from math import tan, pi, atan
x=float(input())
y=float(input())
print(f'{1/tan(x+y):.2f}')
print(f'{1/tan(x+y):.2e}')

x=float(input())
print(f'{pi/2-atan(x):.4f}')

from math import exp, log
print(exp(log(10.001/9.001)*345)*exp(log(13.001/11.001)*249)/(exp(log(9.001)* 10) * exp(log(11.001) * 20)))
#2997.246914575209

(10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20 == exp(log(10.001/9.001)*345)*exp(log(13.001/11.001)*249)/(exp(log(9.001)* 10) * exp(log(11.001)* 20))
#false 2997.246914575195 против 2997.246914575209
