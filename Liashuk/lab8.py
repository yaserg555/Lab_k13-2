print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ Завдання № 2 ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
def kombinazia(n):
    k=1
    c=1
    s=1
    while k!=(n+1):
        c*=(n+k)/k
        k+=1
        s+=c
    return int(s)
kombinazia(10)
print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ Завдання № 4 ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
def f(a):
    s=''
    while a>0:
        b=a%10
        s=str(b**2)+s
        a=a//10
    return s if a>=0 else False
f(12304)
