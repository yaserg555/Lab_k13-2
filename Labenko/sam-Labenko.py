x = float(input("Перша сторона трикутника "))
y = float(input("Друга сторона трикутника "))
z = float(input("Третя сторона трикутника "))
import math
p = float(x+y+z/2)
s = math.sqrt(p*(p-x)*(p-y)*(p-z))

if x > y+z:
    print("Помилка")
elif y > z+x:
    print("Помилка")
elif z > x+y:
    print("Помилка")
else:
    print(f'Периметр:{x+y+z}')
    print(f'Площа:{s}')


    
x=int(input("X = "))
y=int(input("Y = "))

print(f'O[{x},{y}]')

# 6
a = int(input("Перше число = "))
b = int(input("Друге число = "))
c = int(input("Третє число = "))
if a+b == c:
    print(f"Yes")
elif b+c == a:
    print(f"Yes")
elif c+a == b:
    print(f"Yes")
else:
    print(f"No")
    
# 7 
aa = int(input("Введіть перше число "))
bb = int(input("Введіть друге число "))
cc = int(input("Введіть третє число "))
dd = int(input("Введіть четверте число "))
if aa%2 != 0 and bb%2 != 0 and cc != 0 and dd != 0:
    print(f"Not found")
else:
    while max(aa,bb,cc,dd)%2 != 0:
        if max(aa,bb,cc,dd) == aa and aa%2 != 0:
            aa = 0
            continue
        if max(aa,bb,cc,dd) == dd and dd%2 != 0:
            dd = 0
            continue
        if max(aa,bb,cc,dd) == cc and cc%2 != 0:
            cc = 0
            continue
        if max(aa,bb,cc,dd) == bb and bb%2 != 0:
            bb = 0
            continue
    else:
        print(max(aa,bb,cc,dd))
