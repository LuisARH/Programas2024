from transformers import pipeline

# Crear el pipeline de análisis de sentimientos en español
sentiment_pipeline = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Texto a analizar
text = "Me encanta este lugar. Es increíble."

# Obtener resultados
results = sentiment_pipeline(text)

# Imprimir resultados
print(f"Texto: {text}")
print(f"Resultados: {results}")
