#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

n = 4
c = -0.5
x = np.linspace(0.01, n * 2, 1000)
y1 = np.power(x, c) * np.sign(c)
plt.plot(x, y1, color='blue')

# x2 = np.linspace(0.3, 3, 1000)
x2 = np.linspace(-n * 2, -0.3, 1000)
y2 = np.power(np.sign(c) * x2, 1 / c)
plt.plot(x2, y2, color='green')

x3 = np.linspace(-n, n, 1000)
plt.plot(x3, x3, color='red')
plt.axis('equal')
plt.axis([-n, n, -n, n])
plt.savefig("a_0_5_sgn_pow.pdf", bbox_inches="tight")
