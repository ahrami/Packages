import matplotlib.pyplot as plt
from math import *

def foo(t: float) -> float:
    return atan(-0.0012*t**3 + 0.4* t**2+ 0.616*t + 6120) + 0.65*sin(0.24*t + 1.23) - 0.27*cos(0.21*t - 0.17) - (sin(0.34*t + 0.16))/(1 + 0.03*(t - 370.5)**2)

x = range(0, 1000)
y = [foo(t) for t in x]
plt.plot(x, [0]*len(x))
plt.plot(x, y)

for t in x[1:]:
    if y[t] <= 0:
        if y[t - 1] > 0:
            plt.plot(t, 0, '*')
            print(t)
    elif y[t - 1] <= 0:
        plt.plot(t, 0, '*')
        print(t)


a = 0
b = len(x) - 1
while abs(a - b) > 1:
    c = a - (a-b)//2
    if y[a]*y[c] < 0:
        b = c
    else:
        a = c
print(b)
plt.show()

