from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

def preguntar(sistema, usuario, temperature=0.7, max_tokens=500):
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": sistema},
            {"role": "user", "content": usuario}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return respuesta.choices[0].message.content

# ── PRUEBA 1: Específico vs vago ──────────────────────

print("=== PROMPT VAGO ===")
print(preguntar("Eres un asistente útil.", "Háblame de Python"))

print("\n=== PROMPT ESPECÍFICO ===")
print(preguntar(
    "Eres un asistente útil.",
    "Explícame qué es una lista en Python, para qué se usa y dame 2 ejemplos simples."
))

# ── PRUEBA 2: Sin rol vs con rol ──────────────────────
print("\n=== SIN ROL ===")
print(preguntar(
    "Eres un asistente útil.",
    "Explícame qué es la recursividad."
))

print("\n=== CON ROL ===")
print(preguntar(
    "Eres un profesor de programación experto y paciente que explica conceptos difíciles con analogías del mundo real, ejemplos simples y mucho humor.",
    "Explícame qué es la recursividad."
))

# ── PRUEBA 3: Sin formato vs con formato ──────────────
print("\n=== SIN FORMATO ===")
print(preguntar(
    "Eres un asistente útil.",
    "Explícame las diferencias entre listas y diccionarios en Python."
))

print("\n=== CON FORMATO ===")
print(preguntar(
    "Eres un asistente útil.",
    """Explícame las diferencias entre listas y diccionarios en Python.
Responde exactamente en este formato:
1. Definición de lista
2. Definición de diccionario
3. Diferencias clave
4. Ejemplo de código de cada uno"""
))

# ── PRUEBA 4: Few-shot prompting ──────────────────────
print("\n=== FEW-SHOT ===")
print(preguntar(
    "Eres un traductor de español a inglés formal.",
    """Traduce estas frases al inglés formal:

Español: "Hola, ¿cómo estás?"
Inglés: "Good morning, how are you?"

Español: "Muchas gracias por tu ayuda"
Inglés: "Thank you very much for your assistance"

Español: "Necesito hablar contigo urgentemente"
Inglés:"""
))

# ── PRUEBA 5: Chain of Thought ────────────────────────
print("\n=== SIN CHAIN OF THOUGHT ===")
print(preguntar(
    "Eres un asistente útil.",
    "Si tengo una lista [3, 7, 2, 9, 1], ¿cómo la ordeno y calculo la media en Python?"
))

print("\n=== CON CHAIN OF THOUGHT ===")
print(preguntar(
    "Eres un asistente útil.",
    """Si tengo una lista [3, 7, 2, 9, 1], ¿cómo la ordeno y calculo la media en Python?
Piensa paso a paso:
1. Primero explica qué necesitas hacer
2. Luego explica qué funciones de Python usarías y por qué
3. Finalmente escribe el código completo con comentarios"""
))
