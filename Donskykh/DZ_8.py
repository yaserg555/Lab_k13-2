def f2_8(n):
    x = 1
    print(x)
    for i in range(1, n + 1):
        x *= (n + i )/i
        print(x)
        
        
def f3_8(n):
    x=1
    while n>1:
        x*=n
        n=n-2
    return x


def f4_8(n):
    n = str(n)
    a=""
    for i in n:
        a=a+ str(int(i) ** 2)
    return a


def f5_8(n):
    x=2
    print(f'1\n1')
    for i in range(2,n+1):
        x*=(2*i-1)*(2*i)/i**2
        print(x/(i+1))
