#Este archivo selecciona los casos en los que el modelo falla para alguna de las versiones en español.
import pandas as pd

# Leer el archivo Excel
df = pd.read_excel("archivo_analisis_todas_las_versiones.xlsx")

# Función para verificar la condición de 0 y 1s
def check_condition(row):
    return row['Respuesta Correcta Azure'] == 0 or row['Respuesta Correcta ChatGPT'] == 0

# Seleccionar las filas que cumplan con la condición especificada
selected_rows = df[df.apply(check_condition, axis=1)]

# Guardar las filas seleccionadas en otro archivo Excel
output_file = "errores_espanol.xlsx"
selected_rows.to_excel(output_file, index=False)
