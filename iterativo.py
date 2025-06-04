import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

    ####################################
def regla_del_trapecio_manual(y, x):
    h = x[1] - x[0]  #distancia uniforme
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    ####################################

# coeficientes a_n y b_n
def calcular_coeficientes(f, t, T, n):
    a_n = (2 / T) * regla_del_trapecio_manual(f * np.cos(2 * np.pi * n * t / T), t)
    b_n = (2 / T) * regla_del_trapecio_manual(f * np.sin(2 * np.pi * n * t / T), t)
    return a_n, b_n


def calcular_serie_fourier_iterativa(f, t, T, N):
    coeficientes = []
    a0 = (1 / T) * regla_del_trapecio_manual(f, t)
    coeficientes.append((a0, 0.0))  # b0 es 0
    for n in range(1, N + 1):
        a_n, b_n = calcular_coeficientes(f, t, T, n)
        coeficientes.append((a_n, b_n))
    return coeficientes

# Datinhos
T = 2 * np.pi 
t = np.linspace(0, T, 1000, endpoint=False) # 1000 puntos en un período
f = np.sign(np.sin(t)) # función a aproximar
valores_N = [5, 10, 20, 50, 100]
tiempos_iter = []

# tiempo
for N in valores_N:
    inicio = timer()
    calcular_serie_fourier_iterativa(f, t, T, N)
    fin = timer()
    tiempos_iter.append(fin - inicio)


plt.plot(valores_N, tiempos_iter, label='Iterativo', marker='o')
plt.xlabel('Número de armónicos N')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo - Método Iterativo')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# terminal
print(f"{'N':<5} {'Tiempo Iterativo (s)':<25}")
for n, t in zip(valores_N, tiempos_iter):
    print(f"{n:<5} {t:<25.6f}")
