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
    
    
