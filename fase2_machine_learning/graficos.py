import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "nombre": ["Gala", "María", "Carlos", "Ana", "Fernando"],
    "ventas": [100, 200, 150, 300, 75]
}

df = pd.DataFrame(datos)

df.plot(kind="pie", y="ventas", labels=df["nombre"], title="Ventas por persona")
plt.show()
