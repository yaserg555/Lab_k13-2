# https://www.codewars.com/users/VDblue
# @Masinfuture002_bot

  #1
def privet(a,b):
    return f'Добрий день,{a} {b}'
print(privet('Володимир','Донських'))

  #2
x=float(input())
y=float(input())
z=float(input())
print(f'{x!=y and y!=z and z!=x}')

  #3
def check(a,b,e:int =10):
    return f"%.{e}f"%a ==f"%.{e}f"%b
print(check(1.23,1.23,30))

  #4
def check(a:list,b=list):
    return a[0]/b[0] == a[1]/b[1] ==a[2]/b[2]
print('введи через запятую коефициэнты прямой 1')
x=str(input())
x=x.split(',')
x=list(map(lambda x:float(x),x))
print('введи через запятую коефициэнты прямой 2')
y=str(input())
y=y.split(',')
y=list(map(lambda y:float(y),y))
print(check(x,y))
