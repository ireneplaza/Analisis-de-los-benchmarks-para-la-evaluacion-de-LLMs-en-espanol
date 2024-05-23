import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def plot_distribucion_probabilidad(dataframe):
    # Filtrar las filas donde 'Respuesta Correcta' sea 0 o 1
    df_filtrado = dataframe[dataframe['Respuesta Correcta'].isin([0, 1])]

    # Normalizar las probabilidades 
    min_probabilidad = df_filtrado['Probabilidad'].min()
    max_probabilidad = df_filtrado['Probabilidad'].max()
    df_filtrado['Probabilidad_Normalizada'] = (df_filtrado['Probabilidad'] - min_probabilidad) / (max_probabilidad - min_probabilidad)

    aciertos = df_filtrado[df_filtrado['Respuesta Correcta'] == 1]['Probabilidad_Normalizada']
    fallos = df_filtrado[df_filtrado['Respuesta Correcta'] == 0]['Probabilidad_Normalizada']

    # Definir el rango de valores para x
    x = np.linspace(0, 1, 100)

    # Calcular la FDP para aciertos y fallos
    FDP_aciertos = stats.gaussian_kde(aciertos)(x)
    FDP_fallos = stats.gaussian_kde(fallos)(x)

    plt.figure(figsize=(10, 6))

    plt.plot(x, FDP_aciertos, color='green', label='Respuesta Correcta')
    plt.plot(x, FDP_fallos, color='red', label='Respuesta Incorrecta')

    plt.xlabel('Probabilidad')
    plt.ylabel('Densidad de Probabilidad')
    plt.title('Función de Densidad de Probabilidad. Versión Original (Inglés), GPT-3.5-Turbo')

    plt.legend()

    plt.savefig('fdp_original_chatgpt35.png')

    plt.show()

df_resultados = pd.read_excel("miscellaneous_analisis_original.xlsx")

plot_distribucion_probabilidad(df_resultados)
