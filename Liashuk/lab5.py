#№2
def oznaka(x):
    if x>0:
        a=1
    elif x<0:
        a=-1
    else:
        a=0
    return a
#№3
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
#№4
def xnay(a,b,c,x,y):
    if a*b<=x*y or a*c<=x*y or b*c<=x*y:
        print('Yes')
    else:
        print('No')
#№5
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
