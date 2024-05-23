# Archivo usado para realizar consultas a la API del modelo. 
#Se le proporciona un test MMLU para que responda a las preguntas, y guarde dichas respuestas, junto a otros parametros, en un nuevo archivo.

import requests
import pandas as pd
from math import exp

# Carga el archivo Excel con las preguntas 
df = pd.read_excel("miscellaneous_modificado.xlsx")  

# Define la URL de la API
url = "https://api.openai.com/v1/chat/completions"

# Define la clave de API
api_key = "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"

# Listas para guardar información a incluir en el Excel con los resultados
preguntas = []
respuestas = []
soluciones = []
probabilidades = []
top_tokens_list = []
top_probabilities_list = []

for index, row in df.iterrows():
    pregunta = row["Pregunta"]
    respuesta = row["Opciones_Respuesta"]
    solucion = row["Solución"]
    
    messages = [{"role": "user", "content": pregunta}] 

    data = {
        "model": "gpt-3.5-turbo",  #Modelo GPT a utilizar
        "messages": messages,
        "max_tokens": 100,  # Número máximo de tokens en la respuesta
        "logprobs": True, # Muestra las logprobs de los tokens
        "top_logprobs": 5, # Número de logprobs a mostrar
        "temperature": 0 # Valor para obtener probs más equilibrados
    }

    # Define los encabezados de la solicitud con la clave de API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Realiza la solicitud POST a la API
    response = requests.post(url, json=data, headers=headers)
    
    print("Pregunta:", pregunta)
    
    # Comprueba que la solicitud se haya realizado con éxito y guarda la respuesta JSON
    if response.status_code == 200: 
        response_json = response.json() 
        
        # Obtiene la respuesta de la API y la imprime
        respuesta_texto = response_json['choices'][0]['message']['content']
        respuesta = respuesta_texto.split()[0][0]  
        print("Respuesta:", respuesta)
        
        # Obtiene los logprobs de los 5 top_logprobs de la respuesta
        logprobs = response_json['choices'][0]['logprobs']['content'][0]['top_logprobs']
        
        # Extrae los tokens de logprobs y los guarda en una lista
        top_tokens = [token['token'] for token in logprobs] 
        # Convierte logprobs de cada token en probs y las guarda en una lista
        top_probabilities = [exp(token['logprob']) for token in logprobs] 
        
        # Imprime las probabilidades de las 5 top_logprobs
        print("Probabilidades:")
        for token, prob in zip(top_tokens, top_probabilities):
            print(f"Token: {token}, Probabilidad: {prob}")
            
        # Obtiene la probabilidad de la respuesta
        probabilidad = exp(logprobs[0]['logprob'])

        # Agrega la pregunta, respuesta y probabilidad a las listas correspondientes
        preguntas.append(pregunta)
        respuestas.append(respuesta)  
        soluciones.append(solucion)
        probabilidades.append(probabilidad)
        top_tokens_list.append(top_tokens)
        top_probabilities_list.append(top_probabilities)
        
    else:
        print("Error al realizar la solicitud:", response.text)
        
    print("="*100) 

# Crea un DataFrame con las preguntas, sus respuestas, soluciones y sus probabilidades 
df_resultados = pd.DataFrame({"Pregunta": preguntas, 
                               "Solución": soluciones,
                               "Respuesta": respuestas,    
                               "Probabilidad": probabilidades})

# Añade al DataFrame los cinco tokens de mayor probabilidad y dicha probabilidad
for i in range(5):
    df_resultados[f"Top_token_{i+1}"] = [row[i] if len(row) > i else None for row in top_tokens_list]
    df_resultados[f"Top_prob_{i+1}"] = [row[i] if len(row) > i else None for row in top_probabilities_list]

# Convertimos el DataFrame a un archivo Excel
df_resultados.to_excel("miscellaneous_probs_original.xlsx", index=False)

print ("Los resultados obtenidos se han guardado con éxito en un archivo llamado miscellaneous_probs.xlsx")


