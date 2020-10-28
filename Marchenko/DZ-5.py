
     # 1
def func(y):
    k = ['A', 'B', 'C', 'D', 'E', 'F']
    k += range(0, 10)
    return y in k


   #2
def func1(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


   # 3
def func2(a, b, c):
    d = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        return -1
    elif a == 0 and b == 0:
        return 0
    elif a == 0:
        return 1
    elif d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0


     #4
def func3(a, b, c, x, y):
    p = x + y
    return (2 * a) < p and (2 * b) < p and (2 * c) < p


     # 5
def func5(r):
    d = len(r) - 1
    if d == 2 and int(r[0]) == 1 and int(r[1]) == 1:
        return 'років'
    elif d == 1 and int(r[0]) == 1:
        return 'років'
    elif int(r[d]) == 1:
        return 'рік'
    elif int(r[d]) == 2 or int(r[d]) == 3 or int(r[d]) == 4:
        return 'роки'
    else:
        return 'років'

