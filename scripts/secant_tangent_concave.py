# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

l = 0.5
r = 1.5
lw = 3
x = np.linspace(l, r, 1000)
f = lambda x: np.sin(x)
y = f(x)
plt.plot(x, y, color='black', linewidth=lw)
# plt.text(1.05, 0.9, '$f(x)$')

# secant
b = (f(r) - f(l)) / (r - l)
y = f(l) + b * (x - l)
plt.plot(x, y, color='blue', linestyle="dotted", linewidth=lw)
# plt.text(1.4, 0.92, '$s$')

# tangent
f1 = lambda x: np.cos(x)
y = f(l) + f1(l) * (x - l)
plt.plot(x, y, color='orange', linestyle="dashed", linewidth=lw)
# plt.text(0.55, 0.9, '$t_l$')

y = f(r) + f1(r) * (x - r)
plt.plot(x, y, color='red', linestyle='dashed', linewidth=lw)
# plt.text(1.4, 1.3, '$t_r$')

plt.axes().get_xaxis().set_ticklabels([])
plt.axes().get_yaxis().set_ticklabels([])
plt.xlim(l, r)
plt.savefig("tangent_secant_concave.pdf", bbox_inches="tight")
