import graphviz
import numpy as np
from matplotlib.pylab import dot
def afficher_graphe(M): 
    n = len(M)
    dot = graphviz.Digraph()


    for i in range(n):
         # Autres nœuds en bleu clair
        dot.node(str(i), str(i), fillcolor='lightblue', fontcolor='black')

    for i in range(n):
        for j in range(n):
            if M[i, j] != float('inf') and M[i, j] >= 0:
                weight = int(M[i, j]) if M[i, j] == int(M[i, j]) else f"{M[i, j]:.1f}"
                # Autres arêtes en gris
                dot.edge(str(i), str(j), label=str(weight), color='gray', penwidth='1.5')

    dot.view(cleanup=False)

M = np.array([[0, 2, float('inf'), 1],
              [float('inf'), 0, 3, float('inf')],
              [float('inf'), float('inf'), 0, 1],
              [float('inf'), float('inf'), float('inf'), 0]])
afficher_graphe(M)