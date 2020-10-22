# https://www.codewars.com/users/marchenkov25
# http://t.me/elfvic_bot

     # 1
def func(a, b):
    return f'Good morning, {a} {b}!'


v = input('What is your name?\n')
m = input('What is your surname?\n')
print(func(v, m))

     # 2
def func2(x, y, z):
    return x != y and x!= z 


k = input('x = ')
s = input('y = ')
t = input('z = ')
print(f'Змінні попарно різні: {func2(k, s, t)}')

     # 3
def func3(x, y, epsilon=(10 ** -10)):
    return abs(x - y) <= epsilon


g = float(input('перше дійсне значення = '))
h = float(input('друге дійсне значення = '))
print(f'Два дійсних значення рівні: {func3(g, h)}')

        #4
def func1(a1, b1, a2, b2):
    return a1 * b2 == a2 * b1


x = float(input('a1 = '))
y = float(input('b1 = '))
z = float(input('a2 = '))
t = float(input('b2 = '))

print(f'Колінеарні: {func1(x, y, z, t)}')

