#https://www.codewars.com/users/korven

def zad1(pr, im):
    k=(f'Hello, {pr} {im}')
    return print(k)

def zad2(x, y, z):
    q = x!=y and x!=z and y!=z
    return print(q)

def zad3(x,y):
    e=10-10
    q=((x-y)<=e and (x-y)>=-e)
    return print(q)

def zad4(a1,b1,c1,a2,b2,c2):
    k1=-a1/b1
    k2=-a2/b2
    h1=-c1/b1
    h2=-c2/b2
    return print(k1==k2 and h1!=h2)
