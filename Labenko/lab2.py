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
f = (-3+5)*(2%7//3+4*2)
print("(-3+5)*(2%7//3+4*2) = " + str(f))
print(type(f))
g = (3//5.0)*20+32.0)
print("(3//5.0)*20+32.0) = " + str(g))
print(type(g))
h = float(int(1.56)) 
print("float(int(1.56)) = " + str(h))
print(type(h))
i = bool(-0.0)
print("bool(-0.0) = " + str(i))
print(type(i))
j = float('inf')
print("float('inf') = " + str(j))
print(type(j))
k = int(bool(13.56))
print("int(bool(13.56)) = " + str(k))
print(type(k))

name=input("Назвіть число ")
s=int(name)
print("Молодша десяткова цифра - " + str(s%10))
v = int(input("Назвіть число "))

b = ''

while v > 0:
    b = str(v % 2) + b
    v = v // 2

print(b)
print("Молодша двійкова цифра - " + str(v%10))

w = (10.001/9.001)*345
q = (13.001/11.001)*249
r = (w*q)
t = (9.001**10)
y = (11.001**20)
m = r/t
n = m/y
print("(10.001**345)*(13.001**249)/(9.001**355)*(11.001**269) = " + str(n))


l = """Виконавець: Лабенко
                   Анна
                   Євгенівна
            Група: К-13(2)"""
print(l)

