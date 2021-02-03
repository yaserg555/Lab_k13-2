import numpy as np
#1
def indline(i,j,n,m):
    '''(i, j) is index,
    (n, m) is shape'''
    return i*m+j

#2
def index(x, n, m):
    '''x is lineindex,
    (n, m) is shape'''
    i = x // m
    j = x % m
    return [i, j]

#3
def spiral(a):
    l = []
    while a.size > 0:
        l += list(a[0,:]) + list(a[1:,-1]) + list(a[-1,-2::-1]) + list(a[-2:0:-1,0])
        a = a[1:-1,1:-1]
    return b

#4
def snake(a):
    n = a.shape[0]
    l = np.array(a[0,n-1])
    i = 1
    j = n-1
    while j > 0 and i != j:
        while i > -1:
            l = np.hstack((l, a[i, j]))
            i += -1
            j +=-1
        i += 1
        while j < n and j > 0:
            l = np.hstack((l, a[i, j]))
            i += 1
            j += 1
        j += -1
    return l
