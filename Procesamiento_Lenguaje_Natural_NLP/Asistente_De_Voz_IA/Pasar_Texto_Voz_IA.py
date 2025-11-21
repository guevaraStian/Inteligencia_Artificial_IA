#Software que pasa de texto a voz
#Primero ejecutamos la descarga de librerias pip install pyttsx3
import pyttsx3

def convertir_texto_a_mp3(texto, nombre_archivo_mp3):
    # Guardamos en una variable la iniciacion de la libreria pyttsx3
    variable_pyttsx = pyttsx3.init()

    # Se guarda la velocidad de la voz y el volumen a escuchar
    variable_pyttsx.setProperty('rate', 150)  # Velocidad de la voz
    variable_pyttsx.setProperty('volume', 1)  # Volumen (de 0.0 a 1.0)

    # Guardar el audio en un archivo mp3
    variable_pyttsx.save_to_file(texto, nombre_archivo_mp3)

    # Ejecutar el proceso de conversión a voz
    variable_pyttsx.runAndWait()

    print(f"El archivo de audio se ha guardado como {nombre_archivo_mp3}")

# Ejemplo de uso
texto = input("Introduce el texto que quieres convertir en sonido: ")
nombre_archivo_mp3 = input("Introduce el nombre del archivo MP3 (con .mp3 al final): ")

convertir_texto_a_mp3(texto, nombre_archivo_mp3)