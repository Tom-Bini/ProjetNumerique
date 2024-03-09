import numpy as np
from Constantes import CH4,H2O,H2,CO,CO2,X,Xu,T,P,epsilon,eta,rhoCat,rhoCaO,rCbn,ug,MCaO,MCH4,MH2O,MH2,MCO,MCO2,uS,mu,dp,WCaO,Wcat,Cps,Cpg,DR,kg,ks,Mk,Nk,Mb,Nb,HR1,HR2,HR3,Hcbn,TW,zf,XCH4,XH2O,XCaO,XH2,XCO,XCO2,R,PCaO,PCH4,PH2O,PH2,PCO,PCO2,rhos,k0z
from scipy.integrate import solve_ivp

c = [CH4, H2O, H2, CO, CO2, X, T, P]

def odefunction(z,c):
    
    rhog = (MCaO * PCaO + MCH4 * PCH4 + MH2O * PH2O + MH2 * PH2 + MCO * PCO + MCO2 * PCO2)/ (R * T)     #Masse volumique de la phase gazeuse
    Rep = ug * epsilon * rhog * dp / mu
    if Rep < 20 :
        hW = 6.15 * (k0z / DR)
    else :
        if 0.05 < (dp / DR) < 0.3 :
            hW = 2.03 * (kg/DR) * Rep ** 0.8 * np.exp((-6 * dp)/DR)
    K1 = 4.707 * 10 ** 12 * np.exp(-224000/(R * T))
    K3 = 1.142 * 10 ** (-2) * np.exp(37300/(R * T))
    K2 = K1 * K3
    
    k1 = 1.842 / 3600 * 10 ** (-4) * np.exp((-240100/R) * (1/T - 1/648))
    k2 = 2.193 / 3600 * 10 ** (-5) * np.exp((-243900/R) * (1/T - 1/648))
    k3 = 7.558 / 3600 * np.exp((-67130/R) * (1/T - 1/648))
    
    KCH4 = 0.179 * np.exp((38280/R) * (1/T - 1/823))
    KH2O = 0.4152 * np.exp((-88680/R) * (1/T - 1/823))
    KH2 = 0.0296 * np.exp((82900/R) * (1/T - 1/648))
    KCO = 40.91 * np.exp((70650/R) * (1/T - 1/648))
    
    den = 1 + KCO * PCO + KH2 * PH2 + KCH4 * PCH4 + KH2O * PH2O / PH2    
    R1 = k1 * (PCH4 * PH2O - PH2 ** 3 * PCO / K1) / (den ** 2 * PH2 ** 2.5)    
    R2 = k2 * (PCH4 * PH2O ** 2 - PH2 ** 4 * PCO2 / K2) / (den ** 2 * PH2 ** 3.5)    
    R3 = k3 * (PCO * PH2O - PH2 * PCO2 / K3) / (den ** 2 * PH2)
    
    rCH4 = - R1 - R2
    rH2O = - R1 - 2 * R2 - R3
    rH2 = 3 * R1 + 4 * R2 + R3
    rCO = R1 - R3
    rCO2 = R2 + R3
    
    r = [rCH4, rH2O, rH2, rCO, rCO2]

    i = 0
    
    while i<5:
        
        c[i] = (1 - epsilon) * (eta * rhoCat * r[i] - rhoCaO * rCbn) / ug
        
        i += 1
        
    c[5] = MCaO * rCbn / uS
    
    c[6] = - ((1 - epsilon) * eta * rhoCat + (R1 * HR1 + R2 * HR2 + R3 * HR3) - (1 - epsilon) * rhoCaO * rCbn * Hcbn + hW * (TW - T) * 4 / DR) / ((1 - epsilon) * rhos * uS * Cps + rhog * ug * Cpg)
    
    c[7] = - (rhog * ug ** 2 / dp)*((1 - epsilon) / epsilon)*(150 * (1 - epsilon) * mu / (dp * rhog * ug) + 1.75) * 10 ** (-5)
    
    return c

solutionOdeFunction = solve_ivp(odefunction)
