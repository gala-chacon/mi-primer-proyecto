import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

datos = {
    "horas_estudio": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5],
    "horas_sueño":   [4, 3, 6, 7, 5, 6, 7, 8, 7, 8, 5, 4, 6, 7, 8],
    "resultado":     [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(datos)
X = df[["horas_estudio", "horas_sueño"]]
y = df["resultado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo_overfit = KNeighborsClassifier(n_neighbors=1)
modelo_overfit.fit(X_train, y_train)
print(f"k=1 (overfitting):")
print(f"  Precisión entrenamiento: {modelo_overfit.score(X_train, y_train):.2f}")
print(f"  Precisión prueba:        {modelo_overfit.score(X_test, y_test):.2f}")
modelo_correcto = KNeighborsClassifier(n_neighbors=5)
modelo_correcto.fit(X_train, y_train)
print(f"\nk=5 (equilibrado):")
print(f"  Precisión entrenamiento: {modelo_correcto.score(X_train, y_train):.2f}")
print(f"  Precisión prueba:        {modelo_correcto.score(X_test, y_test):.2f}")
