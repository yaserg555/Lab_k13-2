# 1

x = input(f'Впишіть літеру')
def vic(x):
    d = ['A', 'B', 'C', 'D', 'E', 'F']
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
      
# 4
a = float(input(f"Довжина першого ребра цегли = "))
b = float(input(f"Довжина другого ребра цегли = "))
c = float(input(f"Довжина третього ребра цегли = "))
x = float(input(f"Довжина вікна = "))
y = float(input(f"Ширина вікна = "))
def vic(a, b, c, x, y):
    return (x > b and x > a and y > b and y > a) or (x > b and x > c and y > b and y > b) or (x > a and x > c and y > a and y > c)
print(f'Чи влазить цегла у вікно? {vic(a, b, c, x, y)}')
     
# 5
x = int(input(f'Скільки років?'))
def years(x):
    d = (x % 10)
    if d == 1 and x != 11:
        return 'рік'
    elif (d == 2 or d == 4 or d == 3) and x not in range(11,15) :
        return 'рoки'
    elif d in range(5,10) or d == 0 or x in range(11,20):
        return 'рoків'
    else:
        return 'error'
print(f' {x} {years(x)}')
    
