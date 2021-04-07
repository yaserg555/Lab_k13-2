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
