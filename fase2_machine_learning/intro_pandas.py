import pandas as pd
datos = {
    "nombre": ["Gala", "María", "Carlos", "Ana"],
    "edad": [36, 25, 30, 28],
    "ciudad": ["Cádiz", "Madrid", "Barcelona", "Sevilla"]
}

df = pd.DataFrame(datos)
print(df)
print(df["ciudad"])
print(df[(df["ciudad"] == "Madrid") | (df["ciudad"] == "Sevilla")])
print(df.iloc[2])
df["puntuacion"] = [5, 3, 9, 2]
print(df)
df.loc[3, "ciudad"] = "Granada"
print(df)
nueva_fila = {"nombre": "Fernando", "edad": 33, "ciudad": "Cuenca", "puntuacion": 7}
df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
print(df)
df.to_csv("personas.csv", index=False)
print("Archivo guardado")
df2 = pd.read_csv("personas.csv")
print(df2)
print(df.describe()) 
print(df["puntuacion"].mean())
print(df["edad"].max())

