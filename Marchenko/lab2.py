from decimal import Decimal
print('-1-')
a = 2 * 4 % 7
print('2*4%7=' + str(a))
print('Type of result:' + str(type(a)))
b = 2 * (4 % 7)
print('2*(4%7)=' + str(b))
print('Type of result:' + str(type(b)))
c = 51 // 6 % 7
print('51//6%7=' + str(c))
print('Type of result:' + str(type(c)))
d = 51 // (6 % 7)
print('51//(6%7)=' + str(d))
print('Type of result:' + str(type(d)))
e = (-3 + 5) * (2 % 7 // 3 + 4 * 2)
print('(-3+5)*(2%7//3+4*2)=' + str(e))
print('Type of result:' + str(type(e)))
f = (3 // 5.0) * 20 + 32.0
print('(3//5.0)*20+32.0=' + str(f))
print('Type of result:' + str(type(f)))
g = float(int(1.56))
print('float(int(1.56)=' + str(g))
print('Type of result:' + str(type(g)))
j = bool(-0.0)
print('bool(-0.0)=' + str(j))
print('Type of result:' + str(type(j)))
k = float('inf')
print('float(inf)=' + str(k))
print('Type of result:' + str(type(k)))
w = int(bool(13.56))
print('int(bool(13.56))=' + str(w))
print('-3-')
n = (Decimal(10.001) ** 345 * Decimal(13.001) ** 249) / (Decimal(9.001) ** 355 * Decimal(11.001) ** 269)
print('(10.001**345*13.001**249)/(9.001**355*11.001**269)=' + str(n))
print('-4-')
p = '''Виконавець: Марченко
            Вікторія
            Вікторівна
     Група: К-13(2)'''
print(p)
