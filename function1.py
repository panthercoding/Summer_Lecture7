#Python Libraries
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
sns.set()

#Building the Graph
x = np.linspace(0,20,1000)
y = np.power(x,2)

#Setting Limits
#plt.xlim(0,5)
#plt.ylim(0,40)

#Plotting the Graph
plt.plot(x,y)
plt.show()