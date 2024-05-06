import pyttsx3

def leer_texto_en_voz(nombre_archivo):
    try:
        # Abrir el archivo de texto
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            texto = file.read()

        # Inicializar el motor de texto a voz
        engine = pyttsx3.init()

        # Configurar la velocidad de lectura
        engine.setProperty('rate', 150)

        # Leer el texto en voz
        engine.say(texto)
        engine.runAndWait()
    except Exception as e:
        print("Error:", e)

def main():
    nombre_archivo = "word.txt"  # Nombre del archivo de texto

    # Llamar a la función para leer el texto en voz
    leer_texto_en_voz(nombre_archivo)

if __name__ == "__main__":
    main()
