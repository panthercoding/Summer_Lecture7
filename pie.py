import matplotlib.pyplot as plt 
labels = "Gaming","Gaming But in Orange"
sizes = [290,70]

fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,autopct='%1.1f%%',
	textprops={'fontsize':16})

ax1.axis('title')
plt.title("How I Spent Quarantine",fontsize=18)
plt.show()

