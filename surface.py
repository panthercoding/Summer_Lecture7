import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d

#Building the 3D space
fig = plt.figure()
ax = plt.axes(projection="3d")

#Generating (x,y,z) coordinates
def f(x,y):
	return(np.array(x**2+y**2))

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)

#Plotting the Surface Plot
ax.plot_surface(X,Y,Z,cmap="viridis")

#Axis Labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Surface Map of f(x,y)=x^2+y^2")
plt.show()