z, C = calculConcentrationsEuler([z0, zf])

solutionOdeFunction = solve_ivp(odefunction,intervalleIntegration,etatsInitiaux)