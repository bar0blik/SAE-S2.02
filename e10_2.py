import numpy as np

def identification_puissance(N_vals, seuils):
    """
    Identifie la fonction puissance p = c * n^a sans utiliser scipy.
    Utilise uniquement les opérations vectorielles de NumPy.
    """
    # 1. Passage au logarithme : X = ln(n) et Y = ln(seuil)
    X = np.log(N_vals)
    Y = np.log(seuils)
    
    # 2. Calcul des moyennes de X et Y
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    
    # 3. Calcul de la pente 'a' (covariance / variance)
    numerateur = np.sum((X - mean_X) * (Y - mean_Y))
    denominateur = np.sum((X - mean_X) ** 2)
    a = numerateur / denominateur
    
    # 4. Calcul de l'ordonnée à l'origine 'b' (où b = ln(c))
    b = mean_Y - a * mean_X
    
    # 5. On retrouve 'c' par l'exponentielle
    c = np.exp(b)
    
    # Affichage des résultats
    print("--- Résultats de l'identification ---")
    print(f"Pente (a)          : {a:.4f}")
    print(f"Coefficient (c)    : {c:.4f}")
    print(f"Équation trouvée   : p = {c:.3f} * n^({a:.3f})")
    
    return a, c