from Constantes import u_S, C_0, Y, intervalleIntegration, tolerence
import numpy as np
from SimReacteur import calculConcentrationsIVP
from RechercheRacine import secante

def FonctionDeUg(u_s):
    z, C = calculConcentrationsIVP(intervalleIntegration, C_0, u_s)
    C_f = C[:, -1]
    
    C_f_CH4 = C_f[0]
    C_f_H2 = C_f[2]
    C_f_CO = C_f[3]
    C_f_CO2 = C_f[4]
    C_f_tot_sec = C_f_CH4 + C_f_H2 + C_f_CO + C_f_CO2
    y = ((C_f_CO2 / C_f_tot_sec) * 100) - Y
    print("cTot:", C_f_tot_sec)
    print("pourcent :", (C_f_CO2 / C_f_tot_sec) * 100)
    
    return y

def optimisation(u_s, C_0, Y):

  u_s, status = secante(FonctionDeUg, 10e-6, 1, tolerence)
    
  return u_s, status
  
  
u_s_f, status = optimisation(u_S, C_0, Y)