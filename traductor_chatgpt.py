#Traductor basado en la API de ChatGPT, empleado para obtener las traducciones automáticas necesarias.
import pandas as pd
import requests

# Define la URL de la API
url = "https://api.openai.com/v1/chat/completions"

api_key = "introducir aquí api_key"

def translate_text(text):
    messages = [
        {"role": "user", "content":  f"Traducir {text} al español." }
    ]

    data = {
        "model": "gpt-4",  # Modelo empleado para la traducción
        "messages": messages,
        "max_tokens": 200,  # Número máximo de tokens en la respuesta
        "temperature": 0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=data, headers=headers)
    translation = response.json()["choices"][0]["message"]["content"]

    return translation

df = pd.read_excel("testMMLU.xlsx")

print("Iniciando traducción...")
for index, row in df.iterrows():
    original_pregunta = row["Pregunta"]
    translated_pregunta = translate_text(original_pregunta)
    df.at[index, "Pregunta"] = translated_pregunta
    
    original_opciones = row["Opciones_Respuesta"]
    translated_opciones = translate_text(original_opciones)
    df.at[index, "Opciones_Respuesta"] = translated_opciones

    print(f"Procesando fila {index + 1} de {len(df)}")

df.to_excel("test_traducido_gpt.xlsx", index=False)

print("Traducción completada. Archivo 'traducido.xlsx' guardado correctamente.")
