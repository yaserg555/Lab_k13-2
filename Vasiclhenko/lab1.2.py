v = int(input('v'))
print('a')
a= v%10
print(a)
print('б')
b = ''
while v > 0:
    b = str(v % 2) + b
    v = v // 2
b=int(b)
print(b%10)

a=(10.001/9.001)**345
b=(13.001/11.001)**249
x=a*b/((9.001**10)*(11.001**20))
print(x)

print('Виконавець: Васильченко')
print('            Юрiй')
print('            Сергiйович')
print('     Група: К-13(2)')
