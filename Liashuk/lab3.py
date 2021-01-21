import datetime
from math import cos,sin,e,tan,exp,log
#№1
x=1
y=2.5
y=x
x=3
x+=x
print(f"""x={x}; y={y}""")


#№2
x,y=[1,2]
x,y,y,x=[y,x,3,y]
print(f"""x={x}; y={y}""")


#№3 and 4
print(f"""x^2+y^2 ={(x+y)/(x**2+y**2)}
x^2+y^2 ={round((x+y)/(x**2+y**2),3)}""")


# №5
def Time():
    try:
        hour=int(input("Скільки годин? "))
        minute=int(input("Скільки хвилин? "))
        a=datetime.time(hour,minute)
        print(f'{a.hour}:{a.minute}')
    except ValueError as e:
        print(e)
Time()

# №6
print("tg(34) =", tan(34))
print("e =", e)

# №7
def Date():
    try:
        day=int(input("Який день? "))
        month=int(input("Який місяць? "))
        year=int(input("Який рік? "))
        a=datetime.date(year,month,day)
        print(f'{a.day}.{a.month}.{a.year}')
    except ValueError as e:
        print(e)
Date()

# №8
def ctg():
    try:
        x=int(input("Введіте 'х' для обчислення ctg(x+y):  "))
        y=int(input("Введіте 'y' для обчислення ctg(x+y):  "))
        print("ctg(x + y) =",'{:.2e}'.format(cos(x+y)/sin(x+y)))
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
ctg()
