saldo = 1000

def mostrar_saldo(saldo):
    print(f"Tu saldo actual es {saldo}€")

def ingresar(saldo, cantidad):
    resultado = saldo + cantidad
    print(f"Has ingresado {cantidad}€")
    return resultado

def retirar(saldo, cantidad):
    if saldo > cantidad:
        saldo = saldo - cantidad
        print(f"Has retirado {cantidad}€")
    else:
        print("Saldo insuficiente")
    return saldo

while True:
    print("1. Ver saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        mostrar_saldo(saldo)
    elif opcion == "2":
        cantidad = int(input("¿Cuánto quieres ingresar? "))
        saldo = ingresar(saldo, cantidad)
    elif opcion == "3":
        cantidad = int(input("¿Cuánto quieres retirar? "))
        saldo = retirar(saldo, cantidad)
    elif opcion == "4":
        print("¡Hasta luego!")
        break