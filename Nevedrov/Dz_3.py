# https://www.codewars.com/users/Nevedrov
from math import isclose
#1


def hello():
    person = [input('Print your name:'), input('Print your surname:')]
    if not f'{person[0]}{person[1]}'.isalpha():
        print('Name or surname cannot include numbers')
        hello()
    else:
        print(f'Good morning, {person[0]} {person[1]}!')


hello()
#2
numbers = [input('x:'), input('y:'), input('z:')]
print(not(numbers[0] == numbers[1] or numbers[1] == numbers[2] or numbers[0] == numbers[2]))
#3
while True:
    try:
        a = float(input('Print first number:'))
        b = float(input('Print second number:'))
        break
    except ValueError:
        print('numbers type couldn\'t be string')


def if_close(a, b):
    print(isclose(a, b, rel_tol=0.1, abs_tol=0.1))
if_close(a, b)
#4
def if_lines_are_parallel():
    line_01 = [int(input('Print a1:')), int(input('Print b1:'))]
    line_02 = [int(input('Print a2:')), int(input('Print b2:'))]
    determinant = line_01[0] * line_02[1] - line_01[1] * line_02[0]
    return determinant == 0


if_lines_are_parallel()
