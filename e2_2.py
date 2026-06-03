import graphviz
import numpy as np
from matplotlib.pylab import dot
def afficher_graphe(M, chemin): 
    n = len(M)
    # Création du graphe de gauche à droite avec Graphviz
    dot = graphviz.Digraph(graph_attr={'rankdir' : 'LR'})

    for i in range(n):
        if i in chemin:
            # Nœuds du chemin en rouge
            dot.node(str(i), str(i), color='red', fontcolor='black', fontweight='bold')
        else:
            # Autres nœuds en noir
            dot.node(str(i), str(i), fontcolor='black')

    for i in range(n):
        for j in range(n):
            # Affiche seulement les arêtes avec poids fini
            if M[i, j] != float('inf'):
                weight = int(M[i, j]) if M[i, j] == int(M[i, j]) else f"{M[i, j]:.1f}"
                if (str(i), str(j)) in [(str(chemin[k]), str(chemin[k+1])) for k in range(len(chemin)-1)]:
                    # Arêtes du chemin en rouge
                    dot.edge(str(i), str(j), label=str(weight), color='red', penwidth='3', fontcolor='red', fontweight='bold')
                else :
                    # Autres arêtes en gris
                    dot.edge(str(i), str(j), label=str(weight), color='gray', penwidth='1.5')

    # Affiche le graphe
    dot.view()

# Exemple
if __name__ == "__main__":
    INF = float('inf')
    M = np.array([[INF, 2, INF, 1],
                [INF, INF, 3, INF],
                [INF, INF, INF, 1],
                [INF, INF, INF, INF]])

    afficher_graphe(M, [0, 0, 1, 2, 3])