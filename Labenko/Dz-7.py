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
