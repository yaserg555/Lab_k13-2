import math
#9
#a=['qqq']
#a.append(input())
#print(a)

#13
def z13(n):
    a=[]
    for i in range(n):
        a.append(input())
    return a
#print(z13(4))

#14
def z14(l,d):
    l=([i for i in l if i!=d])
    return l
#print(z14([123,123,2,5,2,4],2))

#16
def z16(l,q):
    v=[]
    for i in range(len(l)):
        if l[i]==q: v.append(i)
    return v
#print(z16([123,123,2,5,2,4],2))

def z21(l,o,n):
    for i in range(len(l)):
        if l[i]==o: l[i]=n
        elif l[i]==n: l[i]=o
    return l
#print(z21([123,123,2,5,2,4,123],2,123))

#31
def z31(n):
    l=[]
    for i in range (n):
        q=math.factorial(n)/(math.factorial(i)*math.factorial(n-i))
        l.append(q)
    return l
#print(z31(5))

#37
def h3(n):
    r=False
    while n>0:
        if n%10==3: r=True
        n=n//10
    return r

def z37(l):
    l = ([i for i in l if h3(i) != True])
    q=[l[0]]
    c=True
    i=1
    while c==True:
        if l[i]>=l[i-1]:
            q.append(l[i])
            i+=1
        else: c=False
    return q
#print(z37([1,4,6,7,4]),z37([1,5,3,7,9,6]))

def z42(b,d,m,y):
    a=[m,0,0,0,0,0,0,0,0]
    for j in range(y):
        n=0
        for i in reversed(range(1,9)):
            a[i]=a[i-1]//d
            n+=a[i]*b
        a[0]=n
    return a
#print(z42(4,2,2,3))
