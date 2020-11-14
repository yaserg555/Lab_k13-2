

def seq_c(number):
    c_1 = 1
    for i in range(0, number + 1):
        print(int(c_1))
        c_1 *= (number + i + 1)/(i + 1)


def double_factorial(number):
    if number <= 1:
        return 1
    return number * double_factorial(number-2)


def square_digits_number(number):
    square_digits = []
    for i in range(0, len(t := str(number))):
        square_digits.append(str(int(t[i])**2))
    return ''.join(square_digits)


def seq_c_2(number):
    c_2 = 1
    k = 1
    while k < number:
        c_2 *= (2 * k + 2) * (2 * k + 1) / (k + 1) / (k + 2)
        k += 1
    return int(c_2)
