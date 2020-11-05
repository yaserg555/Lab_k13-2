
def chyslo_1(a,b):
    try:
        x=float(input("Введи число: "))
        return print(f"Число що належить проміжку [{a};{b}]:\n{x}") if a<=x<=b else print(f"Введи число що належить певному проміжку [{a};{b}]")
    except ValueError:
        print("Введи число!")


def chyslo_2(a,b):
    try:
        x=float(input("Введи число: "))
        k=list(set(range(a,b+1)))
        k.index(x)
        print(f"Число що належить проміжку [{a};{b}]:\n{x}")
    except BaseException:
        print(f"Введи число що належить певному проміжку [{a};{b}]")

