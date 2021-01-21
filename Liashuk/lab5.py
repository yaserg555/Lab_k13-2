#№1
def f(x):
    x = input(f"Напишите одну букву")
    bykva = ["A", "B", "C", "D", "E", "F"]
    return x in bykva
# №2
def oznaka(x):
    if x>0:
        a=1
    elif x<0:
        a=-1
    else:
        a=0
    return a
# №3
def rivnyna(a,b,c):
    D=b**2-4*a*c
    if D>0:
        x=2
    elif D==0 and a!=b!=c!=0:
        x=1
    elif a==b==c==0:
        x=-1
    else:
        x=0
    return x
# №4
def xnay(a,b,c,x,y):
    k1=[a,b,c]
    k2=min(k1)
    k1.remove(k2)
    k3=min(k1)
    return ((x>=k2) and (y>=k3)) or ((x>=k3) and (y>=k2))
# №5
def vik(age):
    if ( 11 <= age and age <= 19):
        print(age, "років")
    elif(age % 10 == 1):
        print(age, "рік")
    elif(2 <= age % 10 <= 4):
        print(age, "роки")
    else:
        print(age, "років")

oznaka(-32328347346354875)
rivnyna(3,3,-3)
xnay(21,3434,1,143,32)
vik(100)
