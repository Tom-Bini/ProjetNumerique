import numpy as np
C_tot = 1/22.4      #Concentration totale en z = O (1/22,4 mol/L ou kmol/m^3)
C_CH4 = 1/4 * C_tot       #Concentration de CH4
C_H2O = 3/4 * C_tot       #Concentration de H2O
C_H2 = 0.00001      #Concentration de H2
C_CO = 0.00001      #Concentration de CO
C_CO2 = 0.00001     #Concentration de CO2
X = 0       #Conversion fractionnaire
Xu = 0      #Conversion fractionnaire ultime
T_W = 973.15 #(K)
T = T_W       #Température (K)
P = 3    #Pression totale initiale (bar)
epsilon = 0.5 #Porosité du réacteur
eta = 0.3     #Efficacité du catalyseur
rho_Cat = 1100  #Masse volumique du catalyseur (kg/m^3)     
rho_CaO = 1620 #Masse volumique des pellets de CaO (kg/m^3)
u_g = 1      #Vitesse superficielle du gaz à travers le réacteur (m/s)      
M_CaO = 56   #Masse molaire du CaO (kg/kmol)
M_CH4 = 16   #Masse molaire du CH4 (kg/kmol)
M_H2O = 18   #Masse molaire du H20 (kg/kmol)
M_H2 = 2     #Masse molaire du H2 (kg/kmol)
M_CO = 28    #Masse molaire du CO (kg/kmol)
M_CO2 = 44   #Masse molaire du CO2 (kg/kmol)
u_S = 10 ** (-3)      #Vitesse linéaire du lit mobile le long du réacteur (m/s)
mu = 2.8 * 10 ** (-3)      #Viscosité (pa.s)
d_p = 3 * 10 ** (-3)      #Diamètre des catalyseurs (Nickel) (m)
W_CaO = 83.6 * 10 ** (-3) / 3600 #Flux massique des pellets de Ca0 (kg/s)
W_cat = 16.4 * 10 ** (-3) / 3600 #Flux massique du catalyseur (kg/s)
C_ps = 0.98  #Capacité thermique du solide (kJ/kg.K)
C_pg = 8.45  #Capacité thermique du gaz     (kJ/kg.K)
D_R = 2.4 * 10 ** (-2) #Diamètre intérieur du réacteur tubulaire (m)
k_g = 2.59 * 10 ** (-4) #Conductivité thermique du gaz (kJ/m.s.K)
k_s = 10 ** (-3)     #Conductivité thermique du solide (kJ/m.s.K)
M_k = 303
N_k = -13146
M_b = 1.6
N_b = 5649
H_R1 = 206 * 10 ** 3 #(kJ/kmol)
H_R2 = 164.9 * 10 ** 3 #(kJ/kmol)
H_R3 = -41.1 * 10 ** 3 #(kJ/kmol)
H_cbn = -178.8 * 10 ** 3 #(kJ/kmol)
R = 8.314 #(J/mol.K) ou (pa.m^)
z_f = 0.29
V = z_f * np.pi * (D_R / 2) ** 2
rho_s = (W_cat + W_CaO) / ((W_cat / rho_Cat) + (W_CaO / rho_CaO))    #Masse volumique moyenne des deux solides au sein du réacteur
intervalleIntegration = [0,0.29]
k0_z = k_g * (epsilon + ((1 - epsilon)/((0.139 * epsilon) - 0.0339 + (2/3) * (k_g/k_s))))
Y = 7.5
tolerence = 10e-5

C_0 = np.array([C_CH4,C_H2O,C_H2,C_CO,C_CO2,X,T,P])       #Tableau des états initiaux 