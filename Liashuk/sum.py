try:                                   #3 AND 4
    a = float(input("Уведіть довжини стороти 1: "))
    b = float(input("Уведіть довжини сторони 2: "))
    c = float(input("Уведіть довжини сторони 3: "))
    print(a + b + c)
    x = float(input("Уведіть координату x точки: "))
    y = float(input("Уведіть координату y точки: "))
    print(f"[{x},{y}]")
except:
    print("Введи число!!!")
from math import log                  #5
x=input("x")
y=input("y")
print(log(int(x+y),69))
try:                                   #6
    a=int(input("Число а:  "))
    b=int(input("Число b:  "))
    c=int(input("Число c:  "))
    if a+b==c or a+c==b or c+b==a and  a >= 0 and b >= 0 and c >= 0:
        print("Yes")
    else:
        print("No")
except:
    print("Введи число!!!")
try:                                    #7
    a1=int(input("Число a1:  "))
    b1=int(input("Число b1:  "))
    c1=int(input("Число c1:  "))
    d1=int(input("Число d1:  "))
    print(max(a1,b1,c1,d1))
except:
    print("not found")
k=int(input("k:  "))                          #8
x=int(k/20)
y=k%20
if k%2==0:
    print((y-1)%10)
else:
    print(x+1)
a=[1,3,3,5,7,2,5,4,3,10,7]
print(set(a))
