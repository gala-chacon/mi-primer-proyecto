import pandas as pd

datos = {
    "nombre": ["Gala", "María", "Carlos", "Ana", "Gala", "María"],
    "ciudad": ["Cádiz", "Madrid", "Cádiz", "Madrid", "Cádiz", "Madrid"],
    "ventas": [100, 200, 150, 300, 50, 100]
}

df = pd.DataFrame(datos)
print(df)
por_ciudad = df.groupby("ciudad")["ventas"].sum()
print(por_ciudad)
print(df.groupby("ciudad")["ventas"].mean()) 
print(df.groupby("ciudad")["ventas"].max())
por_nombre = df.groupby("nombre")["ventas"].sum()
print(por_nombre)
print(df.groupby("nombre")["ventas"].mean())
print(df.groupby("nombre")["ventas"].max()) 
