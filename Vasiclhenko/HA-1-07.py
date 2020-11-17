import math
def z3(n):
    v=False
    while n>0 and v==False:
        c=n%10
        v= c%2==1
        n=n//10
    return v

def z4(a,b):
    m=-2.2
    if a<=0: a=10**-10
    while a<b:
        q1=math.sin(math.cos(13*a))
        q2=math.log(a)
        q3=math.cos(q2)
        q=q1+q3
        if q>m: m=q
        a+=10**-5
    return m

def z5(m):
    c1=0
    c2=1
    c=1
    while c<m:
        c=c1+c2
        c1=c2
        c2=c
    return c
