v = int(input('v'))
print('a')
a = v
k = a % 10
while k == 0:
    a = a // 10
    k = a % 10

print(k)
print('б')
b = ''
while v > 0:
    b = str(v % 2) + b
    v = v // 2
b=int(b)
k = b % 10
while k == 0:
    b = b // 10
    k = b % 10
print(b%10)

a=(10.001/9.001)**345
b=(13.001/11.001)**249
x=a*b/((9.001**10)*(11.001**20))
print(x)

t= '''Исполнитель: Васильченко
             Юрий
             Сергеевич
      Група: К-13(2)'''
print(t)
