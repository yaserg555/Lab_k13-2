#1


def is_hex(string):
    return string in {'A', 'B', 'C', 'D', 'E', 'F'}


#2


def x_two_remainder(x):
    return x % 2


#3


def roots(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return -1
    elif a == 0 and b == 0:
        return 0
    elif a == 0:
        return 1
    else:
        if b ** 2 - 4 * a * c > 0:
            return 2
        elif b ** 2 - 4 * a * c == 0:
            return 1
        else:
            return 0

#4


def test(a, b, c, x, y, answer):
    if if_promote(a, b, c, x, y) == answer:
        print('Right')
    else:
        print('Something wrong!')


def if_promote(a, b, c, x, y):
    '''if_promote(a, b, c, x, y) -> bool'''
    return a <= x, y and b <= y or b <= x and a <= y or b <= x and c <= y or c <= x and b <= y or a <= x and c <= y or c <= x and a <= y


#5


def years(age):
    if int(str(age)[len(str(age)) - len(str(age)) // 2 - 1]) in {0, 2, 3, 4, 5, 6, 7, 8, 9} or age == 1:
        if int(str(age)[len(str(age)) - 1]) == 1:
            return f'{age} рік'
        elif 0 < int(str(age)[len(str(age)) - 1]) <= 4:
            return f'{age} роки'
        else:
            return f'{age} років'
    else:
        return f'{age} років'
