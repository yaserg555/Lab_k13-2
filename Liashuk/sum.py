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
        a1=int(input("Число a1:  "))
        b1=int(input("Число b1:  "))
        c1=int(input("Число c1:  "))
        d1=int(input("Число d1:  "))
        print(max(a1,b1,c1,d1))
    except ValueError:
        print("not found")

# №5
def k():
    k=int(input("Введи число k: "))
    s=0
    for i in range(10,100):
        s=s*100+i
    s=str(s)
    a=list(s)
    print(a[k-1])
perymetr()
koordynata()
try_chysla()
max_chyslo()
def k()
