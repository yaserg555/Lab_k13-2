import numpy as np
import scipy.linalg as la
n = 4
D = np.zeros((n,n,), dtype = np.int64)
D

D.T[0] = 1
D

for i in range(1,n):
    for j in range(1,i+1):
        D[i,j] = -D[i,j-1]*(i-j+1)//j
D

D=np.matrix(D)
D = D*D

E = np.zeros((n,n), dtype = np.int64)
for i in range(n):
    E[i][i] = 1
E

E == D

I = la.inv(D)
I

(I == D).all()

I is D
