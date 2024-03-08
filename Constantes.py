import numpy as np
CH4 = 0     #Concentration de CH4
H2O = 0     #Concentration de H2O
H2 = 0      #Concentration de H2
CO = 0      #Concentration de CO
CO2 = 0     #Concentration de CO2
X = 0       #Conversion fractionnaire
Xu = 0      #Conversion fractionnaire ultime
T = 0       #Température
P = 0       #Pression totale
epsilon = 0.5 #Porosité du réacteur
eta = 0.3     #Efficacité du catalyseur
rhoCat = 1100  #Masse volumique du catalyseur      
rhoCaO = 1620  #Masse volumique des pellets de CaO
rCbn = 0    #Taux de consommation de CO2 par carbonatation
ug = 1      #Vitesse superficielle du gaz à travers le réacteur      
MCaO = 56   #Masse molaire du CaO
MCH4 = 16   #Masse molaire du CH4
MH2O = 18   #Masse molaire du H20
MH2 = 2     #Masse molaire du H2
MCO = 28    #Masse molaire du CO
MCO2 = 44   #Masse molaire du CO2
uS = 10 ** (-3)      #Vitesse linéaire du lit mobile le long du réacteur
mu = 2.8 * 10 ** (-3)      #Viscosité
dp = 3 * 10 ** (-3)      #Diamètre des catalyseurs (Nickel)
WCaO = 83.6 * 10 ** (-3) #Flux massique des pellets de Ca0
Wcat = 16.4 * 10 ** (-3) #Flux massique du catalyseur
Cps = 0.98  #Capacité thermique du solide
Cpg = 8.45  #Capacité thermique du gaz
DR = 2.4 * 10 ** (-2) #Diamètre intérieur du réacteur tubulaire
kg = 2.59 * 10 ** (-4) #Conductivité thermique du gaz
ks = 10 ** (-3)     #Conductivité thermique du solide
Mk = 303
Nk = -13146
Mb = 1.6
Nb = 5649
HR1 = 206 * 10 ** 3
HR2 = 164.9 * 10 ** 3
HR3 = -41.1 * 10 ** 3
Hcbn = 178.8 * 10 ** 3
TW = 973.15
zf = 0.29
XCH4 = 3
XH2O = 3
XCaO = 0
XH2 = 0
XCO = 0
XCO2 = 0
R = 8.314
PCaO = P * XCaO
PCH4 = P * XCH4
PH2O = P * XH2O
PH2 = P * XH2
PCO = P * XCO
PCO2 = P * XCO2
rhos = (Wcat + WCaO) / ((Wcat / rhoCat) + (WCaO / rhoCaO))    #Masse volumique moyenne des deux solides au sein du réacteur
rhog = (MCaO * PCaO + MCH4 * PCH4 + MH2O * PH2O + MH2 * PH2 + MCO * PCO + MCO2 * PCO2)/ (R * T)     #Masse volumique de la phase gazeuse
Rep = ug * epsilon * rhog * dp / mu
k0z = kg * (epsilon + ((1 - epsilon)/((0.139 * epsilon) - 0.0339 + (2/3) * (kg/ks))))
if Rep < 20 :
    hW = 6.15 * (k0z / DR)
else :
    if 0.05 < (dp / DR) < 0.3 :
        hW = 2.03 * (kg/DR) * Rep ** 0.8 * np.exp((-6 * dp)/DR)
