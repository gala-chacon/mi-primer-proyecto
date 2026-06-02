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

recetas = [
    "Paella valenciana con pollo y conejo",
    "Gazpacho andaluz con tomate y pepino",
    "Tortilla española de patatas y cebolla",
    "Brownie de chocolate con nueces",
    "Ensalada césar con pollo a la plancha",
    "Lentejas estofadas con chorizo",
    "Tarta de queso al horno",
    "Gambas al ajillo con guindilla",
]
embeddings = [get_embedding(r) for r in recetas]

consultas = [
    "Quiero algo dulce de postre",
    "Tengo ganas de marisco",
    "Algo típico español"
]
for c in consultas:
    emb = get_embedding(c)
    similitudes = [similitud(emb, e) for e in embeddings]
    resultados = sorted(enumerate(similitudes), key=lambda x: x[1], reverse=True)[:3]
    print(f"\nConsulta: '{c}'")
    for i, (indice, score) in enumerate(resultados):
        print(f"  {i+1}. '{recetas[indice]}' (similitud: {score:.4f})")
        