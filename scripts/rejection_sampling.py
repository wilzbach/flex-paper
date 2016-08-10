#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi / 2, 1.5 * np.pi, 1000)
plt.plot(x, np.sin(x))
plt.plot(x, np.full(len(x), 1.0))
#plt.margins(0, 0.1)
y2 = np.sign(np.pi / 2 - x) * x / np.pi * 2
y2[x > (np.pi / 2)] += 2
plt.axis([0, np.pi, 0, 1.1])
plt.plot(x, y2)

d = np.zeros(len(x))
y = np.sin(x)
plt.fill_between(x, y, where=y >= d, interpolate=True, color='gray', alpha=0.5)

# random points
n = 20
xs = np.random.uniform(0, np.pi, n)
ys = np.random.uniform(0, 1, n)
mask = np.array([np.sin(x) > y for x, y in zip(xs, ys)])
plt.scatter(xs[mask], ys[mask], color="black")
plt.scatter(xs[~mask], ys[~mask], color='brown')

plt.savefig('rejection_sampling.pdf', bbox_inches="tight")
