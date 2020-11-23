# 1
def combinations_1(n):
    c = 1
    k = n
    for i in range(n + 1):
        print(int(c))
        c *= (n + i + 1) / (n + i - k + 1)


# 2
def double_factorial(n):
    for i in range(n - 2, 0, -2):
        n *= i
    return n


# 3
def squares(n):
    s = str(n)
    result = ''
    for c in s:
        result += str(int(c) ** 2)
    return result


# 4
def combinations_2(n + 1):
    c = 1
    for i in range(n):
        print(int(c))
        n, k = i * 2, i
        c *= (n + 1) * (n + 2) / (k + 1) / (n - k + 1)
