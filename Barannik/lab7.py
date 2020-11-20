#2
def C(n):
    c = 1
    l = [1]
    k= 1
    while k <= n:
        c = (c * (n-k+1) // k)
        l.append(int(c))
        k = k + 1
    return l

#3
def factorial(n):
    f = 1
    i = n%2
    while i < n :
        i += 2
        f *= i
    return f

#4
def f(x):
    x=str(x)
    l = [ str(int(i)**2) for i in x ]
    return ''.join(l)

#5
def A(n):
    a = 1
    l = [1]
    k = 1
    while k <= n :
        a *= (2 * (2*k -1) // (k + 1))
        l.append(a)
        k += 1
    return l
