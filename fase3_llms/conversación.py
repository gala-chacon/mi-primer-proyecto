from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

historial = [
    {
        "role": "system",
        "content": "Eres un asistente simpático y con buena memoria. Recuerdas todo lo que te cuenta el usuario."
    }
]

def chat (mensaje):
    historial.append({"role": "user", "content": mensaje})
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historial,
        temperature=0.7,
        max_tokens=500
    )
    contenido = respuesta.choices[0].message.content
    historial.append({"role": "assistant", "content": contenido})

    return contenido

print(chat("Hola, me llamo Gala y vivo en la Línea de la Concepción."))
print("---")
print(chat("¿Recuerdas cómo me llamo y dónde vivo?"))
print("---")
print(chat("Y que sabes de la Línea de la Concepción?"))
