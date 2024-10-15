from math import sin
from math import pi
import numpy as np
# --example--
# print(sin(0))
# >>> 0
# ----------
def integral(f=sin, a=0, b=1, N=100):
    N=int(N)
    h = (b - a) / N
    sum = 0
    for k in range( 1, N + 1):
        sum = sum + f(a + (k - 1) * h) + f(a + k * h)
    answer = (h / 2) * sum
    return answer

def func_test_1(x):
    y = 4 / (1 + x ** 2)
    return y

def func_test_2(x):
    y = pi ** (1 / 2) * np.exp(-x ** 2)
    return y

prm = np.array([[0, pi / 2, 50],
               [0, 1, 100],
               [-100, 100, 1000]])
f = [sin, func_test_1, func_test_2]

for i in range(prm.shape[0]):
    a, b, N = prm[i, :]
    print(integral(f=f[i], a=a, b=b, N=N))


