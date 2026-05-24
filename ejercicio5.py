def añadir_contacto(nombre, telefono):
    with open("agenda.txt", "a") as archivo:
        archivo.write(f"{nombre}: {telefono}\n")
    print(f"Contacto '{nombre}' añadido con éxito.") 
def ver_contactos():
    try:
        with open("agenda.txt", "r") as archivo:
            contactos = archivo.readlines()
            if contactos:
                print("📒 Lista de contactos:")
                for contacto in contactos:
                    print(contacto.strip())
            else:
                print("No hay contactos en la agenda.")
    except FileNotFoundError:
        print("No se ha encontrado el archivo de contactos. Aún no has añadido ningún contacto.")
def buscar_contacto(nombre):
    try:
        with open("agenda.txt", "r") as archivo:
            contactos = archivo.readlines()
            for contacto in contactos:
                if contacto.startswith(nombre + ":"):
                    print(f"📞 Contacto encontrado: {contacto.strip()}")
                    return
            print(f"No se ha encontrado el contacto '{nombre}'.")
    except FileNotFoundError:
        print("No se ha encontrado el archivo de contactos. Aún no has añadido ningún contacto.")
while True:
    print("\n📱 Menú de la Agenda de Contactos:")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono: ")
        añadir_contacto(nombre, telefono)
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        nombre = input("Introduce el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")