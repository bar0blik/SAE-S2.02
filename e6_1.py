import e3
import e4_1
import time

import e4_2

def temps_dij(n: int):
    # Graphe aléatoire de taille n
    M = e3.graphe2(n, 0.3, 1, 10)
    debut = time.perf_counter()
    # Appel à la fonction Dijkstra sur le graphe M avec le sommet 0 comme origine
    res = e4_1.Dijkstra(M, 0)
    fin = time.perf_counter()
    return fin - debut

def temps_bf(n: int):
    # Graphe aléatoire de taille n
    M = e3.graphe2(n, 0.3, 1, 10)
    debut = time.perf_counter()
    # Appel à la fonction Bellman-Ford sur le graphe M avec le sommet 0 comme origine
    res = e4_2.Bellman_Ford(M, 0)
    fin = time.perf_counter()
    return fin - debut

