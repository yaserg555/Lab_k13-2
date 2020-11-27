#3
l_3=[ i**2 for i in range(1,11)]

#4
l_4 =[ 1**2 for i in range(10, -1,-1)]

#7
def f_7(l_7):
    if l_7 == []:
        return 'Послідовність порожня'
    l = [str(i) for i in l_7]
    s = ', '.join(l)+'.'
    return s

#19
def f_19(l_19):
    l = l_19
    l.insert(0, l[len(l)-1])
    l.pop(len(l)-1)
    return l

#20
def f_20(l_20):
    l = l_20
    l.insert(len(l), l[0])
    l.pop(0)
    return l

#28
def f_28(l_28):
    s = 0
    for i in range(0,len(l_28)):
        if l_28[i]%2 == 0:
            s += l_28[i]
    return s

#35
def f_35(l_1, l_2):
    x = set(l_1)
    y = set(l_2)
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    return x == y

#41
   '''?????????????????'''     

#50
def f_50(l_50):
    l = []
    while len(l_50)>0:
        i = l_50[0]
        if l_50.count(i) > 1:
            l.append(i)
        while l_50.count(i) > 0:
            l.remove(i)
    return l
