import numpy as np
from Constantes import C_CH4,C_H2O,C_H2,C_CO,C_CO2,X,T,P,epsilon,eta,rho_Cat,rho_CaO,u_g,M_CaO,M_CH4,M_H2O,M_H2,M_CO,M_CO2,mu,d_p,C_ps,C_pg,D_R,k_g,M_k,N_k,M_b,N_b,H_R1,H_R2,H_R3,H_cbn,T_W,R,rho_s,k0_z,V

c = np.array([C_CH4, C_H2O, C_H2, C_CO, C_CO2, X, T, P]) #définition d'un tableau "C" avec nos concentrations, fraction molaire, température et pression

def odefunction(z, c, u_S): #définition de la fonction "odefunction" qui prend en argument z,c et u_S
    
    dC = np.zeros(len(c)) #création d'un tableau "dC" de même longueur que "C"
    
    C_CH4 = c[0]   #initialisation des concentrations, fraction molaire, température et pression #kmol / m^3
    C_H2O = c[1]
    C_H2 = c[2]
    C_CO = c[3]
    C_CO2 = c[4]
    X = c[5]
    T = c[6]
    P = c[7]
    
    K_1 = 4.707 * 10 ** 12 * np.exp(-224000/(R * T)) #calcul des "K"
    K_3 = 1.142 * 10 ** (-2) * np.exp(37300/(R * T))
    K_2 = K_1 * K_3
    
    k_1 = (1.842 / 3600) * 10 ** (-4) * np.exp((-240100/R) * (1/T - 1/648)) #calcul des "k"
    k_2 = (2.193 / 3600) * 10 ** (-5) * np.exp((-243900/R) * (1/T - 1/648))
    k_3 = (7.558 / 3600) * np.exp((-67130/R) * (1/T - 1/648))
    
    K_CH4 = 0.179 * np.exp((38280/R) * (1/T - 1/823)) #calcul des K_i
    K_H2O = 0.4152 * np.exp((-88680/R) * (1/T - 1/823))
    K_H2 = 0.0296 * np.exp((82900/R) * (1/T - 1/648))
    K_CO = 40.91 * np.exp((70650/R) * (1/T - 1/648))
    
    n_CH4 = C_CH4 * V  #calcul du nombre de mole des composés#kmol
    n_H2O = C_H2O * V
    n_H2 = C_H2 * V
    n_CO = C_CO * V
    n_CO2 = C_CO2 * V
    n_tot = n_CH4 + n_H2O + n_H2 + n_CO + n_CO2
    X_CH4 = n_CH4 / n_tot #calcul des fractions molaires des composés
    X_H2O = n_H2O / n_tot
    X_H2 = n_H2 / n_tot
    X_CO = n_CO / n_tot
    X_CO2 = n_CO2 / n_tot
    P_CH4 = P * X_CH4 #calcul des pressions partielles des composés
    P_H2O = P * X_H2O
    P_H2 = P * X_H2
    P_CO = P * X_CO
    P_CO2 = P * X_CO2
    
    den = 1 + K_CO * P_CO + K_H2 * P_H2 + K_CH4 * P_CH4 + K_H2O * P_H2O / P_H2 #calcul du "den"
    
    R_1 = k_1 / P_H2 ** 2.5 * (P_CH4 * P_H2O - (P_H2 ** 3 * P_CO) / K_1) / den ** 2 #calcul des "R"
    R_2 = k_2 / P_H2 ** 3.5 * (P_CH4 * P_H2O ** 2 - (P_H2 ** 4 * P_CO2) / K_2) / den ** 2
    R_3 = k_3 / P_H2 * (P_CO * P_H2O - P_H2 * P_CO2 / K_3) / den ** 2
    
    rho_g = (1/(R * T)) * (M_CH4 * P_CH4 + M_H2O * P_H2O + M_H2 * P_H2 + M_CO * P_CO + M_CO2 * P_CO2) * 100     #calcul de la masse volumique de la phase gazeuse avec les "p" en Pa (kg/m^3)
    
    Rep = u_g * epsilon * rho_g * d_p / mu #calcul du Rep
    
    r_CH4 = - R_1 - R_2 #calcul des r
    r_H2O = - R_1 - 2 * R_2 - R_3
    r_H2 = 3 * R_1 + 4 * R_2 + R_3
    
    if Rep <= 20 : #calcul de h_W en fonction de Rep
        h_W = 6.15 * (k0_z / D_R)
    elif Rep > 20 and 0.05 < (d_p / D_R) < 0.3 :
        h_W = 2.03 * (k_g / D_R) * Rep ** 0.8 * np.exp(-6 * d_p / D_R)
    else : #retourne une erreur si le calcul de h_W est impossible
        return dC
    
    r_CO = R_1 - R_3 #calcul des r
    r_CO2 = R_2 + R_3
    
    k_c = M_k * np.exp(N_k / T) #calcul de certaines variables en fonction de la température
    b = M_b * np.exp(N_b / T)        
    X_u = k_c * b
    r_cbn = (k_c / M_CaO) * (1 - (X / X_u)) ** 2

        
    dC[5] = (M_CaO * r_cbn) / u_S #calcul des dérivées
    
    dC[7] = ( - rho_g * u_g ** 2 * (1 - epsilon) / (d_p * epsilon)) * (150 * (1 - epsilon) * mu / (d_p * rho_g * u_g) + 1.75) * 10 ** (-5)
    
    dC[6] = ( - (1 - epsilon) * rho_Cat * (eta * (R_1 * H_R1 + R_2 * H_R2 + R_3 * H_R3)) - (1 - epsilon) * rho_CaO * r_cbn * H_cbn + (h_W * (T_W - T)) * 4 / D_R) / (((1 - epsilon) * rho_s * u_S * C_ps) + (rho_g * u_g * C_pg))
    
    dC[0] = (eta * (1 - epsilon) * rho_Cat * r_CH4 - (1 - epsilon) * rho_CaO * r_cbn) / u_g
    
    dC[1] = (eta * (1 - epsilon) * rho_Cat * r_H2O - (1 - epsilon) * rho_CaO * r_cbn) / u_g
    
    dC[2] = (eta * (1 - epsilon) * rho_Cat * r_H2 - (1 - epsilon) * rho_CaO * r_cbn) / u_g
    
    dC[3] = (eta * (1 - epsilon) * rho_Cat * r_CO - (1 - epsilon) * rho_CaO * r_cbn) / u_g
    
    dC[4] = (eta * (1 - epsilon) * rho_Cat * r_CO2 - (1 - epsilon) * rho_CaO * r_cbn) / u_g
    
    return dC #la focntion retourne le tableau avec les dérivées
