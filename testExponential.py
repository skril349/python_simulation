import matplotlib.pyplot as plt
import numpy as np

def generar_exponencial_aleatoria():
    # Generar un arreglo de tiempo de 0 a 2 minutos con incremento de 0.01
    tiempo_crecimiento = np.arange(0, 1, 0.01)
    tiempo_decrecimiento = np.arange(1, 2, 0.01)

    # Generar exponencial creciente invertida de 0 a 1: 2 * (1 - e^(-10 * x))
    valores_crecimiento = 2 * (1 - np.exp(-10 * tiempo_crecimiento))

    # Generar exponencial decreciente de 1 a 2: 2 * e^(-10 * (x - 1))
    valores_decrecimiento = 2 * np.exp(-10 * (tiempo_decrecimiento - 1))

    # Combinar los arreglos de tiempo y valores
    tiempo = np.concatenate([tiempo_crecimiento, tiempo_decrecimiento])
    valores = np.concatenate([valores_crecimiento, valores_decrecimiento])

    # Devolver el tiempo y los valores generados
    return tiempo, valores

# Generar gráfico aleatorio
tiempo, valores = generar_exponencial_aleatoria()
plt.plot(tiempo, valores)
plt.xlabel('Tiempo')
plt.ylabel('Valores')
plt.title('Carga y Descarga de un Condensador')
plt.grid(True)

# Calcular la constante de tiempo (5τ)
constante_tiempo = 5 * 0.01  # Incremento de tiempo

# Encontrar el índice en el arreglo de tiempo donde se alcanza 5τ
indice_crecimiento = np.where(tiempo >= constante_tiempo)[0][0]
indice_decrecimiento = np.where(tiempo >= 1 + constante_tiempo)[0][0]

# Marcar los puntos de 5τ en el gráfico
plt.scatter(tiempo[indice_crecimiento], valores[indice_crecimiento], color='red', label='5τ creciente')
plt.scatter(tiempo[indice_decrecimiento], valores[indice_decrecimiento], color='blue', label='5τ decreciente')
plt.legend()

plt.show()
