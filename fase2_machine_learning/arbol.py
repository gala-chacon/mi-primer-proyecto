import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

iris_data = {
    "longitud_petalo": [1.4, 1.4, 1.3, 4.7, 4.5, 4.9, 6.0, 5.8, 5.9, 6.1],
    "ancho_petalo":    [0.2, 0.2, 0.2, 1.4, 1.5, 1.5, 2.5, 2.7, 2.1, 2.5],
    "especie":         [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
}
df = pd.DataFrame(iris_data)
X = df[["longitud_petalo", "ancho_petalo"]]
y = df["especie"]

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

print("¡Modelo entrenado! ✅")
print("\nAsí toma decisiones el modelo:")
print(export_text(modelo, feature_names=["longitud_petalo", "ancho_petalo"]))
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10, 6))
plot_tree(modelo, 
          feature_names=["longitud_petalo", "ancho_petalo"],
          class_names=["setosa", "versicolor", "virginica"],
          filled=True, rounded=True)
plt.title("Árbol de decisión")
plt.show()
