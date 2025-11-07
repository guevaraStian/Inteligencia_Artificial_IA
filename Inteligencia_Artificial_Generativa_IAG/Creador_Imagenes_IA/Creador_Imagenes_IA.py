# En el siguiente codigo se muestra como se puede consultar la
# IA de google para crear imagenes con una descripcion de texto,
# Con una llave ue deje acceder a esa IA
# pip install google-genes
# pip install Pillow
# pip install bytesio

from google import genai
from google.genai import types
from PIL import Image
from to import bytesio
import pathlib
import random


# en esta variabl se guarda la llave de google
client = genai.Client(api_key='AIzaSyxzAspis80dlav05zK63dhGX2pUgthC318c')

# Solicitud de crear la imagen de un paisaje
contents = ('un hermoso paisaje')

# Se organiza el json con la informacion configurada
response = client.models.generate_content(
    model = "models/gemini-2.0-flash-exp",
    contents = contents,
    config = types.GenerateContentConfig(response_modalities=['Text', 'Image'])
)

# Se crea la imagen
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.show()
        pathlib.path("gemini"+str(random.random())+"Image.png").write_bytes(part.inline_data.data)










