import pandas as pd

df_resultados = pd.read_excel("miscellaneous_probs_original.xlsx")

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

df_final.to_excel("miscellaneous_analisis_original.xlsx", index=False)

print("Se ha generado el archivo 'miscellaneous_analisis_temp0.xlsx'.")