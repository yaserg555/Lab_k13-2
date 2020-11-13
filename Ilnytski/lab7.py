import math
def has_odd(n):
    while n > 0 and n % 10 % 2 == 0:
        n //= 10
    return n != 0

def func(x):
    return math.sin(math.cos(13*x)) + math.cos(math.log(x))

def max_on_interval(a, b):
    if (b < a):
        a, b = b, a
    if (b < 0):
        return None
    if (a <= 0):
        a = 1e-6
    range = b - a
    dx = range / 50_000
    max_y = float('-inf')
    while a <= b:
        y = func(a)
        if (y > max_y):
            max_y = y
        a += dx
    return max(max_y, func(a), func(b))


def fibonacci(n):
    if n == 0:
        return 1
    a = 0
    b = 1
    c = 1
    while c <= n:
        c = a + b
        a = b
        b = c
    return c
print(has_odd(4323213))
print(fibonacci(3))
print(max_on_interval(-10, 10))
