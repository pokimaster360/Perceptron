import matplotlib.pyplot as plt
import numpy as np

# Definimos los datos
X = np.array(
    [
        [3, 11],  # True (Índices 0, 1, 2)
        [4, 10],  # True
        [5, 8],  # True
        [3, 5],  # False (Índices 3, 4, 5)
        [5, 6],  # False
        [1, 3],  # False
    ],
    dtype=float,
)

# Separamos los True (primeras 3 filas) y los False (últimas 3 filas)
true_points = X[:3]
false_points = X[3:]

# Graficamos usando scatter para verlos como puntos en un plano cartesiano (X e Y)
plt.scatter(
    true_points[:, 0], true_points[:, 1], color="blue", label="True", s=100
)
plt.scatter(
    false_points[:, 0], false_points[:, 1], color="red", label="False", s=100
)

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)
plt.show()