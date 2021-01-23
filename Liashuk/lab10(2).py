def exercise1(a,b):
    string='Індекс елемента: '
    for i in range(0,len(a)):
        if a[i]==b:
            string+=str(i)+','
    a.append(b)
    return a if string=='Індекс елемента: ' else string[:-1]
print(exercise1(  [2,3,4,2,2]    , 3   ))

def exercise2(a):
    k=0
    if a[0]<a[1]:
        k+=1
    elif a[-1]<a[-2]:
        k+=1
    for i in range(1,len(a)-1):
        if a[i]<a[i+1] and a[i]<a[i-1]:
            k+=1
    return k
print(exercise2([43,5,3,12,1]))

def exercise3(a):
    for i in range(len(a)):
        if a[i]<0:
            a[i]=-1
    return a
print(exercise3([-1,0,1,233,-23,-23,-434]))

def exercise4(a):
    arr=a[:-1]
    arr.insert(0,a[len(a)-1])
    return arr
print(exercise4([1,2,34,46,76,3,4,0]))

def exercise5(a,b):
    return [i for i in a if i!=b]
print(exercise5([0,1,23,0,34,-12,0,-4,0,0,0,0],0))

def exercise6():
    return [i for i in range(100) if i%2!=0 and i%3!=0 and i%5!=0]
print(exercise6())

def exercise7(a,b):
    arr=[]
    for i in range(len(a)):
        if a[i]==b:
            arr.append(i)
    return arr
print(exercise7([23,34,23,3,43,23,1,23,1],23))

def exercise8(a):
    arr=[i for i in a if i>0]
    return len(arr)
print(exercise8([23,-2,23,-3,43,5,1,-2]))
