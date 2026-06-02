from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq()

SISTEMA = "Eres un asistente simpático y con buena memoria."

def llamar_modelo(historial, max_tokens=500):
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historial,
        temperature=0.7,
        max_tokens=max_tokens
    )
    return respuesta.choices[0].message.content

MAX_MENSAJES = 6

historial = [{"role": "system", "content": SISTEMA}]

def chat_limitado(mensaje):
    historial.append({"role": "user", "content": mensaje})
    
    historial_limitado = [historial[0]] + historial[-MAX_MENSAJES:]

    contenido = llamar_modelo(historial_limitado)
    historial.append({"role": "assistant", "content": contenido})
    return contenido

#print(chat_limitado("Hola, me llamo Gala."))
#print(chat_limitado("Tengo 36 años"))
#print(chat_limitado("Vivo en La Línea de la Concepción"))
#print(chat_limitado("Trabajo con Python e inteligencia artificial."))
#print(chat_limitado("¿Recuerdas mi nombre y dónde vivo?"))

# ── SOLUCIÓN 2: Resumir la conversación ──────────────

historial2 = [{"role": "system", "content": SISTEMA}]
resumen_actual = ""

def resumir(historial):
    mensajes = [
        {"role": "system", "content": "Eres un asistente que resume conversaciones."},
        {"role": "user", "content": f"Resume esta conversación en 3-4 frases cortas, guardando datos importantes del usuario: \n\n{str(historial)}"}

    ]
    return llamar_modelo(mensajes, max_tokens=200)

def chat_con_resumen(mensaje):
    global resumen_actual

    if len(historial2) > 8:
        resumen_actual = resumir(historial2)
        historial2.clear()
        historial2.append({"role": "system", "content": SISTEMA})
        historial2.append({"role": "assistant", "content": f"Resumen de lo hablado: {resumen_actual}"})
        
    historial2.append({"role": "user", "content": mensaje})
    contenido = llamar_modelo(historial2)
    historial2.append({"role": "assistant", "content": contenido})
    return contenido

#print(chat_con_resumen("Hola, me llamo Gala."))
#print(chat_con_resumen("Tengo 36 años."))
#print(chat_con_resumen("Vivo en La Línea de la Concepción."))
#print(chat_con_resumen("Estudio programación e inteligencia artificial."))
#print(chat_con_resumen("Mi lenguaje favorito es Python."))
#print(chat_con_resumen("Tengo una pareja inglesa de Bristol."))
#print(chat_con_resumen("Hablo español, inglés, alemán, francés e italiano."))
#print(chat_con_resumen("¿Qué sabes de mí hasta ahora?"))

# ── SOLUCIÓN 3: Guardar historial en archivo ──────────

ARCHIVO_HISTORIAL = "historial.json"

def cargar_historial():
    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"role": "system", "content": SISTEMA}]

def guardar_historial(historial):
    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)

def chat_persistente(mensaje):
    historial = cargar_historial()
    historial.append({"role": "user", "content": mensaje})

    contenido = llamar_modelo(historial)
    historial.append({"role": "assistant", "content": contenido})

    guardar_historial(historial)
    return contenido

#print(chat_persistente("Hola, me llamo Gala y soy programadora."))
print(chat_persistente("¿Recuerdas cómo me llamo?"))
    