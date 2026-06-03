import numpy as np
import random
import time


def graphe_signe_variable(n, p, a, b):
    if p < 0 or p > 1:
        return "p doit être compris entre 0 et 1"
    if n <= 0:
        return "n doit être positif"
    if a >= b:
        return "a doit être inférieur à b"

    M = np.empty((n, n)).astype('float64')
    for i in range(n):
        for j in range(n):
            if random.random() < 1 - p:
                M[i, j] = float('inf')
            else:
                poids = random.randint(a, b - 1)
                if random.random() < 0.5:
                    poids = -poids
                M[i, j] = poids
    return M

def ordre_largeur(M, d) -> list[(int, int, float)]:
    n = len(M)
    visites = [False] * n
    file = [d]
    visites[d] = True
    aretes = []

    # On itere tant que la file n'est pas vide
    while file:
        # On prend le premier sommet u
        u = file.pop(0)
        # On parcours tous les sommets v
        for v in range(n):
            # Si un chemin existe entre u et v et que v n'est pas encore visité, on le visite, on l'ajoute a la pile
            # et on ajoute l'arête (u, v) à la liste des arêtes
            if M[u][v] != float('inf') and not visites[v]:
                visites[v] = True
                file.append(v)
                aretes.append((u, v, M[u][v]))

    return aretes

def ordre_profondeur(M, d) -> list[(int, int, float)]:
    n = len(M)
    visites = [False] * n
    pile = [d]
    visites[d] = True
    aretes = []

    # On itere tant que la pile n'est pas vide
    while pile:
        # On prend le dernier sommet u
        u = pile.pop()
        # On parcours tous les sommets v
        for v in range(n):
            # Si un chemin existe entre u et v et que v n'est pas encore visité, on le visite, on l'ajoute a la pile
            # et on ajoute l'arête (u, v) à la liste des arêtes
            if M[u][v] != float('inf') and not visites[v]:
                visites[v] = True
                pile.append(v)
                aretes.append((u, v, M[u][v]))

    return aretes

def ordre_aleatoire(M, d) -> list[(int, int, float)]:
    n = len(M)
    visites = [False] * n
    pile = [d]
    visites[d] = True
    aretes = []

    # On itere tant que la pile n'est pas vide
    while pile:
        # On prend un sommet u aléatoire dans la pile
        u = pile.pop(np.random.randint(len(pile)))
        # On parcours tous les sommets v
        for v in range(n):
            # Si un chemin existe entre u et v et que v n'est pas encore visité, on le visite, on l'ajoute a la pile
            # et on ajoute l'arête (u, v) à la liste des arêtes
            if M[u][v] != float('inf') and not visites[v]:
                visites[v] = True
                pile.append(v)
                aretes.append((u, v, M[u][v]))
    return aretes

def Bellman_Ford_compteur(M, d, aretes: list[(int, int, float)]):
    n = len(M)

    INF = np.inf

    # On part d'une distance infinie pour tous les sommets sauf d
    dist = [INF] * n
    # On garde un tableau de prédécesseurs pour reconstruire les chemins
    pred = [None] * n
    dist[d] = 0

    # Compteurs
    compteur_tour = 0
    compteur_aretes = 0

    # On parcours toutes les arêtes (n-1) fois maximum
    for _ in range(n - 1):
        compteur_tour += 1

        changed = False
        # On parcours les arêtes
        for u, v, p in aretes:
            compteur_aretes += 1

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
    # On parcours les arêtes
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

    MSG_IMP = "sommet non joignable depuis d par un chemin dans le graphe G"
    MSG_NEG = ("sommet joignable depuis d par un chemin dans le graphe G, mais pas\n"
               "de plus court chemin (présence d’un cycle négatif)")

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
            result[s] = MSG_IMP + "\nNombre de tours: " + str(compteur_tour) + "\nNombre d'arêtes parcourues: " + str(compteur_aretes)
        # Chemin de d à s existe mais est affecté par un cycle négatif
        elif affectes[s]:
            result[s] = MSG_NEG + "\nNombre de tours: " + str(compteur_tour) + "\nNombre d'arêtes parcourues: " + str(compteur_aretes)
        # Chemin de d à s existe et n'est pas affecté par un cycle négatif
        else:
            result[s] = "Chemin: " + str((dist[s], recup_chemin(s))) + "\nNombre de tours: " + str(compteur_tour) + "\nNombre d'arêtes parcourues: " + str(compteur_aretes)

    return result

def Bellman_Ford_largeur(M, d):
    aretes = ordre_largeur(M, d)
    return Bellman_Ford_compteur(M, d, aretes)

def Bellman_Ford_profondeur(M, d):
    aretes = ordre_profondeur(M, d)
    return Bellman_Ford_compteur(M, d, aretes)

def Bellman_Ford_aleatoire(M, d):
    aretes = ordre_aleatoire(M, d)
    return Bellman_Ford_compteur(M, d, aretes)

if __name__ == "__main__":
    M = graphe_signe_variable(100, 0.5, 1, 10)

    variantes = [
        ("largeur", Bellman_Ford_largeur),
        ("profondeur", Bellman_Ford_profondeur),
        ("aleatoire", Bellman_Ford_aleatoire),
    ]

    for nom, fonction in variantes:
        debut = time.perf_counter()
        out = fonction(M, 0)
        fin = time.perf_counter()
        premier = next(iter(out.values()))
        print(f"--- Variante {nom} ---")
        print(f"Temps d'execution: {fin - debut:.6f} s")
        print(f"Exemple de sortie: {premier}")
