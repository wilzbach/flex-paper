#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

c = 2
x = np.linspace(0, 3, 1000)
y1 = np.power(x, c) * np.sign(c)
plt.plot(x, y1)
x2 = np.linspace(0.001, 3, 1000)
y2 = np.power(np.sign(c) * x2, 1 / c) * np.sign(c)
plt.plot(x2, y2)
plt.plot(x, x, color='red')
plt.axis('equal')
plt.axis([0, 2, 0, 2])
plt.savefig("a_2_sgn_pow.pdf", bbox_inches="tight")
