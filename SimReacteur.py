import numpy as np
from Constantes import C_0, intervalleIntegration
from Odefunction import odefunction
import scipy as sci

def calculConcentrationsEuler(intervalle,C0) :
    
    z0, zf = intervalle
    h = 7.5e-8
    z = np.arange(z0, zf + h, h)
    n = len(z)
    
    C_F = np.zeros((len(C0), n))
    C_F[:,0] = C0

    for i in range(1, n):
        C_F[:, i] = C_F[:, i - 1] + h * odefunction(z[i - 1], C_F[:, i-1])

    return z, C_F

#z, C = calculConcentrationsEuler(intervalleIntegration, C_0)

def calculConcentrationsIVP(intervalle, C0):
    
    solve = sci.integrate.solve_ivp(lambda z, C: odefunction(z, C), intervalle, C0, max_step = 10**(-3), rtol=1e-5)
    z = solve.t
    C = solve.y[:,:]
    
    return z, C
    
z, C = calculConcentrationsIVP(intervalleIntegration, C_0)