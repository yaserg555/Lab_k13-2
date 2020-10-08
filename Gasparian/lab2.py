# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''from numpy.core import long'''

from decimal import Decimal

a = 2*4%7
print("2*4%7 = " + str(a))
print(type(a))

b = 2*(4%7)
print("2*(4%7) = " + str(b))
print(type(b))

c = 51//6%7
print("51//6%7 = " + str(c))
print(type(c))

d = 51//(6%7)
print("51//(6%7) = " + str(d))
print(type(d))

e = (-3+5)*(2%7//3+4*2)
print("(-3+5)*(2%7//3+4*2) = " + str(e))
print(type(e))

f = (3//5.0)*20+32.0
print("(3//5.0)*20+32.0 = " + str(f))
print(type(f))

g = float(int(1.56))
print("float(int(1.56)) = " + str(g))
print(type(g))

h = bool(-0.0)
print("bool(-0.0) = " + str(h))
print(type(h))

k = float('inf')
print("float('inf') = " + str(k))
print(type(k))

l = int(bool(13.56))
print("int(bool(13.56)) = " + str(l))
print(type(l))

m = ((Decimal(10.001) ** 345) * (Decimal(13.001) ** 249)) / ((Decimal(9.001) ** 355) * (Decimal(11.001) ** 269))
print("(10.001**345*13.001**249)/(9.001**355*11.001**269)=" + str(m))

n = "Виконавець: Гаспарян \n\t\t\tНiкiта \n\t\t\tОлегович \n\tГрупа: К-13(2)"
print(n)
