from e7 import fc
from e8 import generer_matrice

def test_stat_fc2(n, p, nb_tests=200):
    """Teste la forte connexité avec une probabilité p variable."""
    succes = 0
    for _ in range(nb_tests):
        M = generer_matrice(n, p)
        if fc(M):
            succes += 1
    return succes / nb_tests

def seuil(n, tolerance=0.99, pas=0.02):
    """
    Détermine le p minimum pour lequel le graphe est fortement connexe
    dans plus de 'tolerance' (99%) des cas. On descend p depuis 1.0.
    """
    p = 1.0
    dernier_p_valide = 1.0
    
    while p >= 0:
        prob = test_stat_fc2(n, p, nb_tests=200)
        if prob < tolerance:
            # Dès qu'on passe sous les 99%, le seuil cherché est le p précédent
            return dernier_p_valide
        dernier_p_valide = p
        p -= pas
        
    return 0.0