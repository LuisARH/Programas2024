import docx
import nltk
from nltk.tokenize import word_tokenize

# Función para contar palabras y líneas en un texto
def contar_palabras_lineas(texto):
    palabras = texto.split()
    lineas = texto.split('\n')
    return len(palabras), len(lineas)

# Función para contar la frecuencia de una palabra en el texto
def contar_frecuencia(texto, palabra):
    tokens = word_tokenize(texto)
    frecuencia = tokens.count(palabra)
    return frecuencia

# Función para guardar el texto extraído en un archivo de texto
def guardar_texto(texto, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

# Función principal
def analizar_documento(docx_file, palabra):
    doc = docx.Document(docx_file)
    texto_pagina = ""
    for paragraph in doc.paragraphs:
        texto_pagina += paragraph.text + "\n"

    # Contar palabras y líneas
    num_palabras, num_lineas = contar_palabras_lineas(texto_pagina)
    print("Número de palabras en el documento:", num_palabras)
    print("Número de líneas de texto en el documento:", num_lineas)

    # Contar frecuencia de una palabra
    frecuencia_palabra = contar_frecuencia(texto_pagina, palabra)
    print(f"La palabra '{palabra}' aparece {frecuencia_palabra} veces en el documento.")

    # Guardar texto extraído en un archivo de texto
    if texto_pagina:
        guardar_texto(texto_pagina, "texto_pagina.txt")
        print("Texto extraído guardado en texto_pagina.txt")

    # Cargar el texto del archivo
    with open("texto_pagina.txt", "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    print("----------------------------------------------------------------------")

    # Cargar palabras funcionales en español de NLTK
    palabras_funcionales = nltk.corpus.stopwords.words("spanish")
    for palabra_funcional in palabras_funcionales:
        print(palabra_funcional)

    print("----------------------------------------------------------------------")

    # Tokenizar el texto y eliminar palabras funcionales
    tokens = word_tokenize(texto, "spanish")
    tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

    # Imprimir algunos detalles sobre los tokens
    print(tokens_limpios)
    print("Número total de tokens:", len(tokens))
    print("Número de tokens limpios:", len(tokens_limpios))

    # Crear un objeto Text de NLTK y calcular la distribución de frecuencia
    texto_limpio_nltk = nltk.Text(tokens_limpios)
    distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

    # Graficar las 20 palabras más comunes
    distribucion_limpia.plot(20)

# Ejemplo de uso
documento_word = "word.docx"
palabra_buscada = "dengue"
analizar_documento(documento_word, palabra_buscada)
