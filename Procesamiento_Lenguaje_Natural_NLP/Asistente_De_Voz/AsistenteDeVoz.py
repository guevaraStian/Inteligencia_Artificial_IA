#pip install pipwin
#pip install speechrecognition 
#pip install --upgrade speechrecognition
import pyaudio
import webbrowser
import speech_recognition as sr
r = sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz: ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio, language="es-ES")
            print('Lo que dijiste fue : {}'.format(text))
            print(text)
            if "Amazon" in text:
                webbrowser.open('https://amazon.es')
            if "noticias" in text:
                webbrowser.open('https://elespectador.com')
                webbrowser.open('https://eltiempo.com')
                webbrowser.open('https://cnnespanol.cnn.com')
                webbrowser.open('http://infobae.com')
                webbrowser.open('http://elcolobiano.com')
            if "google" in text:
                webbrowser.open('https://google.com')
            if "redes sociales" in text:
                webbrowser.open('https://facebook.com')
                webbrowser.open('https://x.com')
                webbrowser.open('https://instagram.com')
            if "correos" in text:
                webbrowser.open('https://outlook.com')
                webbrowser.open('https://gmail.com')
            if "videos" in text:
                webbrowser.open('https://youtube.com')
                webbrowser.open('https://tiktok.com')
            if "como estas?" in text:
                print("Bien y tu?")
        except:
            print('No te he entendido')