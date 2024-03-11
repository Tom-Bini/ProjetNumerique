from Constantes import C0, intervalleIntegration
from Odefunction import odefunction
import scipy as sci 
import numpy as np



def calculConcentrationsEuler(intervalle,C0) :
    n = 10  #nombre de pas
    h = (intervalle[0]-intervalle[1])/n
    C = np.zeros((len(C0), n))
    C[:,0] = C0
    
    for i in range(n) :
        for j in range(len(C0)):
            Ctemp = odefunction(intervalle[0] + i * h, C[:,i])
            C0[j] = C0[j] + h * Ctemp[j]
            C[j,i] = C0[j]
            print(C0)
    return h,C

z, C = calculConcentrationsEuler(intervalleIntegration,C0)

def calculConcentrationsIVP(intervalle, C0):
    
    solve = sci.integrate.solve_ivp(odefunction, intervalleIntegration, C0, method='RK45')
    print(solve.success)
    print(C0)
z, C = calculConcentrationsIVP(intervalleIntegration, C0)
    