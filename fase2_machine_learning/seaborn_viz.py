import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["especie"] = iris.target
df["especie"] = df["especie"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print(df.head())
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="especie", y="petal length (cm)", palette="Set2")
plt.title("Distribución de longitud de pétalo por especie")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="petal length (cm)", y="petal width (cm)", 
                hue="especie", palette="Set1", s=100)
plt.title("Relación entre longitud y ancho de pétalo")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 6))
sns.heatmap(df.drop(columns=["especie"]).corr(), 
            annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de calor de correlaciones")
plt.tight_layout()
plt.show()
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
caracteristicas = iris.feature_names

for i, (ax, col) in enumerate(zip(axes.flat, caracteristicas)):
    sns.histplot(data=df, x=col, hue="especie", ax=ax, palette="Set2")
    ax.set_title(col)

plt.suptitle("Distribución de características por especie", fontsize=14)
plt.tight_layout()
plt.show()
