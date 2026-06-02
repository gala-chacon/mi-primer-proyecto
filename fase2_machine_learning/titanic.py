import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.shape)
print(df.head())
print("\nValores vacíos:")
print(df.isnull().sum())
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.dropna(subset=["Embarked"])
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

print("✅ Datos limpios:")
print(df.isnull().sum())
print(df.head())
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X = df.drop(columns=["Survived"])
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

modelos = {
    "KNN":            KNeighborsClassifier(),
    "Árbol decisión": DecisionTreeClassifier(random_state=42),
    "Random Forest":  RandomForestClassifier(n_estimators=100, random_state=42)
}

print("\n🤖 Comparación de modelos:")
print("-" * 40)
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    precision = modelo.score(X_test, y_test)
    print(f"{nombre}: {precision:.2f}")

import matplotlib.pyplot as plt
resultados = {"KNN": 0.78, "Árbol decisión": 0.76, "Random Forest": 0.76}
plt.figure(figsize=(8, 5))
plt.bar(resultados.keys(), resultados.values(), color=["pink", "purple", "green"])
plt.title("Comparación de modelos - Titanic")
plt.ylabel("Precisión")
plt.ylim(0, 1.2)
for i, (nombre, valor) in enumerate(resultados.items()):
    plt.text(i, valor + 0.02, f"{valor:.2f}", ha="center", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
importancias = pd.DataFrame({
    "caracteristica": X.columns,
    "importancia": rf.feature_importances_
}).sort_values("importancia", ascending=False)
print("\n🔍 Características más importantes:")
print(importancias)

