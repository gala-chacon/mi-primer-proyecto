import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["especie"] = iris.target
print(df.head(10))
print(f"\nTotal de flores: {len(df)}")
print(f"Especies: {iris.target_names}")
X = df[["sepal length (cm)", "sepal width (cm)", 
        "petal length (cm)", "petal width (cm)"]]
y = df["especie"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = KNeighborsClassifier()
modelo.fit(X_train, y_train)

puntuacion = modelo.score(X_test, y_test)
print(f"Precisión del modelo: {puntuacion:.2f}")
flor_nueva = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], 
             columns=["sepal length (cm)", "sepal width (cm)", 
                      "petal length (cm)", "petal width (cm)"])
prediccion = modelo.predict(flor_nueva)
print(f"La flor nueva es: {iris.target_names[prediccion[0]]}")
from sklearn.metrics import confusion_matrix, classification_report
y_pred = modelo.predict(X_test)
print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nInforme de clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

