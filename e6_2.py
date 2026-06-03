import numpy as np
import matplotlib.pyplot as plt

from e6_1 import temps_dij, temps_bf

def experience():
    N = range(2, 201)
    temps_dijkstra = []
    temps_bellman = []

    for n in N:
        #moyenne sur plusieurs exécutions
        nb_tests = 5

        td = 0
        tb = 0

        for _ in range(nb_tests):
            td += temps_dij(n)
            tb += temps_bf(n)
        temps_dijkstra.append(td / nb_tests)
        temps_bellman.append(tb / nb_tests)


    #Graphique classique
    plt.figure(figsize=(10, 6))
    plt.plot(N, temps_dijkstra, label="Dijkstra")
    plt.plot(N, temps_bellman, label="Bellman-Ford")
    plt.xlabel("Nombre de sommets n")
    plt.ylabel("Temps (s)")
    plt.title("Temps d'exécution")
    plt.legend()
    plt.grid()
    plt.show()


    # Graphique log-log

    log_n = np.log(N)
    log_d = np.log(temps_dijkstra)
    log_b = np.log(temps_bellman)
    a_d, b_d = np.polyfit(log_n, log_d, 1)
    a_b, b_b = np.polyfit(log_n, log_b, 1)
    print(f"Exposant Dijkstra ≈ {a_d:.3f}")
    print(f"Exposant Bellman-Ford ≈ {a_b:.3f}")
    plt.figure(figsize=(10, 6))
    plt.plot(log_n, log_d, label=f"Dijkstra (a={a_d:.2f})")
    plt.plot(log_n, log_b, label=f"Bellman-Ford (a={a_b:.2f})")
    plt.xlabel("log(n)")
    plt.ylabel("log(temps)")
    plt.title("Représentation log-log")
    plt.legend()
    plt.grid()
    plt.show()

experience()