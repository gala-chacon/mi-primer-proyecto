import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
modelos = {
    "KNN":                KNeighborsClassifier(),
    "Árbol de decisión":  DecisionTreeClassifier(random_state=42),
    "Random Forest":      RandomForestClassifier(n_estimators=100, random_state=42),
    "Regresión logística": LogisticRegression()
}

print("🔄 Cross-validation (5 partes):")
print("-" * 50)
for nombre, modelo in modelos.items():
    scores = cross_val_score(modelo, X_scaled, y, cv=5)
    print(f"{nombre}:")
    print(f"  Precisión por vuelta: {scores.round(2)}")
    print(f"  Media: {scores.mean():.2f} / Desviación: {scores.std():.2f}")
    