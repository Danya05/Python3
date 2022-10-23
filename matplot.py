import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

x1 = np.array([5, 10, 15, 20, 25, 28, 30, 33, 35, 37])
x = np.array([i*i for i in x1])
y1 = np.array([2.6454, 1.943, 1.6904, 1.5782, 1.5348, 1.5272, 1.5268, 1.5322, 1.5416, 1.5492])
y = np.array([y1[i]*y1[i]*x[i] for i in range(len(x))])
plt.title(r'$\Omega(M)$')
plt.minorticks_on()
x_new = np.linspace(x.min(), x.max(), 200)
spl = make_interp_spline(x, y, k = 3)
y_new = spl(x_new)
plt.plot(x_new, y_new)
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.xlabel(r'$a^{2}$, $см^2$')
plt.ylabel(r'$t^{2}a*10^{2}$, $c^2*см$')
t = np.arange(0,1400)
plt.plot(t, 2.2*t + 150)
plt.tight_layout()
plt.show()
