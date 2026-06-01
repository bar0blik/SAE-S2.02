import numpy as np
import matplotlib.pyplot as plt

def fermeture_transitive(M):
    """Calcule la fermeture transitive avec l'algorithme de Roy-Warshall."""
    n = len(M)
    # Copie de la matrice pour ne pas modifier l'originale
    TC = np.array(M, copy=True)
    
    # On met des 1 sur la diagonale (un sommet peut toujours s'atteindre lui-même)
    np.fill_diagonal(TC, 1)
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                TC[i][j] = TC[i][j] or (TC[i][k] and TC[k][j])
    return TC

def fc(M):
    """Teste si le graphe est fortement connexe."""
    TC = fermeture_transitive(M)
    # Retourne True si tous les éléments valent 1
    return np.all(TC == 1)