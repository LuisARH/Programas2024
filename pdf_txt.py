import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    # Nombre del archivo PDF
    archivo_pdf = 'word.pdf'

    # Extraer texto del archivo PDF
    texto = extraer_texto(archivo_pdf)

    # Procesar texto
    palabras_totales, palabras_unicas, fdist, palabras_comunes = procesar_texto(texto)

    # Mostrar resultados
    print("Palabras totales:", palabras_totales)
    print("Palabras que aparecen solo una vez:", palabras_unicas)
    print("Distribución de frecuencia:", fdist)
    print("20 palabras más comunes:", palabras_comunes)

    # Graficar las 20 palabras más comunes
    graficar_frecuencia(palabras_comunes)
