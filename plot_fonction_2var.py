import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# %matplotlib notebook

# def la foction
def fonction1 (x, y):
    return 2*x**2 - x*y**2 + 2*y**2

# np.linspace(borne_inf, borne_sup, npPts)
x = np.linspace(-40, 40, 300)
y = np.linspace(-40, 40, 300)

# make a grid with R groups
X, Y = np.meshgrid(x, y)

Z = fonction1(X,Y)
fig = plt.figure(figsize = (50,30))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='cool')
ax.set_title("Surface Bonus", fontsize = 13)
ax.set_xlabel('x', fontsize = 11)
ax.set_ylabel('y', fontsize = 11)
ax.set_zlabel('Z', fontsize = 11)

plt.show()