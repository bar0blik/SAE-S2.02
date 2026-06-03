import numpy as np

from e7 import fc

def generer_matrice(n, p):
    """Génère une matrice d'adjacence aléatoire de taille n avec probabilité p d'avoir un 1."""
    return np.random.choice([0, 1], size=(n, n), p=[1-p, p])

def test_stat_fc(n, nb_tests=200):
    """Retourne le pourcentage de graphes fortement connexes sur un échantillon."""
    succes = 0
    for _ in range(nb_tests):
        M = generer_matrice(n, 0.5)
        if fc(M):
            succes += 1
    return succes / nb_tests

# Pour déterminer à partir de quel n l'affirmation est vraie :
if __name__ == "__main__":
    for n in range(2, 20):
        prob = test_stat_fc(n)
        print(f"n={n}: {prob*100}%")
        if prob >= 0.99:
            print(f"Seuil de 99% atteint pour n={n}")
            break