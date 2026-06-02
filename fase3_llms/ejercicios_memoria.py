from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq()

SISTEMA = "Eres un agente de viajes simpático"

def llamar_modelo(historial, max_tokens=500):
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historial,
        temperature=0.7,
        max_tokens=max_tokens
    )
    return respuesta.choices[0].message.content

historial = [{"role": "system", "content": SISTEMA}]
ARCHIVO_HISTORIAL = "viajes_historial.json"
def guardar_historial(historial):
    with open(ARCHIVO_HISTORIAL, "w") as f:
        json.dump(historial, f,ensure_ascii=False, indent=4)   
def cargar_historial():
    try:
        with open(ARCHIVO_HISTORIAL, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"role": "system", "content": SISTEMA}]

def chat(mensaje):
    historial = cargar_historial()
    historial.append({"role": "user", "content": mensaje})
    contenido = llamar_modelo(historial)
    historial.append({"role": "assistant", "content": contenido})
    guardar_historial(historial)
    return contenido

print("🌍 Asistente de viajes iniciado. Escribe 'salir' para terminar.\n")

while True:
    mensaje = input("Tú: ")
    
    if mensaje.lower() == "salir":
        print("¡Hasta luego! ✈️")
        break
    
    historial = cargar_historial()
    historial.append({"role": "user", "content": mensaje})
    
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historial,
        temperature=0.7,
        max_tokens=500,
        stream=True
    )
    
    print("\nAsistente: ", end="", flush=True)
    contenido = ""
    for chunk in stream:
        trozo = chunk.choices[0].delta.content
        if trozo is not None:
            print(trozo, end="", flush=True)
            contenido += trozo
    print("\n")
    
    historial.append({"role": "assistant", "content": contenido})
    guardar_historial(historial)