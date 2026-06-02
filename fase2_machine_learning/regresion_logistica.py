import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report

datos = {
    "horas_estudio":  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 5, 6, 8, 1, 4, 7, 9, 10],
    "horas_sueño":    [4, 5, 4, 6, 7, 6, 8, 7, 8,  9, 3, 5, 6, 7, 8, 5, 4, 7, 8,  9],
    "nota_parcial":   [2, 3, 4, 5, 5, 6, 7, 7, 8,  9, 3, 4, 6, 7, 8, 2, 5, 7, 9, 10],
    "resultado":      [0, 0, 0, 0, 1, 1, 1, 1, 1,  1, 0, 0, 1, 1, 1, 0, 0, 1, 1,  1]
}

df = pd.DataFrame(datos)
X = df[["horas_estudio", "horas_sueño", "nota_parcial"]]
y = df["resultado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

print(f"Precisión: {modelo.score(X_test, y_test):.2f}")
print(classification_report(y_test, modelo.predict(X_test)))
probabilidades = modelo.predict_proba(X_test)
print("\nProbabilidades de cada estudiante:")
for i, (prob, real) in enumerate(zip(probabilidades, y_test)):
    print(f"Estudiante {i+1}: {prob[0]*100:.1f}% suspenso / {prob[1]*100:.1f}% aprobado → Real: {'Aprobado' if real == 1 else 'Suspenso'}")
