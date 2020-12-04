def task1():
    list1 = [1, 5, 87, 32]
    list1[1] = 13
    list1.append(25)
    list1[1] = [4, 5]
    list1.pop(4)
    list1.pop(3)
    list1[2] = 8
    tuple1 = tuple(list1)
    print(tuple1)
    list1.append(tuple1)
    list1.pop(-1)
    print(list1)
    print(tuple1[::-1])


def task2():
    list1 = []
    for i in range(2, 20):
        list1.append(i)
    print(list1[3:9])

def task3():
    def function(element, list):
        for i in list:
            if i != element:
                x = 1
            else:
                x *= 0
                element = i
        if x == 1:
            list.append(element)
        return list.index(element)


def task4():
    def minus_one(list):
        for i in range(len(list)):
            if list[i] < 0:
                list[i] = -1


def task5():
    def del_minus(list):
        for i in list:
            if i == 0:
                list.remove(i)
        return list


def task6():
    def sum(list):
        sum = 0
        for i in range(len(list)):
            if list[i]%2 == 0:
                sum += list[i]
        return sum


def task7():
    def seems_seq(seq1, seq2):
        res = True
        for it in seq1:
            if it not in seq2:
                res = False
                break
        for it in seq2:
            if it not in seq1:
                res = False
                break
        return res


def task9():
    def seems_element(seq):
        list1 = []
        for i in range(len(seq)):
            if seq.count(i) > 1:
                list1.append(i)
        return list1
