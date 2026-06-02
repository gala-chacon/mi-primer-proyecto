from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq()

def preguntar(sistema, usuario, temperature=0.7, max_tokens=500):
    respuesta = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role': 'system', 'content': sistema},
            {'role': 'user', 'content': usuario}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return respuesta.choices[0].message.content

print(preguntar(
    """Eres un profesor de idiomas experto y paciente que explica conceptos difíciles de forma sencilla.," \
    
Responde exactamente en este formato:
1. Explicación breve:
2. Ejemplo con 'la primera palabra':
3. Ejemplo con 'la segunda palabra':"    
4. Truco para recordalo:

No hables de temas que no sean gramática o idiomas.
No respondas en otro formato que no sea el indicado.
No uses tecnicismos difíciles.""",
    "No entiendo la diferencia entre 'since' y 'for' en inglés"
))
