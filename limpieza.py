import pandas as pd

datos_sucios = {
    "nombre": ["Gala", "María", "Carlos", None],
    "edad": [36, None, 30, 28],
    "ciudad": ["Cádiz", "Madrid", "Barcelona", "Sevilla"]
}

df_sucio = pd.DataFrame(datos_sucios)
print(df_sucio)
print(df_sucio.isnull().sum())
df_limpio = df_sucio.dropna()
print(df_limpio)
df_relleno = df_sucio.fillna({"edad": df_sucio["edad"].mean(), "nombre": "Desconocido"})
print(df_relleno)
datos_duplicados = {
    "nombre": ["Gala", "María", "Gala", "Carlos"],
    "edad": [36, 25, 36, 30]
}

df_dup = pd.DataFrame(datos_duplicados)
print(df_dup)
print(df_dup.drop_duplicates())