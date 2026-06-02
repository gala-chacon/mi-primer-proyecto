import requests
from geopy.geocoders import Nominatim

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="buscador_tiempo")
    ubicacion = geolocator.geocode(ciudad)
    if ubicacion:
        return ubicacion.latitude, ubicacion.longitude
    else:
        return None, None

def obtener_tiempo(ciudad):
    lat, lon = obtener_coordenadas(ciudad)
    if lat is None:
        print(f"No encontré la ciudad '{ciudad}'")
        return
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&timezone=auto"
    
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    temperatura = datos["current"]["temperature_2m"]
    humedad = datos["current"]["relative_humidity_2m"]
    lluvia = datos["current"]["precipitation"]
    viento = datos["current"]["wind_speed_10m"]
    
    print(f"\n🌍 El tiempo en {ciudad}:")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"💧 Humedad: {humedad}%")
    print(f"🌧️ Lluvia: {lluvia} mm")
    print(f"💨 Viento: {viento} km/h")

while True:
    ciudad = input("\n¿De qué ciudad quieres saber el tiempo? (o 'salir'): ")
    if ciudad.lower() == "salir":
        print("¡Hasta luego!")
        break
    obtener_tiempo(ciudad)