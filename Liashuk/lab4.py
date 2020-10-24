# №1
def hello(a,b):
    return print(f"Привіт, {a} {b}")

# №2
def rizni():
    x=input("x:  ")
    y=input("y:  ")
    z=input("z:  ")
    return print(x!=y!=z!=x)

# №4
def kof1():
    return (a1==a2 and b1==b2 and c1!=c2)
def kof2():
    return (a1==a2 and b1==b2 and c1==c2)
def kof3():
    return (a1!=a2 and b1!=b2)

print("№1")
hello('Ляшук','Андрій')

print("№2")
rizni()

print("№4")
a1, b1, c1 = int(input("a1: ")), int(input("b1: ")), int(input("c1: "))
a2, b2, c2 = int(input("a2: ")), int(input("b2: ")), int(input("c2: "))
kof1()
kof2()
kof3()
print(f"Колінеарні:{kof1()}")
print(f"Накладаються:{kof2()}")
print(f"Перетинаються:{kof3()}")
