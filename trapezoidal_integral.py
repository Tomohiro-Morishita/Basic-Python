from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# ----------
a = 0
b = (1 / 2) * pi
N = 100
h = ( b - a) / N
sum = 0
for k in range( 1, N):
    sum = sum + sin(a + (k - 1) * h) + sin(a + k * h)
answer = (h / 2) * sum
print(answer)
