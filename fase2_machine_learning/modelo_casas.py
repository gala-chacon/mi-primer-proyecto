import pandas as pd
from sklearn.linear_model import LinearRegression
datos = {
    "tamaño": [50, 60, 70, 80, 90, 100, 110, 120],
    "habitaciones": [1, 1, 2, 2, 3, 3, 4, 4],
    "precio": [80000, 90000, 115000, 130000, 150000, 165000, 185000, 200000]
    
}
df= pd.DataFrame(datos)
print(df)

X = df[["tamaño", "habitaciones"]]
y = df["precio"]
modelo = LinearRegression()
modelo.fit(X, y)
print("¡Modelo entrenado!✅")
precio_predicho = modelo.predict(pd.DataFrame([[85, 2]], columns=["tamaño", "habitaciones"]))
print(f"Una casa de 85 m² y 2 habitaciones costaría: {precio_predicho[0]:,.0f} €")
precio_predicho = modelo.predict(pd.DataFrame([[65, 1]], columns=["tamaño", "habitaciones"]))
print(f"Una casa de 65 m² y 1 habitaciones costaría: {precio_predicho[0]:,.0f} €")
precio_predicho = modelo.predict(pd.DataFrame([[95, 3]], columns=["tamaño", "habitaciones"]))
print(f"Una casa de 95 m² y 3 habitaciones costaría: {precio_predicho[0]:,.0f} €")
precio_predicho = modelo.predict(pd.DataFrame([[150, 5]], columns=["tamaño", "habitaciones"]))
print(f"Una casa de 150 m² y 5 habitaciones costaría: {precio_predicho[0]:,.0f} €")
puntuacion = modelo.score(X, y)
print(f"Precisión del modelo: {puntuacion: .2f}")
import matplotlib.pyplot as plt

plt.scatter(df["tamaño"], df["precio"], color="blue", label="Datos reales")
plt.plot(df["tamaño"], modelo.predict(X), color="green", label="Predicción")
plt.xlabel("Tamaño (m²)")
plt.ylabel("Precio (€)")
plt.title("Modelo de predicción de precios")
plt.legend()
plt.show()