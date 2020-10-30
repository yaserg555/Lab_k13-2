# 1
def salut(name, surname):
    return f'Hi, {name} {surname}! May the number 72 will guide you!'
surname = input("What's your surname? ")
name = input("What's your name? ")
print(salut(name, surname))

 # 2
def non_equal(x, y, z):
    return x != y and y != z and x != z

# 3
from math import round
def approx_equal(a, b):
    return round(a, 10) == round(b, 10)

# 4
def parallel_lines(a1, b1, c1, a2, b2, c2):
    return a1 / a2 == b1 / b2 and c1 != c2
