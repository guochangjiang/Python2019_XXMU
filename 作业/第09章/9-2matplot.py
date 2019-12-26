import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,20,1000)
y=np.cos(x)
plt.plot(x,y,'k',color='r',linewidth=3,linestyle='-')
plt.show()
