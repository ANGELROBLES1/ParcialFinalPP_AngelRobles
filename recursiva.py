import numpy as np
import matplotlib.pyplot as plt
from memory_profiler import profile
from timeit import default_timer as timer

# manual
def regla_del_trapecio_manual(y, x):
    h = x[1] - x[0]  # distancia uniforme
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# coeficientes a_n y b_n
def calcular_coeficientes(f, t, T, n):
    a_n = (2 / T) * regla_del_trapecio_manual(f * np.cos(2 * np.pi * n * t / T), t)
    b_n = (2 / T) * regla_del_trapecio_manual(f * np.sin(2 * np.pi * n * t / T), t)
    return a_n, b_n


def calcular_serie_fourier_recursiva(f, t, T, N):
    coeficientes = [(1 / T) * regla_del_trapecio_manual(f, t), 0.0]
    
    def calcular_recursivo(n):
        if n == 0:
            return []
        coef = calcular_recursivo(n - 1)
        a_n, b_n = calcular_coeficientes(f, t, T, n)
        coef.append((a_n, b_n))
        return coef
    
    return [tuple(coeficientes)] + calcular_recursivo(N)

# Datos
T = 2 * np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sign(np.sin(t))
valores_N = [5, 10, 20, 50, 100]
tiempos_recur = []

# tiempo
for N in valores_N:
    inicio = timer()
    calcular_serie_fourier_recursiva(f, t, T, N)
    fin = timer()
    tiempos_recur.append(fin - inicio)


plt.plot(valores_N, tiempos_recur, label='Recursivo', marker='s')
plt.xlabel('Número de armónicos N')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo - Método Recursivo')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# terminal
print(f"{'N':<5} {'Tiempo Recursivo (s)':<25}")
for n, t in zip(valores_N, tiempos_recur):
    print(f"{n:<5} {t:<25.6f}")
