import matplotlib as mpl
import matplotlib.pyplot as plt
from SimReacteur import z, C
import numpy as np

x = z #pour avoir la longueur du réacteur en x

y = np.transpose(C) #pour afficher correctement les valeurs

plt.plot(x, y[:,0], label ='Concentration CH4') #affichage des courbes
plt.plot(x, y[:,1], label ='Concentration H2O')
plt.plot(x, y[:,2], label ='Concentration H2')
plt.plot(x, y[:,3], label ='Concentration CO')
plt.plot(x, y[:,4], label ='Concentration CO2')

plt.legend() #affichage légende
plt.title('Graphique des concentrations') #affichage du titre

plt.show() #affichage du graphique 1

fig, ax1 = plt.subplots() #créé une figure et y afficher un axe

ax2 = ax1.twinx() #définition d'un nouvel axe "jumeau" au premier
ax3 = ax2.twinx() #définition d'un nouvel axe "jumeau" au deuxième 

ax1.plot(x, y[:,5], label ='Fraction molaire',color = 'red') #affichage de la courbe de la fraction molaire sur l'axe 1
ax2.plot(x, y[:,6], label ='Température (K)',color = 'green') #affichage de la courbe de la température sur l'axe 2
ax3.plot(x, y[:,7], label ='Pression (bar)',color = 'blue') #affichage de la courbe de la pression sur l'axe 3

ax1.legend(loc = 'upper center') #affichage de la légende pour l'axe 1 (fraction molaire) en haut au centre
ax2.legend(loc = 'lower center') #affichage de la légende pour l'axe 2 (température) en bas au centre
ax3.legend(loc = 'upper center', bbox_to_anchor =(0.5, 0.9)) #affichage de la légende pour l'axe 3 (pression) en haut au centre à 50% de la gauche et à 90 % du bas du graphique

ax1.set_ylim(0,0.035)  #définition des bornes (min,max) pour les axes
ax2.set_ylim(0,1000)
ax3.set_ylim(2.925,3.025)

plt.title('Graphique de la fraction molaire, de la température et de la pression') #affichage du titre pour le graphique 2

plt.show() #affichage du graphique 2
