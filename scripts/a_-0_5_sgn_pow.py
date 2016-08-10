#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

c = -0.5
x = np.linspace(0.1, 3, 1000)
y1 = np.power(x, c) * np.sign(c)
plt.plot(x, y1)

x2 = np.linspace(0.1, 0.9, 1000)
y2 = np.power(np.sign(c) * x2, 1 / c) * np.sign(c)
#plt.plot(x2, y2)

x3 = np.linspace(0.1, 0.9, 1000)
y3 = np.log(np.abs(c)) / np.log(x3)
plt.plot(x3, y3)
x3 = np.linspace(1.1, 10, 1000)
y3 = np.log(np.abs(c)) / np.log(x3)
plt.plot(x3, y3, color='green')

plt.plot(x, x, color='red')
plt.axis('equal')
#plt.axis([-2, 2, 0, 4])
plt.savefig("a_0_5_sgn_pow.pdf", bbox_inches="tight")
