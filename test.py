from optimisation import FonctionDeUs
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.arange(0.0000001, 0.0001001, 0.0000001)
y = np.zeros(1000)

for i in range(1000):
    y[i] = FonctionDeUs(i)
    
plt.plot(x, y)
plt.xlim(0,0.000001)
plt.show