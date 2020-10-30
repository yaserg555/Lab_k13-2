x = input(f'Впишіть літеру')
def vic(x):
    d = ['A', 'B', 'C', 'D', 'E', 'F']
    return x in d
print(f'{vic(x)})
#№2
def oznaka(x):
    if x>0:
        a=1
    elif x<0:
        a=-1
    else:
        a=0
    return print(a)
#№3
def rivnyna(a,b,c):
    if a!=0:
        D=b**2-4*a*c
        if D>0:
            x=2
        elif D<0:
            x="Ne isnuye"
        else:
            x=1
    elif a==b==c==0:
        print(-1)
    elif a==0:
        x=1
    return print(x)
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
