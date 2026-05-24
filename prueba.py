with open ("prueba.txt", "w") as archivo:
    archivo.write("Hola soy Gala")
with open("prueba.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    