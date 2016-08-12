#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import os
from itertools import cycle

scriptDir = os.path.dirname(os.path.realpath(__file__))
x = np.loadtxt(scriptDir + '/hist_values.csv', delimiter=',')

n, bins, patches = plt.hist(x, cumulative=True, normed=True, bins=100, histtype='step')

x = np.linspace(plt.xlim()[0], plt.xlim()[1], 1000)

plt.plot(x, 1 - np.exp(-x))
plt.margins(0, 0.1)

col = cycle(["brown", "orange"])
#points = [0.2, 0.4, 0.6, 0.8, 0.9, 0.95]
points = [0.4, 0.6, 0.9]
for yPoint in points:
    xPoint = - np.log(1 - yPoint)
    c = next(col)
    # vertical
    plt.plot([xPoint, xPoint], [0, yPoint], color=c)
    # horizontal
    plt.plot([0, xPoint], [yPoint, yPoint], color=c)

#plt.axis('equal')
plt.axis([0, 9, 0, 1])
plt.savefig("inversion_sampling.pdf", bbox_inches="tight")
