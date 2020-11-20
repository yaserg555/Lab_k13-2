print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ Завдання № 4 ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
def f(a):
    s=''
    while a>0:
        b=a%10
        s=str(b**2)+s
        a=a//10
    return s if a>=0 else False
f(12304)
