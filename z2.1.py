import graphviz
import numpy as np

def afficher_graphe(M: np.ndarray, chemin=None, titre="Graphe", nom_fichier="graphe"):
    """
    Affiche un graphe avec GraphViz avec possibilité de mettre en évidence un chemin en rouge
    
    Args:
        M: matrice d'adjacence
        chemin: liste de sommets formant le chemin à afficher en rouge (ex: [0, 2, 3, 1])
        titre: titre du graphe
        nom_fichier: nom du fichier de sortie (sans extension)
    """
    n = len(M)
    
    # Créer un graphe orienté avec GraphViz
    dot = graphviz.Digraph(comment=titre)
    dot.attr(rankdir='LR')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue', fontsize='12')
    dot.attr('graph', label=titre, fontsize='14', fontname='Arial')
    
    # Ensemble des sommets du chemin pour les colorer en rouge
    sommets_chemin = set(chemin) if chemin else set()
    aretes_chemin = set()
    
    if chemin and len(chemin) > 1:
        for i in range(len(chemin) - 1):
            aretes_chemin.add((str(chemin[i]), str(chemin[i+1])))
    
    # Ajouter les nœuds
    for i in range(n):
        if i in sommets_chemin:
            # Nœuds du chemin en rouge
            dot.node(str(i), str(i), fillcolor='red', fontcolor='white', fontweight='bold')
        else:
            # Autres nœuds en bleu clair
            dot.node(str(i), str(i), fillcolor='lightblue', fontcolor='black')
    
    # Ajouter les arêtes
    for i in range(n):
        for j in range(n):
            if M[i, j] != float('inf') and M[i, j] >= 0:
                weight = int(M[i, j]) if M[i, j] == int(M[i, j]) else f"{M[i, j]:.1f}"
                
                if (str(i), str(j)) in aretes_chemin:
                    # Arêtes du chemin en rouge, épaisses
                    dot.edge(str(i), str(j), label=str(weight), color='red', 
                             penwidth='3', fontcolor='red', fontweight='bold')
                else:
                    # Autres arêtes en gris
                    dot.edge(str(i), str(j), label=str(weight), color='gray', penwidth='1.5')
    
    # Afficher le chemin en bas du graphe
    if chemin:
        chemin_str = " → ".join(map(str, chemin))
        dot.attr('graph', label=f"{titre}\nChemin: {chemin_str}", fontsize='14')
    
    # Afficher le graphe
    dot.view(filename=nom_fichier, cleanup=False)
    print(f"Graphe sauvegardé: {nom_fichier}.pdf")