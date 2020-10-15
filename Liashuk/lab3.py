x=1
y=2.5
y=x
x=3
x+=x
print(f"""x={x}; y={y}""")
print("///////////////////////////////////////////\n")
x,y=[1,2]
x,y,y,x=[y,x,3,y]
print(f"""x={x}; y={y}""")
print("///////////////////////////////////////////\n")
print(f"""x^2+y^2 ={(x+y)/(x**2+y**2)}
x^2+y^2 ={round((x+y)/(x**2+y**2),3)}""")
print("///////////////////////////////////////////\n")
try:
    a=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    hour=input("Скільки годин: ")
    i=0
    while hour!=a[i]:
        i+=1
    minutes=int(input("Скільки хвилин: "))
    if minutes<10 and minutes>=0:
        print(f"""  {a[i]}:0{minutes}""")
    else:
        if minutes>=10 and minutes<60:
            print(f"""  {a[i]}:{minutes}""")
        else:
            print("Введіте правильні дані!!!")
except:
    print("Введіте правильні дані!!!")
print("///////////////////////////////////////////\n")
from math import e,atan
print(e)
print("tg(34) =", atan(34))
print("///////////////////////////////////////////\n")
try:
    dd=int(input("Day: "))
    mm=int(input("Month: "))
    yy=int(input("Year: "))
    if (mm==1) and (dd>31) or (mm==2) and (dd>28) or (mm==3) and (dd> 31) or (mm==4) and (dd>30) or (mm==5) and (dd>31) or (mm==6) and (dd>30) or (mm==7) and (dd>31) or (mm==8) and (dd>31)  or (mm==9)  and (dd>30)  or (mm==10) and (dd>31) or (mm==11) and (dd>30 ) or (mm==12) and (dd>31 ) or (dd<1):
        print("Ви ввели не правильні дані у \"Day\"")
    else:
        if (mm>12) or (mm<1):
            print("Ви ввели не правильні дані у \"Month\"")
        else:
            if yy<2020:
                print("Ви ввели не правильні дані у \"Year\"")
            else:
                print(f""" {dd}.{mm}.{yy} """)
except ValueError:
    print("Введіте число!!!")
print("///////////////////////////////////////\n")
try:
    x=int(input("Введіте 'х' для обчислення ctg(x+y):  "))
    y=int(input("Введіте 'y' для обчислення ctg(x+y):  "))
    from math import cos, sin
    print("ctg(x + y) =",'{:.2e}'.format(cos(x+y)/sin(x+y)))
except ValueError:
    print("ви ввели не правильні дані у 'x' or 'y'")
except:
    if x+y==0:
        print("ctg 0, НЕ ІСНУЄ")
print("////////////////////////////////////////\n")
