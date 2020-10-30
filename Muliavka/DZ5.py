# 1
def f_1(s):
    return len(s) == 1 and s in 'ABCDEF'

# 2
def f_2(x):
    if not x:
        return 0
    else:
        return abs(x) / x

# 3
def solutions(a, b, c):
    if a == b == c == 0:
        return -1
    elif a == b == 0:
        return 0
    else:
        D = b ** 2 - (4 * a * c)
        if D < 0:
            return 0
        elif D == 0:
            return 1
        else:
            return 2

# 4
def cegla(a, b, c, x, y):
    return min(a, b, c) <= min(x, y) and (a + b + c - min(a, b, c) - max(a, b, c)) <= max(x, y)

# 5
def age(n):
    if n % 100 in range(11, 20):
        return str(n) + ' років'
    else:
        if n % 10 == 1:
            return str(n) + ' рік'
        elif n % 10 in range(2, 5):
            return str(n) + ' роки'
        else:
            return str(n) + ' років'
