# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 08:25:27 2020

@author: Chintu
"""

import matplotlib.pyplot as plt
x=[3,5,4,7]
y=[5,7,4,9]
plt.plot(x,y,label="line 1")
plt.xlabel("x - label")
plt.ylabel("y - label")
plt.title("Two lines on same graph")


x2=[8,4,6,3]
y2=[5,7,3,4]
plt.plot(x2,y2,label="line 2")

plt.legend()
plt.show()