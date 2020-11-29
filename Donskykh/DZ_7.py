def f3_7(n):
    n=str(n)
    check={1,3,5,7,9}
    return 0 < sum([str(i) in n for i in check])

  
def f4_7(a,b,e=1):
    from math import sin as sin, cos as cos, log as ln
    mx=sin(cos(13*a))+cos(ln(a))
    for i in range(int(a*10**e),int(b*10**e)):
        if mx<sin(cos(13*(i/10**e)))+cos(ln(i/10**e)):
            mx=sin(cos(13*(i/10**e)))+cos(ln(i/10**e))
    return mx
# print(f4_7(0.5,2,3))
#x=0.967  (максимум на 0.5,2)
#y=1.8409...
#а прога выдпаёт 1.8409022190746536, что оч похоже



def fib(m):
    a1,a2=1,1
    while a2<m:
        temp=a2
        a2=a2+a1
        a1=temp
    return a2
