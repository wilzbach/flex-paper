#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 7, 1000)
plt.plot(x, np.log(x))
x2 = np.linspace(-7, 7, 1000)
plt.plot(x2, np.exp(x2))
x3 = np.linspace(-10, 10, 1000)
plt.plot(x3, x3)
plt.axis('equal')
plt.axis([-5, 5, -5, 5])
plt.savefig("log_exp.pdf", bbox_inches="tight")
