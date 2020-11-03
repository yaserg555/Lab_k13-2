def z1(r):
    return r=='A' or r=='B' or r=='C' or r=='D' or r=='E' or r=='F'

def z2(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1

def z3(a,b,c):
    d=b**2-4*a*c
    if a==b==c==0:
        return -1
    elif a==0==b or d<0:
        return 0
    elif a==0 or d==0:
        return 1
    elif d>0:
        return 2

def z4(a,b,c,x,y):
    k=[a,b,c]
    k.sort()
    o=[x,y]
    o.sort()
    return k[1]<=o[1] and k[2]<=o[2]

def z5(n):
    if 5<=n%100<=20:
        s=(f'{n} років')
    elif n%10==1:
        s=(f'{n} рік')
    elif 2<=n%10<=4:
        s=(f'{n} рокb')
    elif 5<=n%10<=9 or n%10==0:
        s=(f'{n} років')
    return s
