CH4 = 0     #Concentration de CH4
H2O = 0     #Concentration de H2O
H2 = 0      #Concentration de H2
CO = 0      #Concentration de CO
CO2 = 0     #Concentration de CO2
X = 0       #Conversion fractionnaire
Xu = 0      #Conversion fractionnaire ultime
T = 0       #Température
P = 0       #Pression totale
epsilon = 0 #Porosité du réacteur
eta = 0     #Efficacité du catalyseur
rhoCat = 0  #Masse volumique du catalyseur
ri = 0      
rhoCaO = 0  #Masse volumique des pellets de CaO
rCbn = 0    #Taux de consommation de CO2 par carbonatation
ug = 0      
MCaO = 56   #Masse molaire du CaO
uS = 0      #Vitesse linéaire du lit mobile le long du réacteur
mu = 0      #Viscosité
dp = 0      #diamètre des catalyseurs (Nickel)
rhog = 0    #masse volumique de la phase gazeuse
rhos = 0    #masse volumique moyenne des deux solides au sein du réacteur

c = [CH4, H2O, H2, CO, CO2, X, T, P]



def odefunction(z,c):

    i = 0
    
    while i<5:
        
        c[i] = (1 - epsilon) * (eta * rhoCat * ri - rhoCaO * rCbn) / ug
        
        i += 1
        
    c[5] = MCaO * rCbn / uS
    c[7] = - (rhog * ug ** 2 / dp)*((1 - epsilon) / epsilon)*(150 * (1 - epsilon) * mu / (dp * rhog * ug) + 1.75) * 10 ** (-5)
    
    return c
