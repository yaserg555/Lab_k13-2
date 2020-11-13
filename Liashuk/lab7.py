print("""
***♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠***
                                 ЗАВДАННЯ №1
""")
def neparne_chyslo_1():
    try:
        x=input('Введи число для першого завдання: ')
        x=int(x)
        return x
    except ValueError:
        return None

def neparne_chyslo_2():
    q=neparne_chyslo_1()
    if q==None:
        print('Error in the ValueError')
    else:
        while q>0:
            a1=q%10
            if a1%2==1:
                print('True')
                break
            q=q//10
        else:
            print('False')

def neparne_chyslo_3():
    try:
        neparne_chyslo_2()
    except KeyboardInterrupt:
        print('Error in the KeyboardInterrupt')
neparne_chyslo_3()
print("""
***♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠***
                                 ЗАВДАННЯ №2
""")
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def qwe(m):
    m=float(m)
    n=1
    if m>=0:
        while m>=fibonacci(n):
            n+=1
        return fibonacci(n)
    else: return None

def qwe1():
    try:
        q=qwe(input('Введи число для другого завдання: '))
        if q==None:
            print(0)
        else:
            print(q)
    except ValueError:
        print('Error in the ValueError')
    except KeyboardInterrupt:
        print('Error in the KeyboardInterrupt')
qwe1()
