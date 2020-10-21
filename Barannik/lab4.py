#1
name=input("Введіть ваше ім'я ")
lastname=input("Введіть ваше прізвище ")
def vitannya(name, lastname):
    return f"Вітаємо, {name} {lastname}"
print(vitannya(name, lastname))

#2
x!=y and x!=z and y!=z

#3
def rivni(x, y):
    return x==y

#4
def nuli(b1,b2):
    return b1==0 and b1==b2
def kut(a1, b1, a2, b2):
    return b1!=0 and b2!=0 and (a1/b1)==(a2/b2)
def kolinearni(a1, b1, c1, a2, b2, c2):
    return nuli(b1, b2) or kut(a1, b1, a2, b2)
