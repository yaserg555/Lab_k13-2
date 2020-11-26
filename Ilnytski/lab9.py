#Task 2
def inner_list():
    l = [i for i in range(2, 20)]
    print(l[3:9])
inner_list()
#Task 7
def wrap(l):
    if (not len(l)):
        print("sequence is empty")
    else:
        for i in range(len(l)):
            l[i] = str(l[i])
        s = ','.join(l)
        print(s + '.')
wrap([1,2,3])
#Task 12
def add_to(l,elem):
    if (elem not in l):
        l.append(elem)
lst = [1,2,3,4]
add_to(lst, 5)
print(lst)
#Task 21
#Task 22
def min_positive(l):
    m = float('inf')
    for i in l:
        if (i < m and i > 0):
            m = i
    return m
print(min_positive([-1,4,-2,4,6,3]))
#Task 25
def avg_positive(l):
    count = 0
    sum = 0
    for key, val in enumerate(l):
        if (val > 0):
            sum += key
            count += 1
    if (not count):
        return -1
    return sum / count
print(avg_positive([1,2,3,4,5]))
#Task 31
binomial = [1]
n = 5
b = 1
k = 0
while k < n:
     b = b*(n-k)//(k+1)
     binomial.append(b)
     k += 1
print(binomial)
#Task 35
set1 = {1}
set2 = {1,1,1,1,1,1,1,1}
print(set1 == set2)
#Task 37
l = [1]
index = 1
while index < len(l) and l[index] >= l[index-1]:
    index += 1
if (index == len(l)):
    print("True")
else:
    print("False")
