import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

# Texto de ejemplo
text = "NLTK es una biblioteca de Python para procesamiento de lenguaje natural. Es muy útil para tareas de PLN."

# Tokenización de palabras
words = word_tokenize(text)

# Etiquetado de partes del discurso (POS tagging)
tagged = nltk.pos_tag(words)

# Definición de la gramática para chunking
# NP: Frase sustantiva (noun phrase)
# VP: Frase verbal (verb phrase)
grammar = """
    NP: {<DT>?<JJ>*<NN.*>}
    VP: {<VB.*><NP|PP|CLAUSE>+$}
    CLAUSE: {<NP><VP>}
    PP: {<IN><NP>}
"""

# Creación del analizador (parser) de chunking
parser = RegexpParser(grammar)

# Aplicación del analizador al texto etiquetado
result = parser.parse(tagged)

# Visualización del resultado
print(result)
result.draw()
