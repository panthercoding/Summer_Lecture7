import matplotlib.pyplot as plt 
import numpy as np 
#import seaborn as sns
#sns.set()

quarters = [1,2,3,4]
sfpoints = [7,27,34,37]
gbpoints = [0,0,7,20]

plt.plot(quarters,sfpoints,color="red",label="SF")
plt.plot(quarters,gbpoints,color="Green",label="GB")

plt.title("NFC San Francisco vs Green Bay",fontsize=16)

plt.xlabel("Game Quarter",fontsize=16)
plt.ylabel("Cumulative SCore",fontsize=16)

plt.xticks(np.arange(1,4+1,step=1))
plt.tick_params(labelsize=14)

plt.legend()

plt.show()