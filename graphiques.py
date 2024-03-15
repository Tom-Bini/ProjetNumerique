import matplotlib as mpl
import matplotlib.pyplot as plt
from SimReacteur import z, C
import numpy as np

x = z

y = np.transpose(C)

plt.plot(x, y[:, 0], label="Concentration CH4")
plt.plot(x, y[:, 1], label="Concentration H2O")
plt.plot(x, y[:, 2], label="Concentration H2")
plt.plot(x, y[:, 3], label="Concentration CO")
plt.plot(x, y[:, 4], label="Concentration CO2")

plt.legend()
plt.title('Graphique des concentrations')
    
    
plt.show()