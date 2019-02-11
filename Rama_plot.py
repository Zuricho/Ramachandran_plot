#!/usr/bin/python2

"""
Created on Wed Feb 11 12:40:00 2019
@author: Zuricho
"""


import matplotlib.pyplot as plt
import numpy as np


phi_psi_list = np.loadtxt("phi_psi.txt")


plt.figure(1, figsize=(3, 3))

# plot function
plt.scatter(phi_psi_list[:,0], phi_psi_list[:,1],
            s=2, color = "red", marker=".",)

# set the plot title
plt.title('Ramachandran Plot of PTR')

# set the limitation of axes
plt.xlim((-180, 180))
plt.ylim((-180, 180))

# set the name of axes
plt.xlabel('phi')
plt.ylabel('psi')

# set the tags of axes
plt.xticks(np.arange(-180, 180, step=60))
plt.yticks(np.arange(-180, 180, step=60))

# set grid
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()