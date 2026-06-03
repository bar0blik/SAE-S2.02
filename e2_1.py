import graphviz
import numpy as np
from matplotlib.pylab import dot
def afficher_graphe(M): 
    n = len(M)
    # Création du graphe de gauche à droite avec Graphviz
    dot = graphviz.Digraph(graph_attr={'rankdir' : 'LR'})

    for i in range(n):
         # Nœuds en noir
        dot.node(str(i), str(i), fillcolor='lightblue', fontcolor='black')

    for i in range(n):
        for j in range(n):
            # Affiche seulement les arêtes avec poids fini
            if M[i, j] != float('inf') and M[i, j] != 0:
                # Poids arrondi à l'entier le plus proche ou affiché avec une décimale
                weight = int(M[i, j]) if M[i, j] == int(M[i, j]) else f"{M[i, j]:.1f}"
                # Arêtes en gris
                dot.edge(str(i), str(j), label=str(weight), color='gray', penwidth='1.5')

    dot.view()

# Exemple
# Ceci évite d'exécuter le code d'affichage du graphe lors de l'importation du module, et ne l'exécutera que si
# ce fichier est exécuté directement.
if __name__ == "__main__":
    INF = float('inf')
    M = np.array([[INF, 2, INF, 1],
                  [INF, INF, 3, INF],
                  [INF, INF, INF, 1],
                  [INF, INF, INF, INF]])
    afficher_graphe(M)