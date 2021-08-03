import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
#sns.set()

#Building the 3D space
fig = plt.figure()
ax = plt.axes(projection="3d")

#Generating (x,y,z) coordinates
def f(x,y):
	return(np.array(x**2+y**2))

x = np.random.uniform(-1,1,1000)
y = np.random.uniform(-1,1,1000)
z = f(x,y)
ax.scatter(x,y,z,c=z,linewidth=0.5)

#Saving out the Image
#plt.savefig("./functionplot.jpg")

#Displaying the Image
plt.show()
