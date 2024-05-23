import pandas as pd
import requests

# Define la URL de la API
url = "https://api.openai.com/v1/chat/completions"

api_key = "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"

def translate_text(text):
    messages = [
        {"role": "user", "content":  f"Traducir {text} al español de forma literal. Tiene que ser literal: no acortar ni reescribir nada." }
    ]

    data = {
        "model": "gpt-4",  # Solo obtiene la traducción correcta con este modelo
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

df = pd.read_excel("miscellaneous_modificado.xlsx")

print("Iniciando traducción...")
for index, row in df.iterrows():
    original_pregunta = row["Pregunta"]
    translated_pregunta = translate_text(original_pregunta)
    df.at[index, "Pregunta"] = translated_pregunta
    
    original_opciones = row["Opciones_Respuesta"]
    translated_opciones = translate_text(original_opciones)
    df.at[index, "Opciones_Respuesta"] = translated_opciones

    print(f"Procesando fila {index + 1} de {len(df)}")

df.to_excel("traducido.xlsx", index=False)

print("Traducción completada. Archivo 'traducido.xlsx' guardado correctamente.")
