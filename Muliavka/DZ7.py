# 1


def has_odd_num(n):
	s = str(n)
	return '1' in s or '3' in s or '5' in s or '7' in s or '9' in s


# 3

def first_fibonacci_after(n):
	f, f1 = 1, 0
	while n >= f:
		f, f1 = f + f1, f
	return f
