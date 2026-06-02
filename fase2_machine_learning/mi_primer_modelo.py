import pandas as pd
from sklearn.linear_model import LinearRegression
datos = {
    "tamaño": [50, 60, 70, 80, 90, 100, 110, 120],
    "precio": [80000, 95000, 110000, 125000, 140000, 155000, 170000, 185000]
}

df = pd.DataFrame(datos)
print(df)
X = df[["tamaño"]]
y = df["precio"]    
modelo = LinearRegression()
modelo.fit(X, y)
print("¡Modelo entrenado! ✅")
precio_predicho = modelo.predict(pd.DataFrame([[85]], columns=["tamaño"]))
print(f"Una casa de 85 m² costaría: {precio_predicho[0]:,.0f} €")
puntuacion = modelo.score(X, y)
print(f"Precisión del modelo: {puntuacion:.2f}")