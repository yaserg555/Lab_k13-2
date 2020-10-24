# №1
def perymetr():
    try:
        a=float(input("Уведіть довжину стороти 1: "))
        b=float(input("Уведіть довжину сторони 2: "))
        c=float(input("Уведіть довжину сторони 3: "))
        if a<=0 or b<=0 or c<=0:
            print("Введи додатнє число(крім 0)!!")
        else:
            print("Периметр трикутника",a + b + c)
    except ValueError:
        print("Введи число!!!")
# №2
def koordynata():
    try:
        x = float(input("Уведіть координату 'x' точки: "))
        y = float(input("Уведіть координату 'y' точки: "))
        print(f"[{x},{y}]")
    except ValueError:
        print("Введи число!!!")
# №3
def try_chysla():
    try:
        a=int(input("Число а:  "))
        b=int(input("Число b:  "))
        c=int(input("Число c:  "))
        if a+b==c or a+c==b or c+b==a:
            print("Yes")
        else:
            print("No")
    except ValueError:
        print("Введи число!!!")
# №4
def max_chyslo():
    try:
        k=[]
        a=int(input("Число a:  "))
        b=int(input("Число b:  "))
        c=int(input("Число c:  "))
        d=int(input("Число d:  "))
        v=[a,b,c,d]
        for i in range(0,4):
            if v[i]%2==0:
                k.insert(0,v[i])
        print(max(k))
    except BaseException:
        print("not found")

# №5
def k():
    try:
        k=int(input("Введи число k: "))
        s=0
        for i in range(10,100):
            s=s*100+i
        if k<=1 or k>=180:
            print("Error!")
        else:
            s=str(s)
            a=list(s)
            print(a[k-1])
    except ValueError:
        print("Введи число!!!")

# №6
def sume():
    from math import cos
    i=3
    j=5
    s=0
    while i!=113:
        s+=cos(i/j)
        i+=2
        j+=2
    print(s)

# №7
def log():
    from math import log
    x=int(input("Введи x: "))
    y=int(input("Введи y: "))
    print(log(x+y,69))

perymetr()
koordynata()
try_chysla()
max_chyslo()
k()
sume()
log()
