# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
   3.Написати програму, яка за довжинами сторін трикутника обчислює його периметр. Вхідні значення вважати коректними.
   4.Написати програму, яка запитує в користувача координати точки дійсної площини, а потім виводить отриману точку. 
   Зверніть увагу на зовнішній вигляд друкованого результату.
"""

a = float(input("перша сторона: "))
b = float(input("друга сторона: "))
c = float(input("третя сторона: "))

if float(a + b < c):
    print("трикутника не існує")
elif float(a + c < c):
    print("трикутника не існує")
elif float(b + c < a):
    print("трикутника не існує")
else:
    print(f"периметр: {a + b + c}")


x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))
print(f"координати: {x}; {y}; {z}")
