#2
def check_mod(x):
    return {
        x <= -1 : -1,
        x == 0 : 0,
        x >= 1 : 1
    }[True]

#4
def kirbich(x,y,a,b,c):
    import itertools
    return 0<sum(list(map(lambda a: a[0]<=x and a[1]<=y,list(itertools.permutations([a,b,c],2)))))

