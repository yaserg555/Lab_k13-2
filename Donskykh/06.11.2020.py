def f(x):
    if int(x)<0:
        return f'-{f(x[1:])}'
    if len(x)==1:
        return x
    else:
        return f'{f(x[1:])}{x[0]}'
x=input()
print(f(x))
