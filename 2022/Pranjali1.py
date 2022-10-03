import matplotlib.pyplot as plt
col=[8000,12000,9800,11200,15500,7300]
section=['A','B','C','D','E','F']
plt.title("Volunteering week collection")
plt.axis("equal")
plt.pie(col,labels=section,autopct="%5.2f%%")
plt.show()
