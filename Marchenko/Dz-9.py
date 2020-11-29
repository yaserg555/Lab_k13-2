a = []
for i in range(0, 101):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:                                    # 5
        a.append(i)

     #14
def func1(n, b:list):
    while n in b:
        b.remove(n)
    else:
       return b

       # 29a
def func2a(c:list):
    return c[::2]

       # 29b
def func2b(d:list):
    return d[1::2]

     # 18
def func3(a:list):
    while 0 in a:
        a.remove(0)
    else:
        return a

     # 13
def func4(n:int):
    a = []
    while len(a) < n:
            b = int(input())
            if b not in a:
                 a.append(b)
            else:
                raise RuntimeError
    else:
        return a

     #27
def sp_condition(i):
    return i % 3 == 0


def func5(a:list):
     return [i for i in a if sp_condition(i)]

       # 37
def func6(a:list):
    b = [i for i in a if str(3) not in str(i)]
    c = [b[0]]
    i = 1
    while i <= (len(b) - 1):
        if b[i] >= b[i-1]:
            c.append(b[i])
            i += 1
        else:
            break
    return c

       # 40
def _func7(b, c):
    i = len(c)
    while i <= (len(b) - 1):
        if b[i] <= b[i - 1]:
            c.append(b[i])
            i += 1
        else:
            break
    return c


def func7(a:list):
    b = [i for i in a if str(3) not in str(i)]
    print(b)
    c = [b[0]]
    i = 1
    while i <= (len(b) - 1):
        if b[i] >= b[i-1]:
            c.append(b[i])
            i += 1
        else:
            c.append(b[i])
            break
    return _func7(b, c)
