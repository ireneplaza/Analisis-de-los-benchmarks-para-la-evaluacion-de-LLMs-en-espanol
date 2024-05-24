#Archivo empleado para obtener información acerca de las respuestas de los modelos a los tests en diferentes idiomas.
import pandas as pd

def procesar_archivo(archivo, idioma):
    df = pd.read_excel(archivo)

    aciertos = sum(df['Solución'] == df['Respuesta'])
    total_preguntas = len(df)
    porcentaje_aciertos = (aciertos / total_preguntas) * 100

    # Nueva columna: Probabilidad de acierto
    probabilidad_acierto = df[df['Respuesta'] == df['Solución']]['Probabilidad'].sum()

    # Nueva columna: Tasa de probabilidad de acierto (%)
    tasa_probabilidad_acierto = (probabilidad_acierto / aciertos) * 100 if aciertos != 0 else 0

    nuevo_df = pd.DataFrame({'Idioma': [idioma],
                             'Número de aciertos': [aciertos],
                             'Número de fallos': [total_preguntas - aciertos],
                             'Porcentaje aciertos': [porcentaje_aciertos],
                             'Tasa de probabilidad de acierto (%)': [tasa_probabilidad_acierto]})
                             
    return nuevo_df

# Procesar el primer archivo
df_ingles = procesar_archivo('archivo_respuestas_ingles.xlsx', 'Inglés')
# Procesar el segundo archivo
df_espanol_chatgpt = procesar_archivo('archivo_respuestas_traducido_chatgpt.xlsx', 'Español GPT')
# Procesar el tercer archivo
df_espanol_azure = procesar_archivo('archivo_respuestas_traducido_azure.xlsx', 'Español Azure')

# Concatenar los DataFrames
resultado_final = pd.concat([df_ingles, df_espanol_chatgpt, df_espanol_azure], ignore_index=True)

# Guardar el resultado en un archivo Excel
resultado_final.to_excel('resultados_completos.xlsx', index=False)


