import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=36.53&longitude=-6.29&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&timezone=Europe/Madrid"

respuesta = requests.get(url)
datos = respuesta.json()

temperatura = datos["current"]["temperature_2m"]
humedad = datos["current"]["relative_humidity_2m"]
lluvia = datos["current"]["precipitation"]
viento = datos["current"]["wind_speed_10m"]

print(f"El tiempo en Cádiz ahora mismo:")
print(f"🌡️ Temperatura: {temperatura}°C")
print(f"💧 Humedad: {humedad}%")
print(f"🌧️ Lluvia: {lluvia} mm")
print(f"💨 Viento: {viento} km/h")
