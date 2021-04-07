import os
import random
with open('file.txt', 'w', encoding = "UTF-8") as file:
    file_size = os.stat('file.txt').st_size
    while file_size < 100000:              # створює файл поки його розмір не буде більший за 100_000 Байт
        a = random.uniform(-1000, 1000)
        b = random.uniform(-1000, 1000)
        file.write(f'{a} {b}\n')
        file_size = os.stat('file.txt').st_size

with open('file.txt', 'r', encoding = "UTF-8") as file:
    print(file.read())

# №1 
with open('file.txt', 'r', encoding = "UTF-8") as file:
    arr = [(float(i.split()[0]), float(i.split()[1])) for i in a]
    print(arr)

# №2
with open('file.txt', 'r', encoding = "UTF-8") as file:
    for i in enumerate(file, 1):
        pass
    print(int(i[0]))
# №3
class Refrigerator:

    def __init__(self, a='немає', b='а', c='немає', d='а', dict_1={1: 'PTE', 2: 'PTH', 3: 'GTE', 4: 'GTH'}):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.dict_1 = dict_1

    def put_the_elephant(self):
        if (self.a == 'немає') and (self.c == 'немає'):
            self.a = 'є'
            self.b = ''
        elif self.a == 'є':
            print('У холодильнику уже є слон!!!')
        else:
            print('У холодильнику вже є бегемот!!!')

    def put_the_hippopotamus(self):
        if (self.a == 'немає') and (self.c == 'немає'):
            self.c = 'є'
            self.d = ''
        elif self.c == 'є':
            print('У холодильнику уже є бегемот!!!\n')
        else:
            print('У холодильнику вже є слон!!!\n')

    def get_the_elephant(self):
        if self.a == 'є':
            self.a = 'немає'
            self.b = 'а'
        elif self.a == 'немає':
            print('У холодильнику немає слона!!!\n')

    def get_the_hippopotamus(self):
        if self.c == 'є':
            self.c = 'немає'
            self.d = 'а'
        elif self.c == 'немає':
            print('У холодильнику немає бегемота!!!\n')

    def output(self):
        print(f"{self.dict_1[1]}: put_the_elephant\n"
              f"{self.dict_1[2]}: put_the_hippopotamus\n"
              f"{self.dict_1[3]}: get_the_elephant\n"
              f"{self.dict_1[4]}: get_the_hippopotamus")
        print(f"У холодильнуку {self.a} слон{self.b}.")
        print(f"У холодильнуку {self.c} бегемот{self.d}.")

    def resultat(self):
        Refrigerator.output(self)
        str_1 = input('Enter: ')
        if str_1 == self.dict_1[1]:
            Refrigerator.put_the_elephant(self)
        elif str_1 == self.dict_1[2]:
            Refrigerator.put_the_hippopotamus(self)
        elif str_1 == self.dict_1[3]:
            Refrigerator.get_the_elephant(self)
        elif str_1 == self.dict_1[4]:
            Refrigerator.get_the_hippopotamus(self)
        else:
            print("Команди не знайдено!!!\n")



obj = Refrigerator()
k = 0
while k < 3:
    obj.resultat()
    k += 1
    
    
