     #1
def func(x):
    x = list(str(x))
    a = ['1', '3', '5', '7', '9']
    k = list(set(x) & set(a))
    if not k:
        return False
    else:
        return True


      #3
def func1(m):
    f0, f1, n = 0, 1, 2
    while f0 <= m:
        n += 1
        f = f1 + f0
        f0, f1 = f1, f
    else:
        return f0
