import matplotlib as mpl
import matplotlib.pyplot as plt
from SimReacteur import z, C

x = z

y = C

for i in range(len(C)):

    plt.plot(x, y[:,i])
    
    
plt.show