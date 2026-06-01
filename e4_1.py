def Dijkstra(M, d):
    n = len(M)
    #Vérifie que les poids sont tous positifs ou infinis
    for i in range(n):
        for j in range(n):
            if M[i, j] != float('inf') and M[i, j] < 0:
                return "Dijkstra ne fonctionne pas avec des poids négatifs"

    #Initialisation des dictionnaires de distances et de prédécesseurs
    dist = {}
    pred = {}
    for i in range(n):
        dist[i] = float('inf')
        pred[i] = None
    dist[d] = 0
    pred[d] = d


    A = []
    not_in_A = []
    for i in range(n):
        not_in_A.append(i)

    # Algorithme de Dijkstra
    while not_in_A:
        s = not_in_A[0]
        min_dist = dist[s]
        for x in not_in_A[1:]:
            if dist[x] < min_dist:
                min_dist = dist[x]
                s = x
        if dist[s] == float('inf'):
            break
        not_in_A.remove(s)
        
        A.append(s)

        # Relâcher les arêtes sortantes de s
        for t in not_in_A:
            if M[s, t] != float('inf'):
                nouvelle_distance = dist[s] + M[s, t]
                if nouvelle_distance < dist[t]:
                    dist[t] = nouvelle_distance
                    pred[t] = s

    # Construire le résultat
    resultat = {}
    for s in range(n):
        if s == d:
            continue
        
        if dist[s] == float('inf'):
            resultat[s] = "sommet non joignable à " + str(d) + " par un chemin dans le graphe G"
        else:
            chemin = []
            courant = s
            while courant is not None:
                chemin.append(courant)
                if courant == d:
                    break
                courant = pred[courant]
            chemin.reverse()
            resultat[s] = {"longueur": dist[s], "chemin": chemin}

    return resultat