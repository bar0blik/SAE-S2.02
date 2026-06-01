import numpy as np

def Bellman_Ford(M, d):
    n = len(M)
    # Construire la liste des arêtes à partir de la matrice
    aretes = []
    # On parcours tous les elts de la matrice
    for i in range(n):
        for j in range(n):
            p = M[i][j]
            # On ignore les infinis
            if np.isinf(p):
                continue
            # On ajoute l'arête (i, j) avec poids p
            aretes.append((i, j, p))

    INF = np.inf

    # On part d'une distance infinie pour tous les sommets sauf d
    dist = [INF] * n
    # On garde un tableau de prédécesseurs pour reconstruire les chemins
    pred = [None] * n
    dist[d] = 0

    # On parcoure toutes les arêtes (n-1) fois maximum
    for _ in range(n - 1):
        changed = False
        # On parcours les arêtes
        for u, v, p in aretes:
            # Si on peut améliorer la distance vers v en passant par u, on met à jour
            if dist[u] != INF and dist[u] + p < dist[v]:
                dist[v] = dist[u] + p
                pred[v] = u
                changed = True
        # Si rien n'a changé pendant ce passage, on arrête d'itérer
        if not changed:
            break

    # Détection des sommets affectés par un cycle négatif
    affectes = [False] * n
    # On parcoure les arêtes
    for u, v, p in aretes:
        # Si on peut encore améliorer la distance vers v, alors v est affecté par un cycle négatif
        if dist[u] != INF and dist[u] + p < dist[v]:
            affectes[v] = True

    # Propager l'effet des cycles négatifs aux sommets atteignables depuis eux
    # construire adjacence pour parcours
    adj = [[] for _ in range(n)] #Tableau de tableaux vides de longueur n
    # Pour chaque arête, on ajoute dans adj au point de départ u, le point d'arrivée v
    for u, v, p in aretes:
        adj[u].append(v)

    # On prend tous les sommets affectés par un cycle négatif
    q = [i for i, a in enumerate(affectes) if a]
    # On parcours q en pour propager les cycles
    while q:
        u = q.pop(0)
        # Pour chaque element de q on affecte tous ses voisins
        for v in adj[u]:
            if not affectes[v]:
                affectes[v] = True
                q.append(v)

    MSG_IMP = "sommet non joignable depuis " + str(d) + " par un chemin dans le graphe G"
    MSG_NEG = ("sommet joignable depuis " + str(d) + " par un chemin dans le graphe G, mais pas\n"
               "de plus court chemin (présence d'un cycle négatif)")

    # Fonction pour reconstruire le chemin depuis d jusqu'à t
    def recup_chemin(t):
        chemin = []
        actuel = t
        # Liste des sommets visités
        visite = []
        # On parcours les sommets non visités
        while actuel is not None and actuel not in visite:
            # On ajoute le sommet actuel au chemin et à la liste des visités
            chemin.append(actuel)
            visite.append(actuel)
            # On remonte vers le prédécesseur du sommet actuel
            actuel = pred[actuel]
        # On inverse le chemin pour l'avoir dans le bon sens
        chemin.reverse()
        return chemin

    result = {}
    for s in range(n):
        # Pas de chemin de d à s
        if dist[s] == INF:
            result[s] = MSG_IMP
        # Chemin de d à s existe mais est affecté par un cycle négatif
        elif affectes[s]:
            result[s] = MSG_NEG
        # Chemin de d à s existe et n'est pas affecté par un cycle négatif
        else:
            result[s] = (dist[s], recup_chemin(s))

    return result


if __name__ == "__main__":
    INF = np.inf
    M = [
        [INF, 1, 4, INF],
        [INF, INF, 1, INF],
        [INF, -3, INF, INF],
        [INF, INF, INF, INF],
    ]

    # Ici 0 -> 1 (1), 1 -> 2 (1), 2 -> 1 (-3) cycle négatif
    out = Bellman_Ford(M, 0)
    for v, info in out.items():
        print(f"Sommet {v}: ", end='')
        if isinstance(info, tuple):
            dist, path = info
            print(f"distance = {dist}, chemin = {path}")
        else:
            print(info)
