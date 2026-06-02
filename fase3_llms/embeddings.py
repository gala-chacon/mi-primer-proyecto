from google import genai
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(texto):
    resultado = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texto
    )
    return np.array(resultado.embeddings[0].values)

def similitud(emb1, emb2):
    return np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))

# ── PRUEBA 1: Generar embeddings ──────────────────────
textos = [
    "Me encanta programar en Python",
    "Python es mi lenguaje de programación favorito",
    "El fútbol es el deporte más popular del mundo",
]

embeddings = [get_embedding(t) for t in textos]
print("Dimensiones del embedding:", len(embeddings[0]))

# ── PRUEBA 2: Similitud entre textos ─────────────────
print("\n=== SIMILITUD ENTRE TEXTOS ===")
print(f"Python vs Python:  {similitud(embeddings[0], embeddings[1]):.4f}")
print(f"Python vs fútbol:  {similitud(embeddings[0], embeddings[2]):.4f}")

# ── PRUEBA 3: Búsqueda semántica ─────────────────────
documentos = [
    "Python es ideal para inteligencia artificial",
    "Me gusta el café por las mañanas",
    "scikit-learn es una librería de Machine Learning",
    "El Real Madrid ganó la Champions",
    "Los LLMs son modelos de lenguaje muy potentes",
]

consulta = "¿Qué lenguajes se usan en IA?"

emb_consulta = get_embedding(consulta)
emb_docs = [get_embedding(d) for d in documentos]

print(f"\n=== BÚSQUEDA: '{consulta}' ===")
resultados = [(documentos[i], similitud(emb_consulta, emb_docs[i])) for i in range(len(documentos))]
resultados.sort(key=lambda x: x[1], reverse=True)

for doc, score in resultados:
    print(f"{score:.4f} → {doc}")
    

