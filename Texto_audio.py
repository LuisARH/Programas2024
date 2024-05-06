from gtts import gTTS
import os

def texto_a_audio():
    texto = input("Introduce el texto que deseas convertir a audio: ")
    nombre_archivo_salida = input("Introduce el nombre del archivo de audio de salida (incluyendo la extensión, por ejemplo, audio_salida.mp3): ")
    tts = gTTS(text=texto, lang='ko')
    tts.save(nombre_archivo_salida)
    print("¡El archivo de audio ha sido generado con éxito!")

# Convertir texto a audio
texto_a_audio()

