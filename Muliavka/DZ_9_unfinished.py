# 6

s_1 = s[:(len(s) + 1) // 2]
s_2 = s[:len(s) // 2]
s_3 = s[:(len(s) + 2) // 3]
s_4 = s[len(s) // 2:]
s_5 = s[(len(s) + 1) // 2:]
s_6 = s[(len(s) + 2) // 3:(-len(s) + 2) // 3]
s_7 = s[:10]
s_8 = s[:10][::-1]
s_9 = s[2::3]
s_10 = s[2::3][::-1]

# 7

def f_7(s):
    if s == []:
        return 'Sequence is empty.'
    return ','.join(s) + '.'

# 13

def f_13(n):
    s = []
    for _ in range(n):
        try:
            a = int(input())
            if a in s:
                raise RuntimeError
            s.append(a)
        except:
            raise RuntimeError
    return s

# 16

def f_16(s, el):
    return [i for i in range(len(s)) if s[i] == el]

# 22

def f_22(s):
    s = [a for a in s if a > 0]
    if s == []:
        return "There isn't any positive integer."
    return min(s)

# 27

def f_27(s):
    condition = True
    return [a for a in s if condition]

# 33

def f_33(s1, s2):
    return s1 + s2

# 43

def f_43(l):
    s = l.split()
    if int(s[0]) % 4:
        february = 28
    else:
        february = 29
    months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = int(s[1])
    month = 0
    while day > months[month]:
        day -= months[month]
        month += 1
    return f'{day} {month + 1}'

# 49

def f_49(s):
    result = []
    for a in s:
        if a not in result:
            result.append(a)
    return result
