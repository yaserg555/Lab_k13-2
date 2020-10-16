>>> def periimeter_triangle(a,b,c):
	return a+b+c

>>> def coordinates (x,y):
	return '''A[x,y]'''
#6
a=int(input())
b=int(input())
c=int(input())
if a+b==c or a+c==b or b+c==a:
	print ('yes')
