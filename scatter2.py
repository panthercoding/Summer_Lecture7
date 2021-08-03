#Python Libraries
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,10,30)
y1 = np.sin(x)
y2 = np.cos(x)

#Without Legend
#plt.scatter(x,y1,marker="o",c="red",s=40,alpha=0.5)
#plt.scatter(x,y2,marker="o",c="purple",s=40,alpha=0.5)

#With Legend
#plt.scatter(x,y1,marker="o",c="red",s=40,alpha=0.5)
#plt.scatter(x,y2,marker="o",c="purple",s=40,alpha=0.5)

plt.show()