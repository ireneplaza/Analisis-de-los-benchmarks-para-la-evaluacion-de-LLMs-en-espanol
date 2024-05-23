import pandas as pd
import requests
import uuid
def translate_text(text, from_lang, to_lang):
    # Add your key and endpoint
    key = "f720465e3f9c4babb16b1d5ae5c99053"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource.
    location = "westeurope"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': from_lang,
        'to': to_lang
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{'text': text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print("Respuesta de la API:", response)
    
    translated_text = response[0]['translations'][0]['text']
    return translated_text

excel_file_path = 'miscellaneous_original.xlsx'
df = pd.read_excel(excel_file_path)

translated_df = df.applymap(lambda x: translate_text(str(x), 'en', 'es') if isinstance(x, str) else x)

translated_excel_path = 'trad.xlsx'
translated_df.to_excel(translated_excel_path, index=False)

print("Excel traducido guardado en:", translated_excel_path)
