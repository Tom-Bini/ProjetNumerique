from Constantes import *

c = [CH4, H2O, H2, CO, CO2, X, T, P]

def odefunction(z,c):
    
    den = 1 + KCO * pCO + KH2 * pH2 + KCH4 * pCH4 + KH2O * pH2O / pH2
    
    R1 = k1 * (pCH4 * pH2O - pH2 ** 3 * pCO / K1) / (den ** 2 * pH2 ** 2.5)
    
    R2 = k2 * (pCH4 * pH2O ** 2 - pH2 ** 4 * pCO2 / K2) / (den ** 2 * pH2 ** 3.5)
    
    R3 = k3 * (pCO * pH2O - pH2 * pCO2 / K3) / (den ** 2 * pH2)
    
    rCH4 = - R1 - R2
    rH2O = - R1 - 2 * R2 - R3
    rH2 = 3 * R1 + 4 * R2 + R3
    rCO = R1 - R3
    rCO2 = R2 + R3
    
    r = [rCH4, rH20, rH2, rCO, rCO2]

    i = 0
    
    while i<5:
        
        c[i] = (1 - epsilon) * (eta * rhoCat * r[i] - rhoCaO * rCbn) / ug
        
        i += 1
        
    c[5] = MCaO * rCbn / uS
    
    c[6] = - ((1 - epsilon) * eta * rhoCat + (R1 * HR1 + R2 * HR2 + R3 * HR3) - (1 - epsilon) * rhoCaO * rCbn * Hcbn + hW * (TW - T) * 4 / DR) / ((1 - epsilon) * rhos * uS * Cps + rhog * ug * Cpg)
    
    c[7] = - (rhog * ug ** 2 / dp)*((1 - epsilon) / epsilon)*(150 * (1 - epsilon) * mu / (dp * rhog * ug) + 1.75) * 10 ** (-5)
    
    return c
