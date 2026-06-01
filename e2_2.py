import graphviz
import numpy as np
from matplotlib.pylab import dot
def afficher_graphe(M, chemin): 
    n = len(M)
    dot = graphviz.Digraph()

    for i in range(n):
        if i in chemin:
            # Nœuds du chemin en rouge
            dot.node(str(i), str(i), color='red', fontcolor='black', fontweight='bold')
        else:
            # Autres nœuds en bleu clair
            dot.node(str(i), str(i), fontcolor='black')

    for i in range(n):
        for j in range(n):
            if M[i, j] != float('inf') and M[i, j] >= 0:
                weight = int(M[i, j]) if M[i, j] == int(M[i, j]) else f"{M[i, j]:.1f}"
                if (str(i), str(j)) in [(str(chemin[k]), str(chemin[k+1])) for k in range(len(chemin)-1)]:
                    dot.edge(str(i), str(j), label=str(weight), color='red', penwidth='3', fontcolor='red', fontweight='bold')
                else :
                    # Autres arêtes en gris
                    dot.edge(str(i), str(j), label=str(weight), color='gray', penwidth='1.5')

    dot.view(cleanup=False)

M = np.array([[0, 2, float('inf'), 1],
              [float('inf'), 0, 3, float('inf')],
              [float('inf'), float('inf'), 0, 1],
              [float('inf'), float('inf'), float('inf'), 0]])

afficher_graphe(M, [0, 0, 1, 2, 3])