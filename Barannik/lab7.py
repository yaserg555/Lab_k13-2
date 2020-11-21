#3
def par(n):
    return '1' in str(n) or '3' in str(n) or '5' in str(n) or '7' in str(n) or '9' in str(n)

#4
import math
def f(x):
    return math.sin(math.cos(x * 13)) + math.cos(math.log1p(x))
def max_znachena(a, b):
    i = a
    m = f(b)
    while i < b:
        if f(i) > m :
            m = f(i)
        i += 0.001
    return m

#5
def fi(m):
    fi1 = 1
    fi2 = 1
    while fi2 <= m:
        fi1, fi2 = fi2, fi1+fi2
    return fi2
