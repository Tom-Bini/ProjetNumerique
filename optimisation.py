from Constantes import u_S, C_0, Y, intervalleIntegration, tolerence
import numpy as np
from SimReacteur import calculConcentrationsIVP
from RechercheRacine import bissection, secante

def FonctionDeUs(u_s):
    z, C = calculConcentrationsIVP(intervalleIntegration, C_0, u_s)
    C_f = C[:, -1]
    
    C_f_CH4 = C_f[0]
    C_f_H2 = C_f[2]
    C_f_CO = C_f[3]
    C_f_CO2 = C_f[4]
    C_f_tot_sec = C_f_CH4 + C_f_H2 + C_f_CO + C_f_CO2
    y = ((C_f_CO2 / C_f_tot_sec) * 100) - Y
    
    return y

def optimisation(u_s, C_0, Y):

  u_s, status = secante(FonctionDeUs, 1e-5, 1e-1, tolerence) #1e-5 et 1e-1 est un intervalle qui fonctionne
    
  return u_s, status
  
  
u_s_f, status = optimisation(u_S, C_0, Y)