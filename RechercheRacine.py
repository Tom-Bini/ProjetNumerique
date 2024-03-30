def secante(f, x0, x1, tol, nmax = 1000):
    
    y0 = f(x0)
    y1 = f(x1)
    
    statut = 0
    
    if abs(y0) < tol:
        return x0, statut
    if abs(y1) < tol:
        return x1, statut
        
    n = 0
    y2 = 10 #ajout d'une valeur arbitraire à y2 pour entrer dans la boucle (elle n'aura aucune influence sur le calcul car elle n'est pas utilisée avant d'être remplacée par f(x2)
        
    while abs(y1) > tol and n < nmax:
        
        
        if y1 - y0 == 0:
            statut = 1
            return x0, statut
        x2 = x1 - ((y1 * (x1 - x0)) / (y1 - y0))
        y2 = f(x2)
        
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
        n = n + 1 #compteur pour le nombre d'itération de la boucle
    if n == nmax:
        statut = - 1
        return x1, statut
                
    return x1, statut

def bissection(f, x0, x1, tol, nmax = 1000):
    y0 = f(x0)
    y1 = f(x1)
    
    statut=0
    
    if abs(y0) < tol:
        return x0, statut
    if abs(y1) < tol:
        return x1, statut
    if y0 * y1 > 0:
        statut = 1
        return x1, statut
    
    if y1 < y0: #si f(x1) est inférieur à f(x0) alors on échnage x0 et x1 pour toujours avoir f(x0) < f(x1)
        temp = x1
        x1 = x0
        x0 = temp
        
        temp = y1 #on échange y0 et y1 pour qu'ils correspondent toujours à x0 et x1
        y1 = y0
        y0 = temp
        
    n = 0.0 #on initialise n à 0 pour entrer dans la boucle
    x2 = 0.0
    y2 = y0 #attribution d'une valeur à y2 pour entrer dans la boucle
    
    while abs(x1 - x0) > tol and n < nmax :
        x2 = (x0 + x1) / 2
        y2 = f(x2)
            
        if y2 < 0:
            x0=x2
        else :
            x1=x2
        n = n+1 #on incrémente n, n compte le nombre d'itération, si n = nmax, on sort de la boucle, on en déduit que la fonction ne converge pas ou pas assez vite
        
    if n == nmax:
        statut = - 1
        return x2, statut
        
    return x2, statut
