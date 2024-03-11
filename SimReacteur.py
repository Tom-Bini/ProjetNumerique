# solutionOdeFunction = solve_ivp(odefunction,intervalleIntegration,etatsInitiaux) pas sûr qu'on doive l'implémenter like that

from Constantes.py import C0

z, C = calculConcentrationsEuler([z0, zf], C0)

