import numpy

def isHex(s):
    if (len(s) == 1 and -1 < ord(s) - 65 < 6):
        print("Yes")
    else:
        print("No")

def sign(x):
    print(numpy.sign(x))

def equation(a, b, c):
    if (a == 0):
        if (b == 0):
            if (c==0): print(-1)
            else: print(0)
        else: print((-c) / b)
    else:
        d = b*b - 4*a*c
        if d < 0: print(0)
        elif (d == 0): print(-b / 2 / a)
        else:
            print((-b - sqrt(d)) / 2, (-b + sqrt(d)) / 2)

def inside(x, y, z, a, b):
    if ((x < a and y < b) or (x < b and y < a) or (y < a and z < b) or (y < b and z < a) or (x < a and y < b) or (x < b and y < a)):
        print("Yes")
    else:
        print("No")

def gram_correct(age):
    if ( 11 <= age and age <= 19):
        print(age, "років")
    elif(age % 10 == 1):
        print(age, "рік")
    elif(2 <= age % 10 and age % 10 <= 4):
        print(age, "роки")
    else:
        print(age, "років")

s = input()
isHex(s)

x = float(input())
sign(x)

a = float(input())
b = float(input())
c = float(input())

equation(a, b, c)

x = float(input())
y = float(input())
z = float(input())

a = float(input())
b = float(input())

inside(x, y, z, a, b)

age = int(input())

gram_correct(age)
