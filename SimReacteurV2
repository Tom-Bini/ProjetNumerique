import numpy as np
from Constantes import C_0, intervalleIntegration
from Odefunction import odefunction
import scipy as sci

def calculConcentrationsEuler(intervalle,C_0) :
    n = 10 #nbre pas
    h = (intervalle[0]-intervalle[1])/n
    C_F = C_0

    for i in range(n):
        C_temp = odefunction(intervalle[0] + i * h, C_0)
        C_temp = C_0 + h * C_temp
        C_0 = C_temp
        C_F = np.vstack((C_F, C_0))

    return C_F
    
a = calculConcentrationsEuler(intervalleIntegration, C_0)
