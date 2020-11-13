def binomial_2(n):
    c = 1
    s = 1
    for k in range(0, n):
        c_next = c * (n + k + 1) // (k + 1)
        print(c_next)
        c = c_next
        s += c
    return s
print(f"s = {binomial_2(3)}")
print("///")

def double_binomial(n):
    if (n <= 1):
        return 1
    else:
        return n * double_binomial(n-2)
print(double_binomial(10))
print("///")
def square_digits(n):
    if (n == 0):
        return "0"
    s = ""
    while n > 0:
        digit = n % 10
        s = str(digit * digit) + s
        n = n // 10
    return s
print(square_digits(153))
print("/// next")
def binomial_5(n):
    c = 1.0
    print(c)
    for k in range(0, n):
        c_next = c * (2*k + 1) * (2*k + 2) // ((k + 1) * (k + 1))
        c = c_next
        #print(c_next)
        print(c_next / (k+2))
binomial_5(10)
