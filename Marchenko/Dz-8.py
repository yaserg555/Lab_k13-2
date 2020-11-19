def func1(n):
    c = 1
    print(c)
    for k in range(1, n+1):
        c1 = c * (k + n) / k
        c = c1
        print(int(c))
    return ''


def func2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * func2(n-2)


def func3(x):
    if x >= 0:
        a = list(str(x))
        b = []
        for i in a:
            b.append(str(int(i) ** 2))
        return ''.join(b)


def func4(n):
    c = 1
    print(c)
    for k in range(1, n + 1):
        c1 = c * (2 * k - 1) * 2 * k / (k ** 2 + k)
        c = c1
        print(int(c1))
    return ''
