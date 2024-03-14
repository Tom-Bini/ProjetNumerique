import numpy as np
from Constantes import C_0, intervalleIntegration
from Odefunction import odefunction
import scipy as sci

def calculConcentrationsEuler(intervalle,C0) :
    
    z0, zf = intervalle
    n = 50 #nbre pas
    h = (zf - z0)/n #taille pas
    C_F = np.copy(C0)

    for i in range(n):
        C_temp = odefunction(intervalle[0] + i * h, C0)
        C_temp = C0 + h * C_temp
        C0 = C_temp
        C_F = np.vstack((C_F, C0))

    return C_F

#a = calculConcentrationsEuler(intervalleIntegration, C_0)

def calculConcentrationsIVP(intervalle, C0):
    
    solve = sci.integrate.solve_ivp(lambda z, C: odefunction(z, C), intervalle, C0)
    z = solve.t
    C = solve.y[:,:]
    
    return z, C
    
#z, C = calculConcentrationsIVP(intervalleIntegration, C_0)