def chyslo(a,b):
    try:
        x=float(input('Введіть число: '))
    except ValueError:
        print("input wrong")
    return x if a<=x<=b else f"Введіть число що належить проміжку [{a};{b}]"
print(chyslo(3,7))
