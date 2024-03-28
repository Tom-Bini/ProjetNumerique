def secante(f,x0,x1,tol): #définition de la fonction sécante qui prend en argument une fonction, 2 bornes et une tolérence
    nmax = 1000 #initialisation du nombre maximum d'étape (choix arbitraire, si la fonction ne converge pas vers une racine en moins de 1000 étapes on considère qu'il n'y en a pas)
    y0 = f(x0) #calcul des images de x0 et x1
    y1 = f(x1)
    
    statut = 0 #initialisation du statut à 0 (si il reste à 0, alors pas d'erreur)
    
    if abs(y0) < tol: #si y0 ou -y0 est inférieur à la tolérence alors x0 est une racine donc on retourne la racine sans faire le calcul
        return x0, statut
    if abs(y1) < tol: #même chose que pour y0
        return x1, statut
        
    n = 0 #initialisation de n à 0 pour compter le nombre d'itération de la boucle
    y2 = 10 #ajout d'une valeur arbitraire à y2 pour entrer dans la boucle (elle n'aura aucune influence sur le calcul car elle n'est pas utilisée avant d'être remplacée par f(x2)
        
    while abs(y1) > tol and n < nmax: #gardien de boucle qui permet d'enter dans la boucle si la racine trouvée n'entre pas dans la tolérence et si le nombre d'itération est inférieur à nmax
        
        if y1 - y0 == 0: #barrière pour éviter une division par 0 lors de l'application du calcul de la sécante
            statut = 1 #change la valeur du statut
            return x0, statut #retourne x0 et le statut modifié pour indiquer l'erreur
        x2 = x1 - ((y1 * (x1 - x0)) / (y1 - y0)) #calcul d'approximation de la racine
        y2 = f(x2)       
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
        n = n + 1 #compteur pour le nombre d'itération de la boucle
    if n == nmax: #quand le nombre d'itération maximum est atteint on change le statut et on le retourne
        statut = - 1
        return x1, statut
                
    return x1, statut #on retourne l'approximation de la racine avec la variable statut pour indiquer si tout a fonctionné ou non

def bissection(f,x0,x1,tol): #définition de la fonction bissection qui prend en argument une fonction, 2 bornes et une tolérence
    nmax = 100 #initialisation du nombre maximum d'étape (choix arbitraire, si la fonction ne converge pas vers une racine en moins de 100 étapes on considère qu'il n'y en a pas)
    y0 = f(x0) #calcul des images de x0 et x1
    y1 = f(x1)
    
    statut=0 #initialisation du statut à 0 (si il reste à 0, alors pas d'erreur)
    
    if abs(y0) < tol:  #si y0 ou -y0 est inférieur à la tolérence alors x0 est une racine donc on retourne la racine sans faire le calcul
        return x0, statut
    if abs(y1) < tol: #même chose que pour y0
        return x1, statut
    if y0 * y1 > 0: #on regarde le signe des images, si elles ont le même signe alors il n'y a pas de racine entre les bornes x0 et x1
        statut = 1 #on change le statut pour montrer une erreur
        return x1, statut  #on retourne le statut pour montrer qu'il y a eu une erreur
    
    if y1 < y0: #si f(x1) est inférieur à f(x0) alors on échange x0 et x1 pour toujours avoir f(x0) < f(x1)
        temp = x1
        x1 = x0
        x0 = temp
        
        temp = y1 #on échange y0 et y1 pour qu'ils correspondent toujours à x0 et x1
        y1 = y0
        y0 = temp
        
    n = 0 #on initialise n à 0 pour entrer dans la boucle
    x2 = 0 #initialisation de x2
    y2 = y0 #attribution d'une valeur à y2 pour entrer dans la boucle (arbitraire et n'a aucune incidence car elle est changée avant d'être utilisée)
    
    while abs(x1-x0) > tol and n < nmax : #gardien de boucle, continue l'exécution de la boucle si il n'y a pas de racine dans notre tolérence et si le nombre d'itération n'a pas atteint le nombre d'itération maximum
        x2 = (x0 + x1) / 2 #application de la formule de la bissection
        y2 = f(x2)
            
        if y2 < 0: #si l'image de la nouvelle approximation de la racine calculée est négative, on remplace x0 (qui est la borne négative) par x2(qui est la nouvelle approximation de la racine) 
            x0=x2
        else :
            x1=x2#si l'image de la nouvelle approximation de la racine calculée est positive, on remplace x1 (qui est la borne positive) par x2(qui est la nouvelle approximation de la racine)
            n = n+1 #on incrémente n, n compte le nombre d'itération, si n = nmax, on sort de la boucle, on en déduit que la fonction ne converge pas ou pas assez vite vers une racine dans notre tolérence
        
    if n == nmax: #si le nombre d'itération à atteint le nombre d'itération maximum
        statut = - 1 #on change le statut pour indiquer une erreur
        return x2, statut #on retourne le statut pour insiquer une erreur
        
    return x2, statut #on retourne l'approximation de la racine et le satut pour indiquer si il y a eu une erreur ou non
