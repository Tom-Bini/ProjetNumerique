from Constantes import C_0, intervalleIntegration
from Odefunction import odefunction
import scipy as sci
import numpy as np

def calculConcentrationsEuler(intervalle,C_0) :
    print(C_0)
    n = 10  #nombre de pas
    h = (intervalle[0]-intervalle[1])/n
    C = np.zeros((n + 1, len(C_0)))
    C_temp = C_0
    
   '''for i in range(n) :
        for j in range(len(C_0)):
            print("C0 :")
            print(C_0)
            C_temp = np.zeros(len(C_0))
            C_temp = odefunction(intervalle[0] + i * h, C[:,i])
            C_0 = C_0 + h * C_temp
            C[:,i] = C_0
            print("C :")
            print(C)'''
            
            
    for i in range(n) :
        print("C0 :")
        print(C_0)
        C[i] = Cz
        Cz = odefunction(intervalle[0] + (i + 1) * h, C_temp)
        
        
        
        
        
        print("C :")
        print(C)
    return h,C

z, C = calculConcentrationsEuler(intervalleIntegration,C_0)

'''def calculConcentrationsIVP(intervalle, C_0):
    
    solve = sci.integrate.solve_ivp(odefunction, intervalleIntegration, C_0, method='RK45')
    print(solve.success)
    print(C_0)
z, C = calculConcentrationsIVP(intervalleIntegration, C_0)'''
    