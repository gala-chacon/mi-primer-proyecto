import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
parametros = {
    "n_estimators": [10, 50, 100, 200],
    "max_depth":    [2, 5, 10, None],
    "min_samples_split": [2, 5, 10]
}

modelo = RandomForestClassifier(random_state=42)
busqueda = GridSearchCV(modelo, parametros, cv=5, scoring="accuracy")
busqueda.fit(X_scaled, y)

print("🔍 Mejores hiperparámetros encontrados:")
print(busqueda.best_params_)
print(f"\nMejor precisión: {busqueda.best_score_:.2f}")
