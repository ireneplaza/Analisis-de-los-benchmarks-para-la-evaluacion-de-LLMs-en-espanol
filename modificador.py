import pandas as pd

# Carga el archivo Excel original
df = pd.read_excel("elem_maths_test_modificado.xlsx")

datos_ordenado = []

# Itera sobre las filas del DataFrame original y agrega las entradas al nuevo formato
for index, row in df.iterrows():
    # Busca el índice del primer signo de interrogación en la cadena
    indice_interrogacion = row["Columna_Unica"].find("?")
    
    # Extrae el enunciado de la pregunta hasta el primer signo de interrogación
    enunciado_pregunta = row["Columna_Unica"][:indice_interrogacion + 1].strip()
    
    # Extrae las opciones de respuesta separadas por comas
    opciones_respuesta = [opcion.strip() for opcion in row["Columna_Unica"][indice_interrogacion + 1:].split(",")]
    
    # La respuesta correcta es la última parte
    respuesta_correcta = opciones_respuesta[-1]
    
    # Elimina la respuesta correcta de las opciones de respuesta
    opciones_respuesta = opciones_respuesta[:-1]
    
    # Concatena las opciones de respuesta numeradas con A, B, C, etc., al enunciado de la pregunta
    opciones_pregunta = "".join([f"\n{chr(65 + i)}. {opcion}" for i, opcion in enumerate(opciones_respuesta)])
    
    # Añade las opciones de respuesta numeradas al enunciado de la pregunta
    enunciado_pregunta += f" Please answer:{opciones_pregunta}."  
    
    datos_ordenado.append({"Pregunta": enunciado_pregunta,
                           "Opciones_Respuesta": opciones_respuesta,
                           "Solución": respuesta_correcta})

# Crea un nuevo DataFrame a partir de la lista de datos modificados
df_ordenado = pd.DataFrame(datos_ordenado)

# Guarda el nuevo DataFrame en un archivo Excel
df_ordenado.to_excel("miscellaneous_modificado.xlsx", index=False)

print("Los resultados obtenidos se han guardado con éxito en un archivo llamado miscellaneous_modificado.xlsx.")
