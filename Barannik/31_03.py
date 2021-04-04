#1
def file_to_list_of_couples(fname) :
    couples = []
    with open( fname, 'r', encoding = 'utf- 8') as f:
        data = f.readlines()
        for row in data:
            n = ''
            for i in row.strip():
                if i.isdigit():
                    n += i
                else :
                    n1 = n
                    n = ''
            n2 = n
            if n1.isdigit() and n2.isdigit():
                couples.append((int(n1) , int(n2)))            
    return couples
print(file_to_list_of_couples('1.txt'))

#2
def row_count(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        n = 0
        for row in f:
            n += 1
    return n
print (row_count('1.txt'))
