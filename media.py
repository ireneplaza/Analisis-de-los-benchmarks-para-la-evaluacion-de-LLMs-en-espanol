import pandas as pd

# Nombre del archivo Excel
archivo_excel = "miscellaneous_analisis_original.xlsx"

# Leer el archivo Excel en un DataFrame de Pandas
df = pd.read_excel(archivo_excel)

# Filtrar las filas donde 'Respuesta Correcta' es igual a 1
respuestas_correctas = df[df['Respuesta Correcta'] == 1]

# Calcular el número de aciertos
numero_aciertos = len(respuestas_correctas)

# Calcular la suma de las probabilidades de los tokens en los que ha acertado
suma_probabilidades_aciertos = respuestas_correctas['Probabilidad'].sum()

# Calcular la tasa de aciertos
if numero_aciertos > 0:
    tasa_aciertos = (suma_probabilidades_aciertos / numero_aciertos) * 100
else:
    tasa_aciertos = 0

# Mostrar los resultados
print(f"Número de aciertos: {numero_aciertos}")
print(f"Tasa de aciertos: {tasa_aciertos:.2f}%")
