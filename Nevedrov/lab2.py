#1
print('''                                        
Виконавець: Нєвєдров
            Олексій
            Дмитрович
     Група: К-13(2)
     ''')
def cout(a, b):
    print(str(a)+'='+str(b))
    print('type'+' '+str(a)+'='+str(type(b)))


#2
cout('2*4%7',2*4%7)
cout('2*(4%7)', 2*(4%7))
cout('51//6%7', 51//6%7 )
cout('51//(6%7)', 51//(6%7))
cout('(-3+5)*(2%7//3+4*2)', (-3+5)*(2%7//3+4*2))
cout('(3//5.0)*20+32.0', (3//5.0)*20+32.0)
cout('float(int(1.56))', float(int(1.56)))
cout('bool(-0.0)', bool(-0.0))
cout('''float('inf')''', float('inf'))
cout('int(bool(13.56))', int(bool(13.56)))
print('\n')
#3
v = int(input('Введите число:'))
print(v % 100 % 10)
print(v % 2)
#4
print('\n')
cout('10.001^ 345 *13.001^249 / (9.001^355 * 11.001^269)', ((10.001/9.001)**345)/(9.001**10)*(13.001**249)/(11.001**269))