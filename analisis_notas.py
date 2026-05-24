import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "asignatura": ["Matemáticas", "Lengua", "Inglés", "Tecnología", "Ciencias"],
    "nota": [5, 7, 8, 6, 9],
    "profesor": ["Sr. García", "Sra. López", "Sr. Smith", "Sra. Martínez", "Sr. Pérez"] 
}

df = pd.DataFrame(datos)
print(df)
print("Media de notas:", df["nota"].mean())
print("Nota más alta:", df["nota"].max())
print("Nota más baja:", df["nota"].min())
aprobadas = df[df["nota"] >= 5]
print("Asignaturas aprobadas:")
print(aprobadas)
df.plot(kind="bar", x="asignatura", y="nota", title="Notas por asignatura", color="pink")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()