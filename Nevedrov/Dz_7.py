import math
#3


def is_odd(number):
    while number != 0:
        if (t := abs(number) % 10) % 2 == 1:
            return True
        number = (abs(number) - t)/10
    return False


#4


def f(x):
    try:
        return math.sin(math.cos(13*x))+math.cos(math.log(x, math.e))
    except ValueError:
        return None


def max_F(a, b, delta_x):
    local_maximums_coordinates = []
    if (t := f(a)) is not None:
        local_maximums_coordinates.append((a, t))
    if (t := f(b)) is not None:
        local_maximums_coordinates.append((b, t))
    while a < b:
        try:
            if (t:=f(a)) > f(a - delta_x) and t > f(a + delta_x):
                local_maximums_coordinates.append((a, t))
            a += delta_x
        except TypeError:
            a += delta_x
    try:
        return max(local_maximums_coordinates, key=lambda i: i[1])[0]
    except ValueError:
        print('Extremums don\'t exist')


#5


def least_bigger_fibonacci_number(number):
    F_0 = 0
    F_1 = 1
    while (F_2 := F_0 + F_1) <= number:
        F_1, F_0 = F_2, F_1
    return F_2
