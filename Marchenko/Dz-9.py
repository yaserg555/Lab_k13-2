a = []
for i in range(0, 101):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:                                    # 5
        a.append(i)


def func1(n:int, b:list):
    while n in b:                                                                    # 14
        b.remove(n)
    else:
        return b


def func2a(c:list):                                                                          # 29a
    return c[::2]


def func2b(d:list):
    return d[1::2]                                                                           # 29b


def func3(a:list):
    while 0 in a:                                                                            # 18
        a.remove(0)
    else:
        return a


def func4(n:int):
    a = []
    while len(a) < n:
            b = int(input())
            if b not in a:                                                              # 13
                 a.append(b)
            else:
                raise RuntimeError
    else:
        return a
