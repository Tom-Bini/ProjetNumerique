import numpy as np
from Constantes import C_0, intervalleIntegration
from Odefunction import odefunction
import scipy as sci

def calculConcentrationsEuler(intervalle,C0) : #définition de la fonction "calculConcentationEuler" qui prend 2 arguments, l'intervalle et le tableau des concentrations initiales
    
    z0, zf = intervalle #on extrait les 2 valeurs de "intervalle" pour les attribuer à z0 et zf
    h = 7.5e-8 #longueur d'un pas (abitraire mais on a choisi celui-ci car il a un bon rapport précision/tempsde calcul)
    z = np.arange(z0, zf + h, h) #création d'un tableau allant de z0 à zf compris avec un pas de h (si on avait juste mis zf on se serait arrêter un pas avant zf car le arange va jusqu'à la valeur du 2e argument non inclus)
    n = len(z) #calcul du nombre de pas
    
    C_F = np.zeros((len(C0), n)) #création d'un tableau avec comment nombre de ligne la longueur de C0 (ici : 8) et de n colonne (comme ça on peut ranger toutes les valeurs de C0 dans une colonne du nouveau tableau et puis à chaque n on va stocker les nouvelles valeurs)
    C_F[:,0] = C0 #on met les éléments du tableau C0 dans la première colonne du nouveau tableau

    for i in range(1, n):
        C_F[:, i] = C_F[:, i - 1] + h * odefunction(z[i - 1], C_F[:, i-1]) #on applique la formule de euler et on calcule les concentrations grâce à "odefunction" qu'on range à chaque itération à la colonne suivante du tableau C_F. 

    return z, C_F #ci dessus on a C_F[:,i-1] car on va chercher dans le tableau les valeurs de l'itération précédante et pour z[i-1], on commence la boucle à 1 (car les valeurs initiales sont déjà dans le tableau) sauf que on veut la valeur z[0] quand i = 1 puis z[1] quand i=2 etc donc il faut faire -1 

#z, C = calculConcentrationsEuler(intervalleIntegration, C_0)

def calculConcentrationsIVP(intervalle, C0, u_s = 1): #définition de la fonction calculConcentrationIVP qui prend 3 arguments, l'intervalle, le tableau des concentrations initiales et u_s pour le faire varier quand on calculera fonctionDeUg
    
    solve = sci.integrate.solve_ivp(lambda z, C: odefunction(z, C, u_s), intervalle, C0, max_step = 10**(-3), rtol=1e-5) #on calcule la solution grâce à solve_ivp, qui prend en argument l'équation résolue, lambda z,c, qui est odefunction pour nous, prend aussi en argument l'intervalle, le tableau C0 (concentrations initiales) qui correspond aux conditions initiales, maxstep qui est la taille maximum des pas et rtol qui est la tolérence
    z = solve.t #on met dans z toutes les valeurs où on a calculé des conce ntrations
    C = solve.y[:,:] #on met dans C toutes les valeurs des concentrations qui ont été calculées
    
    return z, C #on retourne l'intervalle et le tableau des concentrations
    
z, C = calculConcentrationsIVP(intervalleIntegration, C_0) #utilisation du la fonction et on met dans z et c les valeurs qu'elles retournent
