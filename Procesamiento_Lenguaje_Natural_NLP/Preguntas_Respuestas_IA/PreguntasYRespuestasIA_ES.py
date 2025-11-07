#Primero se descarga la libreria open ai con el siguiente comando  "pip install openai"
import os
import openai
import googletrans

key = "Para usar esta aplicacion hay que pedirle a chatgpt una llave ponerla aqui"

# Se inicia la variable que tiene el traductor
traductor = googletrans.Translator()

# Se ingresa la pregunta en español
pregunta = input("Por favor ingrese pregunta en español: ")
ejemplo_pregunta = "¿cuantos continentes hay en el mundo?"

# Se usa el tradutor para pasar la pregunta de español a ingles
traducido = traductor.translate(pregunta, src='es', dest='en')

#Se declara la llave de chatgpt y se configuran las variables de configuracion de openai
openai.api_key = key
response = openai.Completion.create(
  engine="davinci",
  prompt=traducido.text,
  max_tokens=30,
  top_p=1
)
# Prodcedemos a mostrar en pantalla la respuesta de la consulta
print(response["choices"])
