print("First part")
print(" ")
a = 2*4%7
print("2*4%7 = " + str(a))
print("Type of result:")
print(type(a))
print(" ")
b = 2*(4%7)
print("2*(4%7) = " + str(b))
print("Type of result:")
print(type(b))
print(" ")
c = 51//6%7
print("51//6%7 = " + str(c))
print("Type of result:")
print(type(c))
print(" ")
e = (-3+5)*(2%7//3+4*2)
print("(-3+5)*(2%7//3+4*2) = " + str(e))
print("Type of result:")
print(type(e))
print(" ")
f = (3//5.0)*20+32.0
print("(3//5.0)*20+32.0 = " + str(f))
print("Type of result:")
print(type(f))
print(" ")
g = float(int(1.56))
print("float(int(1.56)) = " + str(g))
print("Type of result:")
print(type(g))
print(" ")
d = bool(-0.0)
print("bool(-0.0) = " + str(d))
print("Type of result:")
print(type(d))
print(" ")
j = float('inf')
print("float('inf') = " + str(j))
print("Type of result:")
print(type(j))
print(" ")
k = int(bool(13.56))
print("int(bool(13.56)) = " + str(k))
print("Type of result:")
print(type(k))
print(" ")
print("Third part")
print(" ")
l = (((10.001/9.001)**345)*((13.001/11.001)**249))/((9.001**10)*(11.001**20))
print("10.001^345 *13.001^249 / (9.001^355 * 11.001^269) = " + str(l))
print(" ")
print("Fourth part")
print(" ")
print(r) = """Виконавець: Рижова
            Олександра
            Юріївна
     Група: К-13(2)"""
print("Second part-1")
print(" ")
print("Write a number _ ")
v1 = int(input())
if v1>=0:
    q1 = str(v1)
    q1 = list(q1)
    print(min(q1))
    v1 = bin(v1)
    v1 = str(v1)
    v1 = list(v1)
    print(min(v1))
else:
    print("Error")
print(" ")
print("Second part-2")
print(" ")
print("Write a number _ ")
v2 = int(input())
if v2>=0:
    print(v2%10)
else:
    print("Error")
if v2>=0:
    print(v2%2)
else:
    print("Error")
print(" ")
print("Second part-3")
print(" ")
print("Write a number _ ")
v3 = int(input())
v4 = v3
if v4>=0:
    while v4%10==0 :
        v4 = v4/10
    else:
        print(v4%10)
else:
    print("Error")
if v3>=0:
    v3 = bin(v3)
    v3 = str(v3)
    v3 = list(v3)
    print(v3[-1])
else:
    print("Error")
