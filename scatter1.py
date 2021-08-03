#Python Libraries
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
sns.set()

N = 100 #100 points
x = 0.8*np.random.rand(N)
y = 0.8*np.random.rand(N)

#plt.scatter(x,y)
#plt.scatter(x,y,marker="^")
#plt.scatter(x,y,s=100,marker="o",c=np.random.rand(N))
plt.show()