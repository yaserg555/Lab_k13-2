https://www.codewars.com/users/Annalab-sys
@SerialManiacbot

# 1
t = str(input("Ваше ім'я - "))
k = str(input("Ваше прізвище - "))
def hello(x, y)
     return f'Вітаю,{y} {x}'
print(f"Вітаю, {hello(t, k)}")

# 2
m=float(input())
n=float(input())
l=float(input())
def equality(a, b, c):
    d = a!=b and a!=c and b!=c
    return d
print(f"Числа попарно нерівні: {equality(n, m, l)}")

# 3
def epsilon(x, y, e = (10 ** -10)):
    return float(x - y) <= e
    
# 4
def geo(aa, bb, aaa, bbb):
    return aa * bbb == aaa * bb
first = int(input('a = '))
second = int(input('b = '))
third = int(input('c = '))
fourth = int(input('d = '))

print(f"Прямі колінеарні: {geo(first, second, third, fourth)}")

