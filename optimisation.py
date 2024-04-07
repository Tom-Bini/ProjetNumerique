from Constantes import u_S, C_0, Y, intervalleIntegration, tolerence
import numpy as np
from SimReacteur import calculConcentrationsIVP
from RechercheRacine import secante
import matplotlib.pyplot as plt

def FonctionDeUg(u_s): #définition de la fonction "FonctionDeUg" qui prend un argument
    z, C = calculConcentrationsIVP(intervalleIntegration, C_0, u_s) #calcul de z et C grâce à la fonction "calculConcentrationsIVP"
    C_f = C[:, -1] #création d'un nouveau tableau où on prend toutes les lignes et la dernière colone du tableau C (pour avoir les dernières dérivées des concentrations, fraction molaire, température et pression)
    
    C_f_CH4 = C_f[0] #initialisation des concentrations
    C_f_H2 = C_f[2]
    C_f_CO = C_f[3]
    C_f_CO2 = C_f[4]
    C_f_tot_sec = C_f_CH4 + C_f_H2 + C_f_CO + C_f_CO2 #calcul de la somme des concentrations (sauf de h2o)
    y = ((C_f_CO2 / C_f_tot_sec) * 100) - Y #calcul de l'ordonnée (concentration) par rapport l'absice (u_S)
    
    return y

def optimisation(u_s, C_0, Y): #définition qui prend 3 arguments pour les passer à secante qui appelle fonctionDeUg, qui utilise Y et fonctionDeUg appelle calculConcentrationsIVP qui utilise C_0 et u_s

  u_s, status = secante(FonctionDeUg, 10e-5, 0.11, tolerence) #on calcul le point où la fonction est optimale
    
  return u_s, status #on retourne le point optimal
  
  
u_s_f, status = optimisation(u_S, C_0, Y) #on écrit dans u_s_f le u_S optimal pour le fonctionnement du réacteur

tabT = np.arange(T - 12,T + 12, 0.1)

def variationDeUsf(u_s,c,tabT):
    
    tabUsf = np.zeros(len(tabT))
    
    for i in range(len(tabT)):
        
        C_0[6] = tabT[i]
        tabUsf[i], _ = optimisation(u_s, C_0, Y)
        
    return tabUsf

Y = variationDeUsf(u_S,C_0,tabT)
