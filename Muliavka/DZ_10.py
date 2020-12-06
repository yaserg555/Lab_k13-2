# 3


def f_3(arr):
    counter, total = 0, 0
    for i in range(len(arr)):
        if arr[i] > 0:
        counter += 1
        total += i
    if counter:
        return total / counter
    else:
        return -1


# 4


def f_4(arr):
    for a in arr:
        if a <= 0:
            return False
    return True


# 5


def f_5(arr):
    for a in arr:
        if not a % 7:
            return False
    return True


# 6


def f_6(arr):
    return 7 in arr


# 8


def f_8(arr):
    return sum([a for a in arr if not a % 2])


# 9


def f_9(arr):
    return sum(arr[::2])
