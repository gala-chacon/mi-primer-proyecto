import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
df = pd.read_csv("diabetes.csv")

print(f"Total de pacientes: {len(df)}")
print(f"\nColumnas: {list(df.columns)}")
print(f"\nDistribución:")
print(df["Outcome"].value_counts())
print(f"\nValores vacíos:")
print(df.isnull().sum())
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlaciones entre variables")
plt.tight_layout()
plt.show()
X = df.drop(columns=["Outcome"])
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

modelos = {
    "KNN":                 KNeighborsClassifier(),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
    "Regresión logística": LogisticRegression()
}

print("\n🤖 Comparación de modelos:")
print("-" * 40)
for nombre, modelo in modelos.items():
    scores = cross_val_score(modelo, 
                            pd.DataFrame(scaler.fit_transform(X), columns=X.columns), 
                            y, cv=5)
    print(f"{nombre}: {scores.mean():.2f} (±{scores.std():.2f})")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

importancias = pd.DataFrame({
    "caracteristica": X.columns,
    "importancia": rf.feature_importances_
}).sort_values("importancia", ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=importancias, x="importancia", y="caracteristica", palette="coolwarm")
plt.title("Características más importantes para predecir diabetes")
plt.tight_layout()
plt.show()
