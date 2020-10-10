print('Andrii')

print("Указати значення виразів мови Pyhton та їх типи:\n\n а) 9/5, (-9)/5, 9/(-5), (-9)/(-5)\nВІДПОВІДЬ:")
print("9/5 =",9/5,"               Type of result:",type(9/5))
print("(-9)/5 =",-9/5,"           Type of result:",type(-9/5))
print("9/(-5) =",9/-5,"           Type of result:",type(9/-5))
print("(-9)/(-5) =",-9/-5,"         Type of result:",type(-9/-5))

print("\n б) 9//5, (-9)//5, 9//(-5), (-9)//(-5)\nВІДПОВІДЬ:")
print("9//5 =",9//5,"               Type of result:",type(9//5))
print("(-9)//5 =",-9//5,"           Type of result:",type(-9//5))
print("9//(-5) =",9//-5,"           Type of result:",type(9//-5))
print("(-9)//(-5) =",-9//-5,"         Type of result:",type(-9//-5))

print("\n в) 9%5; (-9)%5, 9%(-5), (-9)%(-5)\nВІДПОВІДЬ:")
print("9%5 =",9%5,"             Type of result:",type(9%5))
print("(-9)%5 =",-9%5,"           Type of result:",type(-9%5))
print("9%(-5) =",9%-5,"           Type of result:",type(9%-5))
print("(-9)%(-5) =",-9%-5,"         Type of result:",type(-9%-5))

print("\n г) 9.0/5.0, 9.0//5.0, 1.5//0.75\nВІДПОВІДЬ:")
print("9.0/5.0 =",9.0/5.0,"          Type of result:",type(9.0/5.0))
print("9.0//5.0 =",9.0//5.0,"         Type of result:",type(9.0//5.0))
print("1.5//0.75 =",1.5//0.75,"        Type of result:",type(1.5//0.75))

print("\n Обчислити вираз а) √2, б)3^1.5\nВІДПОВІДЬ:\n a) √2 =" + str(round(2**(1/2),5))+"\n б) 3^1.5 =" + str(round(3**1.5,5)))
print("\n Обчислити вираз а) √2, б)3^1.5\nВІДПОВІДЬ:\n a) √2 =" + str(2**(1/2))+"\n б) 3^1.5 =" + str(3**1.5))

a=input('Хочеш перевести число у двійкову систему числення?(Yes;No)  ')
if a=="No":
    a=input('Хочеш перевести число у вісімкову систему числення?(Yes;No)  ')
    if a=="No":
        a=input('Хочеш перевести число у шістьнадцякову систему числення?(Yes;No)  ')
        if a=="No":
            print('Програма завершина!!!')
        else:
            if a=="Yes":
                a=input("Введи число:  ")
                print(hex(int(a)))
            else:
                print("Ви ввели неправильні дані!!!")
    else:
        if a=="Yes":
            a=input('Введи число:  ')
            print(oct(int(a)))
        else:
                print("Ви ввели неправильні дані!!!")

else:
    if a=="Yes":
            a=input('Введи число:  ')
            print(bin(int(a)))
    else:
                print("Ви ввели неправильні дані!!!")
