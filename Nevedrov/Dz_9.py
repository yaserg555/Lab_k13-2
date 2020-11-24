#1
a = [1, 5, 87, 32]
a.insert(1, 13)
del a[2]
a.append(25)
a.insert(1, [4,5])
del a[2]
del a[2:4]
a.insert(2, 8)
del a[3]
b = tuple(a)
print(b)
a.extend(b)
del a[len(a)-1]
print(a)
b = list(b)
b.reverse()
b = tuple(b)
print(b)


#4
def square_list():
    return [i**2 for i in range(10, -1, -1)]


#12
def add_element(list, element):
    if list.count(element) == 0:
        list.append(element)
    return list.index(element)


#16
def indexes_list(list, element):
    indexes_list = []
    for i in range(list.count(element)):
        indexes_list.append(list.index(element, i, len(list)))
    return indexes_list


#26
def divide_by_13_list(list):
    element_list = []
    for i in range(len(list)):
        if not list[i] % 13:
            element_list.append(list[i])
    return element_list


#28
def pair_numbers_sum(list):
    sum = 0
    for i in range(len(list)-1):
        if not list[i] % 2:
            sum += list[i]
    return sum


def list_sum(list_1, list_2):
    return sorted(list(set(list_1 + list_2)))


#44
def day_number(day, month, year):
    days_number = 0
    for i in range(1, month):
        print(i)
        if i in {1, 3, 5, 7, 8, 10, 12}:
            days_number += 31
        elif i in {4, 6, 9, 11}:
            days_number += 30
        elif i in {2}:
            if not year % 4:
                days_number += 29
            else:
                days_number += 28
        else:
            raise Exception('Wrong month format!')
    days_number += day
    return days_number


#45
def digits_number(string):
    digits_number = 0
    for i in string:
        if i.isdigit():
            digits_number += 1
    return digits_number
