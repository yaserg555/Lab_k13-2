x = float(input("Перша сторона трикутника "))
y = float(input("Друга сторона трикутника "))
z = float(input("Третя сторона трикутника "))
import math
p = float(x+y+z/2)
s = math.sqrt(p*(p-x)*(p-y)*(p-z))

if x > y+z:
    print("Помилка")
elif y > z+x:
    print("Помилка")
elif z > x+y:
    print("Помилка")
else:
    print(f'Периметр:{x+y+z}')
    print(f'Площа:{s}')


    
x1=int(input("X = "))
y1=int(input("Y = "))

print(f'O[{x1},{y1}]')

# 6
a = int(input("Перше число = "))
b = int(input("Друге число = "))
c = int(input("Третє число = "))
if a+b == c:
    print(f"Yes")
elif b+c == a:
    print(f"Yes")
elif c+a == b:
    print(f"Yes")
else:
    print(f"No")
    
# 7 
aa = int(input("Введіть перше число "))
bb = int(input("Введіть друге число "))
cc = int(input("Введіть третє число "))
dd = int(input("Введіть четверте число "))
if aa%2 != 0 and bb%2 != 0 and cc != 0 and dd != 0:
    print(f"Not found")
else:
    while max(aa,bb,cc,dd)%2 != 0:
        if max(aa,bb,cc,dd) == aa and aa%2 != 0:
            aa = 0
            continue
        if max(aa,bb,cc,dd) == dd and dd%2 != 0:
            dd = 0
            continue
        if max(aa,bb,cc,dd) == cc and cc%2 != 0:
            cc = 0
            continue
        if max(aa,bb,cc,dd) == bb and bb%2 != 0:
            bb = 0
            continue
    else:
        print(max(aa,bb,cc,dd))

# 8
v = [1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,2,6,2,7,2,8,2,9,3,0,3,1,3,2,3,3,3,4,3,5,3,6,3,7,3,8,3,9,
     4, 0, 4, 1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6, 4, 7, 4, 8, 4, 9, 5, 0, 5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6, 5, 7, 5, 8, 5,
     9, 6, 0, 6, 1, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6, 6, 7, 6, 8, 6, 9, 7, 0, 7, 1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6, 7, 7, 7, 8,
     7, 9, 8, 0, 8, 1, 8, 2, 8, 3, 8, 4, 8, 5, 8, 6, 8, 7, 8, 8, 8, 9, 9, 0, 9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6, 9, 7, 9,
     8, 9, 9]
d = int(input("Введіть число "))
print(v[d])

# 9
j = 3
k = 0
r = 5
from math import cos
while j <= 111 and r <= 113:
       k += cos(j+r)
       j += 2
       r += 2
       
print(k)

# 10

import requests
from bs4 import BeautifulSoup


def world_covid19_stats(url: str = "https://www.worldometers.info/coronavirus/country/ukraine/") -> dict:
    """
    Return a dict of current Ukraine COVID-19 statistics
    """
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    keys = soup.findAll("h1")
    values = soup.findAll("div", {"class": "maincounter-number"})
    keys += soup.findAll("span", {"class": "panel-title"})
    values += soup.findAll("div", {"class": "number-table-main"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}


if __name__ == "__main__":
    print("\033[1m" + "COVID-19 Status of Ukraine" + "\033[0m\n")
    for key, value in ukraine_covid19_stats().items():
        print(f"{key}\n{value}\n")

# 11
aaa = [1, 3, 4, 5, 4, 5]
bbb = set(aaa)
if len(aaa) == len(bbb):
    print('Всі числа унікальні')
else:
    print('Числа не унікальні')

# 12
x = float(input("Введіть значення х = "))
y = float(input("Введіть значення y = "))
q = x
y = q
x = y
print(f"x={x}, y={y}")


x = float(input("Введіть значення х = "))
y = float(input("Введіть значення y = "))
x=x+y
y=x-y
x=x-y
print(f"x={x}, y={y}")

x = float(input("Введіть значення х = "))
y = float(input("Введіть значення y = "))
x, y =y, x
print(f'x={x}, y={y}')
