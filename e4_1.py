def Dijkstra(M, d):
    n = len(M)
    #On vérifie que les poids sont tous positifs ou infinis
    for i in range(n):
        for j in range(n):
            if M[i, j] != float('inf') and M[i, j] < 0:
                return "Dijkstra ne fonctionne pas avec des poids négatifs"

    #On initialise les dictionnaires de distances et de prédécesseurs
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

    #Algorithme de Dijkstra : 
    while not_in_A:
    #On cherche le sommet s avec la plus petite distance :
        #On initialise s au premier somment 
        s = not_in_A[0]
        #On initialise min_dist à la distance de s
        min_dist = dist[s]
        for x in not_in_A[1:]:
            if dist[x] < min_dist:
                #Si on trouve un sommet avec un distance plus petite, on met à jour s et min_dist
                min_dist = dist[x]
                s = x
        if dist[s] == float('inf'):
            #Si la distance est "infini", les sommmets restants ne sont pas joignables dont on peut l'enlever des la liste des sommets à traiter
            break
        not_in_A.remove(s)
        #On ajoute le sommet s à A
        A.append(s)

        #On relache les arêtes sortantes de s
        for t in not_in_A:
            if M[s, t] != float('inf'):
            #Si la distance de s + le poids de l'arête (s, t) est plus petite que la distance actuelle de t, on met à jour la distance de t
                nouvelle_distance = dist[s] + M[s, t]
                if nouvelle_distance < dist[t]:
                    dist[t] = nouvelle_distance
                    pred[t] = s

    #On construit le résultat
    resultat = {}
    for s in range(n):
        if s == d:
            continue
        
        #Si la distance de s est "infini" alors s n'est pas joignable à d par un chemin dans le graphe
        if dist[s] == float('inf'):
            resultat[s] = "sommet non joignable à " + str(d) + " par un chemin dans le graphe"
        else:
        #Sinon on construit le chemin de s à d en remontant les prédécesseurs
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