import numpy as np
import random


def graphe(n, a, b):
    """
    Génère aléatoirement une matrice n*n dont les coefficients sont entiers et compris 
    entre a et b-1.
    """
    #Cas de base 1, n est négatif
    if n <= 0:
        return "n doit être positif"
    #Cas de base 2, a est supérieur ou égale à b
    if a >= b:
        return "a doit être inférieur à b"
    #Création de la matrice
    M = np.empty((n, n))
    #Coefficients de type float
    M = M.astype('float64')
    
    #Parcours de la matrice par ligne
    for i in range(n):
        #Parcours de la matrice par colonne
        for j in range(n):
            #Génère un nombre de type float compris entre 0 et 1, si inférieur à la motié -> met la valeur infini à la ligne i de la colonne j
            if random.random() < 0.5:
                M[i, j] = float('inf')
            #Sinon -> met une valeure comprise entre a et b-1 (puisque b est exclus dans l'intervale) à la ligne i de la colonne j  
            else:
                M[i, j] = random.randint(a, b - 1)
    return M

def graphe2(n, p, a, b):
    """
    Génère aléatoirement une matrice n*n dont les coefficients ont une probabilité p d'être 
    compris entre a et b-1 et une probabilité 1-p d'être infini.
    """
    if p < 0 or p > 1:
        return "p doit être compris entre 0 et 1"
    #Cas de base 1, n est négatif
    if n <= 0:
        return "n doit être positif"
    #Cas de base 2, a est supérieur ou égale à b
    if a >= b:
        return "a doit être inférieur à b"
    #Création de la matrice
    M = np.empty((n, n))
    #Coefficients de type float
    M = M.astype('float64')
    
    #Parcours de la matrice par ligne
    for i in range(n):
        #Parcours de la matrice par colonne
        for j in range(n):
            #Génère un nombre de type float compris entre 0 et 1, si inférieur à la motié -> met la valeur infini à la ligne i de la colonne j
            if random.random() < 1 - p:
                M[i, j] = float('inf')
            #Sinon -> met une valeure comprise entre a et b-1 (puisque b est exclus dans l'intervale) à la ligne i de la colonne j  
            else:
                M[i, j] = random.randint(a, b - 1)
    return M

print(graphe2(4, 0.3, 1, 10))