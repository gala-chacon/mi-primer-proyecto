import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

datos = {
    "tamaño":       [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    "habitaciones": [1,  1,  2,  2,  3,  3,   4,   4,   5,   5],
    "precio":       [80000, 90000, 115000, 130000, 150000, 165000, 185000, 200000, 220000, 235000]
}

df = pd.DataFrame(datos)

X = df[["tamaño", "habitaciones"]]
y = df["precio"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("¡Modelo entrenado! ✅")
puntuacion = modelo.score(X_test, y_test)
print(f"Precisión con datos de prueba: {puntuacion:.2f}")
