
# ----------------------------
# pip install openai-whisper edge-tts
# ----------------------------
import whisper
import random
import asyncio
import edge_tts
import pyttsx3
#texto = "a e i o u b c d a r i o"
texto =  input("Por favor, Ingrese minimo 3 palabras: ")



def texto_a_wav(texto, archivo="voz.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(texto, archivo)
    engine.runAndWait()

texto_a_wav(texto)


# --------------------------
# 1. Transcribir WAV con Whisper
# --------------------------
def transcribir_wav(path_wav):
    modelo = whisper.load_model("small")  # puedes usar "base" o "medium"
    resultado = modelo.transcribe(path_wav)
    texto = resultado["text"]
    print("Transcripción:", texto)
    return texto

# --------------------------
# 2. Separar palabras
# --------------------------
def separar_palabras(texto):
    palabras = texto.strip().split()
    return palabras

# --------------------------
# 3. Mezclar palabras aleatoriamente
# --------------------------
def mezclar_palabras(palabras, longitud=None):
    if longitud is None:
        longitud = len(palabras)

    palabras_mezcladas = random.sample(palabras, len(palabras))
    nuevo_texto = " ".join(palabras_mezcladas[:longitud])
    return nuevo_texto

# --------------------------
# 4. Generar audio con Edge-TTS
# --------------------------
async def texto_a_audio(texto, salida="salida.wav"):
    comunicador = edge_tts.Communicate(texto, voice="es-ES-ElviraNeural")
    await comunicador.save(salida)
    print("Audio generado:", salida)

# --------------------------
# 5. Flujo completo
# --------------------------
def procesar_audio(path="entrada.wav"):
    # 1. Transcripción
    texto_original = transcribir_wav(path)

    # 2. Separar palabras
    palabras = separar_palabras(texto_original)

    # 3. Generar texto aleatorio
    nuevo_texto = mezclar_palabras(palabras)
    print("Texto generado:", nuevo_texto)

    variable = nuevo_texto
    with open("Palabras_Aleatorias.txt", "w", encoding="utf-8") as f:
        f.write(variable)

    print("Archivo creado correctamente.")

    # 4. Generar audio
    asyncio.run(texto_a_audio(nuevo_texto, "salida.wav"))

    return texto_original, nuevo_texto


# --------------------------
# EJECUCIÓN
# --------------------------
texto_o, texto_n = procesar_audio("voz.wav")

print("\nTexto original:\n", texto_o)
print("\nTexto generado aleatorio:\n", texto_n)














