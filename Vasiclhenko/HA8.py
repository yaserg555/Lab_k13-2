def z2(n):
    print (1)
    q=1
    for i in range (1,n):
        q=q*((n+i)/i)
        print(q)
    return ""

#print(z2(3), z2(5), z2(4))

def z3(n):
    q=1
    w=1
    e=1
    for i in range(2,n+1):
        e=q*i
        q=w
        w=e
    return e

#print(z3(4), z3(6), z3(5))

def z4(n):
    s=''
    n=str(n)
    for i in range(len(n)):
        q=str(int(n[i])**2)
        s+=q
    return s

#print(z4(156),z4(3126),z4(141234))

def z5(n):
    print(1)
    for i in range(1,n):
        q=1
        d=1
        for j in range(i+1, i*2):
            q=q*j
        for j in range(1,i):
            d=d*j
        c=2*(q/d)/(i+1)
        print(c)
    return ''

#print(z5(6),z5(4),z5(10))
