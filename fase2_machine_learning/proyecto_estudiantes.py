import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
datos = {
    "horas_estudio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 5, 6, 8, 1, 4, 7, 9, 10],
    "horas_sueño":    [4, 5, 4, 6, 7, 6, 8, 7, 8,  9, 3, 5, 6, 7, 8, 5, 4, 7, 8,  9],
    "asistencia":     [40, 50, 55, 60, 70, 75, 80, 85, 90, 95, 45, 60, 70, 80, 90, 30, 65, 85, 95, 100],
    "nota_parcial":   [2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 3, 4, 6, 7, 8, 2, 5, 7, 9, 10],
    "resultado":      [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(datos)
print("📊 Datos de estudiantes:")
print(df)
print(f"\nTotal estudiantes: {len(df)}")
print(f"Aprobados: {df['resultado'].sum()}")
print(f"Suspensos: {len(df) - df['resultado'].sum()}")

X = df[["horas_estudio", "horas_sueño", "asistencia", "nota_parcial"]]
y = df["resultado"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

print(f"\n✅ Datos preparados:")
print(f"Entrenamiento: {len(X_train)} estudiantes")
print(f"Prueba: {len(X_test)} estudiantes")
modelos = {
    "KNN":             KNeighborsClassifier(),
    "Árbol decisión":  DecisionTreeClassifier(random_state=42),
    "Random Forest":   RandomForestClassifier(n_estimators=100, random_state=42)
}

print("\n🤖 Comparación de modelos:")
print("-" * 40)

resultados = {}
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    precision = modelo.score(X_test, y_test)
    resultados[nombre] = precision
    print(f"{nombre}: {precision:.2f}")

plt.figure(figsize=(8, 5))
plt.bar(resultados.keys(), resultados.values(), color=["orange", "blue", "yellow"])
plt.title("Comparación de modelos")
plt.ylabel("Precisión")
plt.ylim(0, 1.2)
for i, (nombre, valor) in enumerate(resultados.items()):
    plt.text(i, valor + 0.02, f"{valor:.2f}", ha="center", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()
print("\n🎓 Predicción de estudiante nuevo:")
estudiante_nuevo = pd.DataFrame([[6, 7, 80, 6]], 
                  columns=["horas_estudio", "horas_sueño", "asistencia", "nota_parcial"])
estudiante_normalizado = pd.DataFrame(scaler.transform(estudiante_nuevo), 
                         columns=estudiante_nuevo.columns)

for nombre, modelo in modelos.items():
    pred = modelo.predict(estudiante_normalizado)
    resultado = "✅ Aprobado" if pred[0] == 1 else "❌ Suspenso"
    print(f"{nombre}: {resultado}")
    
