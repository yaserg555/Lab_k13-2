# 1

x = input('Впишіть літеру')
def vic(x):
    d = 'ABCDEF'
    return x in d
print(f'Літера в шістнадцятковій системі? {vic(x)})

# 2

def number(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    elif x > 0:
        return 1
print(f'Результат = {number(x)}')

# 3
def maths(a,b,c):
    k = float((b**2)-4*a*c)
    if k < 0:
        return -1
    elif k == 0:
        return -b/2*a, b/2*a  
    elif k > 0:
        return float((-b+(sqrt(k))/(2*a))), float((-b-(sqrt(k))/(2*a)))
print(f'Результат = {maths(a,b,c)}')
