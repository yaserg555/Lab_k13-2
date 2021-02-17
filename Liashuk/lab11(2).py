

minimum = np.min(array, axis = 1)
maxymum = np.max(array, axis = 0)
for i in range(n):
    for j in range(m):
        if (minimum[i] == maxymum[j]):
            print(f'{minimum[i]} ---> {(i,j)}')
