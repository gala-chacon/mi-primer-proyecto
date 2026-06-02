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
        max_tokens=500,
        stream=True

    )
    print("\mAsistente: ", end="", flush=True)
    contenido = ""
    for chunk in respuesta:
        trozo = chunk.choices[0].delta.content
        if trozo is not None:
            print(trozo, end="", flush=True)
            contenido += trozo
    print("\n")
    historial.append({"role": "assistant", "content": contenido})
print("🤖 Chat iniciado. Escribe ' salir ' para terminar. \n")

while True:
    mensaje = input("Tu: ")
    if mensaje.lower() == "salir":
        print("¡Hasta luego!👋")
        break
    chat(mensaje)
    