#Archivo que emplea el codificador tiktoken para la tokenización del Pater Noster en diferentes idiomas
#Enlace en el que se consultaron las distintas versiones del Padre NuESTRO: https://es.askingbox.com/informacion/padre-nuestro-en-otros-idiomas#indonesio
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")

pater_noster = enc.encode("introducir aquí texto a tokenizar")

print (pater_noster)
print(len(pater_noster))

