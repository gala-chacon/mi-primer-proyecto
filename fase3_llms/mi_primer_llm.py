from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()
stream = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Eres un asistente útil y conciso."
        },
        {
            "role": "user",
            "content": "Explícame qué es la inteligencia artificial en 3 párrafos."
        }
    ],
    temperature=0.7,
    max_tokens=400,
    stream=True 
)
for chunk in stream:
    contenido = chunk.choices[0].delta.content
    if contenido is not None:
        print(contenido, end="", flush=True)

print()

