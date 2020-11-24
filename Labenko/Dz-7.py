#1 
def odd():
    a = int(input(f"\nа = "))
    print(f"\nЧи містить число {a} непарні числа?")
    c = abs(a)
    d = 0
    while c > 0:
        if c % 2 != 0:
            d += 1
        c = c // 10
    if d >= 1:
        print(f"Так")
    else:
        print(f"Ні")
odd()

#2
def max(a,b):
    e = -10
    if a > b:
        a, b = b, a
    if a <= 0:
        a = 10 ** -6
    while a < b:
        f1 = math.sin(math.cos(13*a))
        f2 = math.cos(math.log(a))
        f = q1 + q2
        if f > e:
            e = f
        a += 10**-3
    return e

#3
def fibonacci():
    m = int(input(f"Введіть число "))
    n = 0
    p = 1
    k = n + p
    if m<0:
        return n
    while k <= m:
        c = p
        p += n
        n = c
        k = n+p
    return k
print(f"{fibonacci()}")
