# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

"""10"""
A = []
def f():
    try:
        n = int(input("Enter n:"))
        for i in range(n):
            A.append(list(map(int, input().split())))
        print(A)
    except ValueError:
        exit()
f()

"""12"""
A = [1, 2, 3, 4, 5]
e = int(input("Enter e:"))
def add(A, e):
    if A.count(e) == 0:
        A.append(e)
    return A.index(e)
print(add(A, e))


"""15"""
def f1(n, i):
    d = 0
    while i in n:
        if i > 0:
            d = d + 1
    return d


"""26"""
def func1(list):
    element_list = []
    for i in range(len(list)):
        if list[i] % 13 == 0:
            element_list.append(list[i])
    return element_list

"""27"""
def umova(i):
    return i % 2 == 0

def func2(list):
     return [for i in list if umova(i)]
     
 
"""45"""
def f45(str):
    count = 0
    for i in str:
        if i.isdigit() is True:
            count += 1
    return count
