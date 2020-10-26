#1
def cufra(x) :
    return x=='0' or x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or x=='8' or x=='9' or x=='A' or x=='B' or x=='C' or x=='D' or x=='E' or x=='F'

#2
def znak(x):
    f=0
    if x<0:
        f=-1
    elif x>0:
        f=1
    return f

#3
def rivnannya(a, b, c):
    f=0
    if a==0:
        if b!=0:
            f=1
        elif c==0:
            f=-1      
    elif (b**2-4*a*c)>0:
        f=2
    elif (b**2-4*a*c)==0:
        f=1
    return f

#4
def cegla(a, b, c, x, y):
    return min(a, b,c)<=min(x, y) and (a+b+c-min(a, b, c)-max(a, b, c))<=max(x, y)

#5
def vik(x):
    if x%10==1:
        s='рік'
    elif x%10==2 or x%10==3 or x%10==4:
        s='роки'
    else:
        s='років'
    return f'{x} {s}'
