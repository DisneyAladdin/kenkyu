#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

plt.plot( [3,1,4,1,5,9,2,6,5], label = "Data 1")
plt.plot( [3,5,8,9,7,9,3,2,3], label = "Data 2")
plt.legend() # 凡例を表示

plt.title("Graph Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
