import matplotlib.pyplot as plt

from e9 import seuil

def etude_graphique():
    N_vals = list(range(10, 41))
    seuils = [seuil(n) for n in N_vals]
    
    plt.figure(figsize=(10, 5))
    plt.plot(N_vals, seuils, marker='o', linestyle='-', color='b')
    plt.title("Seuil de forte connexité p en fonction de n")
    plt.xlabel("Nombre de sommets (n)")
    plt.ylabel("Seuil de probabilité (p)")
    plt.grid(True)
    plt.show()
    
    return N_vals, seuils