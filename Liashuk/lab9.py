def a_9(a):
    try:
        b=int(input('Введи ціле число: '))
        a.append(b)
    except ValueError:
        a=a
    return a

def b_9(a):
    try:
        b=int(input('Введи ціле число: '))
        a.append(b)
    except ValueError:
        a.clear()
    return a

def a_12(a):
    b=input('vvedy chyslo: ')
    try:
        s=''
        for i in range(0,len(a)):
            if str(a[i])==b:
                s+=str(i) + ';'      # Утворює строкуз індексів
        res=list(s)
        res.pop(len(res)-1)    # IndexError     # Видаляє останній елемент (;) з списка res
        resultat=f"Елемент {b} знаходиться під індексом: {''.join(res)}"
    except IndexError:
        a.append(b)
        resultat=a
    return resultat


def a1_13(n):
    b=input('Введи ціле число: ')
    return a1_13(n-1) if int(b) and n>1 else None

def a2_13(n):
    try:
        a1_13(n)
    except ValueError:
        print('*** ValueError')



print('*** Завдання № 9(а)')
print(a_9([32,34,345,6,7,6]))
print('*** Завдання № 9(б)')
print(b_9([32,34,345,6,7,6]))


print('*** Завдання № 12')
print(a_12([32,32,5,23,'ds',320,0,0,0,'sds',0,'32',0,00,0,0,32]))

print('*** Завдання № 13')
print(a2_13(6))
