import math
print('For degrees')
print('')
x = float(input('Write x:'))
y = float(input('Write y:'))
d = math.radians(x+y)
a = (math.tan(d))**(-1)
print("ctg = " + str(round(a, 2)))
print('')
x = float(input('Write x:'))
f = math.atan(x)
k = math.degrees(math.pi/2-f)
print("arcctg = " + str(round(k, 4)))
print('')
dd = input('Enter date of your birth:')
mm = input('Enter mounth of your birth:')
yy = input('Enter year of your birth:')
print(f"{dd}.{mm}.{yy}")
print("")
print((exp(log(10.001/9.001)*345)/exp(log(9.001)*10))*(exp(log(13.001/11.001)*249)/exp(log(11.001)*20)))
