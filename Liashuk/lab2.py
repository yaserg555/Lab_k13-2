#№1
print(2*4%7, type(2*4%7))
print(2*(4%7), type(2*(4%7)))
print(51//6%7, type(51//6%7))
print(51//(6%7), type(51//(6%7)))
print((-3+5)*(2%7//3+4*2), type((-3+5)*(2%7//3+4*2)))
print((3//5.0)*20+32.0, type((3//5.0)*20+32.0))
print(float(int(1.56)), type(float(int(1.56))))
print(bool(-0.0), type(bool(-0.0)))
print(float('inf'), type(float('inf')))
print(int(bool(13.56)), type(int(bool(13.56))))

#№2
def chislo1(x):
    print(x%2)
def chislo2(x):
    print(hex(x%16))
def chislo3(x):
    print(x%10)

print("значення молодшої двійкової цифри числа:"),chislo1(2324544)
print("значення молодшої шістнадцяткової цифри числа:"),chislo2(122312321)
print("значення молодшої десяткової цифри числа:"),chislo3(122312321)


#№3
print((10.001/9.001)**345*(13.001/11.001)**249/9.001**10/11.001**20)

#№4
print("""
Виконавець: Ляшук
            Андрій
            Анатолійович
     Група: К-13(2)
""")
