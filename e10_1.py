import matplotlib.pyplot as plt

from e9 import seuil

def etude_graphique():
    N_vals = list(range(10, 41))
    seuils = [seuil(n) for n in N_vals]
    
    #On affiche les résultats dans un graphique
    plt.figure(figsize=(10, 5))
    #On trace les points et les relie par des lignes
    plt.plot(N_vals, seuils, marker='o', linestyle='-', color='b')
    #On ajoute un titre et des labels aux axes
    plt.title("Seuil de forte connexité p en fonction de n")
    plt.xlabel("Nombre de sommets (n)")
    plt.ylabel("Seuil de probabilité (p)")
    #On ajoute une grille pour faciliter la lecture du graphique
    plt.grid(True)
    plt.show()
    
    return N_vals, seuils