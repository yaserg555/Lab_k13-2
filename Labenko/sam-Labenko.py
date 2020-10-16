x = float(input("Перша сторона трикутника "))
y = float(input("Друга сторона трикутника "))
z = float(input("Третя сторона трикутника "))
s = x + y + z
if x > y+z:
    print("Помилка")
elif y > z+x:
    print("Помилка")
elif z > x+y:
    print("Помилка")
else:
    print(f'Периметр:{x+y+z}')
    
x=int(input("X = "))
y=int(input("Y = "))

print(f'O[{x},{y}]')
