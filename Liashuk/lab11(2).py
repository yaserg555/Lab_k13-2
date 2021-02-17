import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3 + 2*x**2 - 3*x - 2) / (x**2 + x - 2)

x = np.linspace(-4, 4, 500)
A = f(x)
plt.figure(figsize = (17,12), dpi = 80)

A[A > 100] = np.inf
A[A < -100] = -np.inf

sp = plt.subplot(224)
sp.spines['left'].set_position('center')
sp.spines['right'].set_position('center')
sp.spines['bottom'].set_position('center')
sp.spines['top'].set_position('center')


plt.plot(x,A, label = r'$f_1=\ (x^3 + 2x^2 - 3x - 2)/(x^2 + x - 2)$', color = 'red')
plt.plot([-2,-2],[-10,10],[1,1],[-10,10], color = 'blue', linestyle = '--')


plt.ylim((-10,10))
plt.show()

