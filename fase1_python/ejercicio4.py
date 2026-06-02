def guardar_nota(nombre, nota):
    with open("notas.txt", "a") as archivo:
        archivo.write(f"{nombre}: {nota}\n")
guardar_nota("Matemáticas", 8.5)
guardar_nota("Historia", 7.0)
guardar_nota("Inglés", 9.2)
guardar_nota("Física", 6.8)
def leer_notas():
    print("📚 Notas guardadas:")
    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
def calcular_media_notas():
    notas = []
    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            nota = float(linea.split(": ")[1])
            notas.append(nota)
    print(f"📚Media de notas: {sum(notas) / len(notas):.2f}")
leer_notas()
calcular_media_notas()




