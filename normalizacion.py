import pandas as pd
from sklearn.preprocessing import MinMaxScaler

datos = {
    "tamaño":       [50, 80, 100, 120, 150],
    "habitaciones": [1,  2,  3,   4,   5],
    "precio":       [80000, 130000, 165000, 200000, 235000]
}

df = pd.DataFrame(datos)
print("Antes de normalizar:")
print(df)
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("\nDespués de normalizar:")
print(df_normalizado)
