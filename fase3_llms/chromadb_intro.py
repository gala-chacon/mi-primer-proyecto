import faiss
import numpy as np
from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()
client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(texto):
    time.sleep(1)
    resultado = client_gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=texto
    )
    return np.array(resultado.embeddings[0].values, dtype="float32")

# ── Documentos ────────────────────────────────────────
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

# ── Generar embeddings ────────────────────────────────
print("Generando embeddings...")
embeddings = np.array([get_embedding(r) for r in recetas])

# ── Crear índice FAISS ────────────────────────────────
dimension = embeddings.shape[1]  # 3072
indice = faiss.IndexFlatL2(dimension)
indice.add(embeddings)
print(f"✅ {indice.ntotal} recetas guardadas en FAISS")

# ── Buscar ────────────────────────────────────────────
consulta = "Quiero algo dulce de postre"
emb_consulta = np.array([get_embedding(consulta)])

distancias, indices = indice.search(emb_consulta, k=3)

print(f"\nConsulta: '{consulta}'")
for i, idx in enumerate(indices[0]):
    print(f"  {i+1}. {recetas[idx]} (distancia: {distancias[0][i]:.4f})")

for consulta in ["Tengo ganas de marisco", "Algo típico español"]:
    emb_consulta = np.array([get_embedding(consulta)])
    distancias, indices = indice.search(emb_consulta, k=3)
    print(f"\nConsulta: '{consulta}'")
    for i, idx in enumerate(indices[0]):
        print(f"  {i+1}. {recetas[idx]} (distancia: {distancias[0][i]:.4f})")
