import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
arbol = DecisionTreeClassifier(random_state=42)
arbol.fit(X_train, y_train)
print(f"Un solo árbol:   {arbol.score(X_test, y_test):.2f}")
bosque = RandomForestClassifier(n_estimators=100, random_state=42)
bosque.fit(X_train, y_train)
print(f"Random Forest:   {bosque.score(X_test, y_test):.2f}")
importancias = pd.DataFrame({
    "caracteristica": iris.feature_names,
    "importancia": bosque.feature_importances_
}).sort_values("importancia", ascending=False)

print("\nImportancia de cada característica:")
print(importancias)
