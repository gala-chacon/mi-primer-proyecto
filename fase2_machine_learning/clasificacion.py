import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
datos = {
    "horas_estudio": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "horas_sueño": [4, 3, 6, 7, 5, 6, 7, 8, 7, 8],
    "resultado": [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]

}
df = pd.DataFrame(datos)
print(df)

X = df[["horas_estudio", "horas_sueño"]]
y = df["resultado"]

modelo = KNeighborsClassifier()
modelo.fit(X, y)

print("¡Modelo entrenado! ✅")
prediccion = modelo.predict(pd.DataFrame([[5, 7]], columns=["horas_estudio", "horas_sueño"]))
print(f"¿Aprobará? {'✅ Aprobado' if prediccion[0] == 1 else '❌ Suspenso'}")
prediccion = modelo.predict(pd.DataFrame([[1, 3]], columns=["horas_estudio", "horas_sueño"]))
print(f"¿Aprobará? {'✅ Aprobado' if prediccion[0] == 1 else '❌ Suspenso'}")
prediccion = modelo.predict(pd.DataFrame([[8, 4]], columns=["horas_estudio", "horas_sueño"]))
print(f"¿Aprobará? {'✅ Aprobado' if prediccion[0] == 1 else '❌ Suspenso'}")
prediccion = modelo.predict(pd.DataFrame([[3, 8]], columns=["horas_estudio", "horas_sueño"]))
print(f"¿Aprobará? {'✅ Aprobado' if prediccion[0] == 1 else '❌ Suspenso'}")