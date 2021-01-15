# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 08:42:10 2020

@author: Chintu
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,5,4,2,6]
plt.plot(x,y,color='green',linestyle='dashed',linewidth=2,
         marker='*',markerfacecolor='blue',markersize=10)
plt.xlim(1,7)
plt.ylim(1,7)

plt.xlabel('x - label')
plt.ylabel('y - label')

plt.title('Customization')

plt.show()