#1
def func1():
    a = [1, 5, 87, 37]
    a[1] = 13
    a.append(25)
    a[1:2] = (4,5)
    a.pop(3)
    a.pop(3)
    a[2:3] = (8, 5)
    b = tuple(a)
    print(b)
    a = a * 2
    a.pop(-1)
    print(a)
    print((b)[::-1])
func1()

#15
def func3(nums):
    count = 0
    for i in nums:
        if i > 0:
            count = count + 1
    return count


#18
def func4(integers):
    return [x for x in integers if x != 0]

#20
def func5(lst):
    return lst[-1:] + lst[:-1]

#34
def func7(lst1, lst2):
    d = []
    for i in a:
        for j in b:
            if i == j:
                d.append(i)
    return d

#44
import datetime
def func9():
    year = int(input("Введіть рік: "))
    month = int(input("Введіть порядковий номер місяця: "))
    day = int(input("Введіть число: "))
    a = datetime.datetime(year, month, day).strftime("%j")
    return a

