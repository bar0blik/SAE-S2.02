import numpy as np

ex1 = np.array([
    [None, 3, 8, None, None, None],
    [None, None, 2, 5, None, None],
    [None, None, None, -4, None, None],
    [None, 1, 6, None, None, None],
    [None, None, None, None, None, 5],
    [None, None, None, None, -2, None]
])

ex2 = np.array([
    [None, 1, 2, None, None],
    [None, None, 2, 2, None],
    [1, None, None, None, None],
    [1, None, None, None, None],
    [None, 1, None, 2, None]
])

for ex in [ex1, ex2]:
    for i in range(ex.shape[0]):
        for j in range(ex.shape[1]):
            if ex[i, j] is None:
                ex[i, j] = float('inf')

print("Exemple 1 :")
print(ex1)
print("Exemple 2 :")
print(ex2)
