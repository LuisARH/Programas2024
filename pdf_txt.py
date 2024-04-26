import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import os

# Descargar los recursos necesarios para NLTK
nltk.download('punkt')

def extraer_texto(pdf_file):
    texto = ''
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            texto += page.extract_text()
    return texto

def procesar_texto(texto):
    tokens = word_tokenize(texto.lower())
    palabras_totales = len(tokens)
    fdist = FreqDist(tokens)
    palabras_unicas = len(fdist.hapaxes())
    palabras_comunes = fdist.most_common(20)
    return palabras_totales, palabras_unicas, fdist, palabras_comunes

def graficar_frecuencia(palabras_comunes):
    palabras, frecuencias = zip(*palabras_comunes)
    plt.figure(figsize=(10, 6))
    plt.bar(palabras, frecuencias, color='skyblue')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title('20 palabras más comunes')
    plt.xticks(rotation=45)
    plt.show()

def guardar_texto_en_txt(texto, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        file.write(texto)

if __name__ == "__main__":
    # Solicitar al usuario el nombre del archivo PDF
    archivo_pdf = input("Por favor, introduce el nombre del archivo PDF que deseas procesar: ")

    # Validar si el archivo es un PDF
    if not archivo_pdf.lower().endswith('.pdf'):
        print("El archivo proporcionado no es un archivo PDF.")
    elif not os.path.exists(archivo_pdf):
        print("El archivo especificado no existe.")
    else:
        # Extraer texto del archivo PDF
        texto = extraer_texto(archivo_pdf)

        # Guardar texto en un archivo de texto
        nombre_archivo_txt = os.path.splitext(archivo_pdf)[0] + '.txt'
        guardar_texto_en_txt(texto, nombre_archivo_txt)
        print(f"El texto ha sido guardado en {nombre_archivo_txt}")

        # Procesar texto
        palabras_totales, palabras_unicas, fdist, palabras_comunes = procesar_texto(texto)

        # Mostrar resultados
        print("Palabras totales:", palabras_totales)
        print("Palabras que aparecen solo una vez:", palabras_unicas)
        print("Distribución de frecuencia:", fdist)
        print("20 palabras más comunes:", palabras_comunes)

        # Graficar las 20 palabras más comunes
        graficar_frecuencia(palabras_comunes)
