# Este archivo se utiliza una vez obtenidas las respuestas del modelo al test al que se le somete, para realizar un análisis de sus resultados. 
# Genera un nuevo archivo donde indica si el modelo falla o acierta, indicando la probabilidad de la respuesta correcta, tanto en el caso de que sea la respuesta definitva del modelo, como en el caso de que la respuesta correcta se encontrase en uno de los top_5_tokens.
import pandas as pd

df_resultados = pd.read_excel("archivo_respuestas.xlsx")

# Compara los resultados con la solución
df_resultados['Respuesta Correcta'] = (df_resultados['Solución'] == df_resultados['Respuesta']).astype(int)

probabilidades_respuesta_correcta = []

for index, row in df_resultados.iterrows():
    if row['Respuesta Correcta'] == 1:  
        probabilidad_respuesta_correcta = row['Probabilidad']
    else:
        respuesta_correcta = row['Solución']
        probabilidad_respuesta_correcta = 0  # Probabilidad si no encuentra la solucion 
        for i in range(1, 6):
            top_token = row[f"Top_token_{i}"]
            if top_token == respuesta_correcta:
                probabilidad_respuesta_correcta = row[f"Top_prob_{i}"]
                break
    probabilidades_respuesta_correcta.append(probabilidad_respuesta_correcta)

df_resultados['Probabilidad de Respuesta Correcta'] = probabilidades_respuesta_correcta

df_final = df_resultados[['Respuesta Correcta', 'Probabilidad', 'Probabilidad de Respuesta Correcta']]

df_final.to_excel("archivo_analizado.xlsx", index=False)

print("Se ha generado el archivo")
