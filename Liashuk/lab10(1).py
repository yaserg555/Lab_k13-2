def exercise2(a):
    b=a.copy()
    c=a.copy()
    a.sort(reverse=True)
    b.sort(reverse=False)
    return c==a or c==b

print(exercise2([12,46,45]))

def exercise3(a):
    sum=0
    k=0
    for i in range(0,len(a)):
        if a[i]>=0:
            sum+=i
            k+=1
    return  sum/k if k!=0 else -1
print(exercise3([-23,-34,-54,-34,-2,-3,-23]))

def exercise4(a):
    arr=[i for i in a if i>=0]
    return arr==a
print(exercise4([23,4,6,5,345]))


def exercise5(a):
    arr=[i for i in a if i/7==i//7]
    return arr==a
print(exercise5([7,14,22,28,35]))

def exercise6(a):
    return 7 in a
print(exercise6([14,22,28,35]))

def exercise7(a):
    return [i for i in a if i%2==0]
print(exercise7([14,22,28,35]))

def exercise8(a):
    return sum([i for i in a if i%2==0])
print(exercise8([2,2,21,2]))

def exercise9(a):
    return sum(a[::2])
print(exercise9([2,2,21,1,1,1,10,1,1]))
