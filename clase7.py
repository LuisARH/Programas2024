import nltk
nltk.download("punkt")

archivo_nombre="texto1.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

print("\n\n\n\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
palabras_total=len(tokens)
print("El total de palabras es de: ", palabras_total )