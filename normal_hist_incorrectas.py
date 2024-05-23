import pandas as pd
import matplotlib.pyplot as plt
import math

df_resultados = pd.read_excel("miscellaneous_analisis_original.xlsx")

# Normalizar las probabilidades 
min_probabilidad = df_resultados['Probabilidad'].min()
max_probabilidad = df_resultados['Probabilidad'].max()
df_resultados['Probabilidad_Normalizada'] = (df_resultados['Probabilidad'] - min_probabilidad) / (max_probabilidad - min_probabilidad)

incorrecta = df_resultados[df_resultados['Respuesta Correcta'] == 0]

# Crear el histograma 
plt.figure(figsize=(10, 6))
plt.hist(incorrecta['Probabilidad_Normalizada'], color='red', alpha=0.5, label='Respuesta Incorrecta', bins=int(math.sqrt(df_resultados.notnull().sum().sum())))
plt.xlabel('Probabilidad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Probabilidades de las Respuestas incorrectas. Versión Original (Inglés), GPT3.5-Turbo')

media_probabilidades = incorrecta['Probabilidad_Normalizada'].mean()

plt.axvline(x=media_probabilidades, color='blue', linestyle='--')


plt.legend([f'Respuestas Incorrectas', f'Media = {media_probabilidades}'])

plt.grid(True)
plt.savefig("hist_incorrectas_original_gpt35.png")
plt.show()

