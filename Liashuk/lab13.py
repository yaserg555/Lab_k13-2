# Nomer 1

def loose_change(cents):
    copy = cents; arr = []
    if cents > 0:
        for i in {25, 10, 5, 1}:
            K = cents // i
            arr.append(K)
            cents -= K*i
    else:
        arr = [0,0,0,0]
    return  {'Nickels': arr[2], 'Pennies': arr[3], 'Dimes': arr[1], 'Quarters': arr[0]}
# Nomer 2

def grabscrab(word, possible_words):
    list_1 = [] # creating an empty list
    arr = (chr(i) for i in range(ord('a'), ord('z') + 1))
    di = dict.fromkeys(arr, 0)   # creating a dictionary of letters
    basic_dictionary = di.copy() # creating a dictionary with a copy
    for i in word:
        basic_dictionary[i] += 1
    for i in possible_words: # main cycle
        for j in i:
            di[j] += 1
        if di == basic_dictionary:
            list_1.append(i)
        for j in i:
            di[j] -= 1
    return list_1

# 2 variant rozvyzku

from collections import Counter
def grabscrab(word, possible_words):
    return [i for i in possible_words if Counter(word) == Counter(i)]

# Nomer 3 

def f(x):
    y = x // 2
    return [i for i in range(2,y+1) if x%i == 0]


def factorsRange(n, m):
    k = dict()
    for i in range(n, m+1):
        if f(i) == []:
            k[i] = ['None']
        else:
            k[i] = f(i)
    return k
    
