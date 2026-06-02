from datetime import datetime
historial = []
def registrar_movimiento(tipo,cantidad,saldo):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M")
    movimiento = f"^[{ahora}] {tipo}: {cantidad}€ (Saldo: {saldo:.2f}€)"
    historial.append(movimiento)
    

def cargar_saldo():
    try:
        with open("saldo.txt", "r") as archivo:
            return float(archivo.read())
    except:
        return 1000

def guardar_saldo(saldo):
    with open("saldo.txt", "w") as archivo:
        archivo.write(str(saldo))

def mostrar_saldo(saldo):
    print(f"Tu saldo actual es {saldo:.2f}€")

def ingresar(saldo, cantidad):
    resultado = saldo + cantidad
    print(f"Has ingresado {cantidad}€")
    guardar_saldo(resultado)
    registrar_movimiento("Ingreso", cantidad, resultado)
    return resultado

def retirar(saldo, cantidad):
    if saldo > cantidad:
        saldo = saldo - cantidad
        print(f"Has retirado {cantidad}€")
        registrar_movimiento("Retirada", cantidad, saldo)
    else:
        print("Saldo insuficiente")
    guardar_saldo(saldo)
    return saldo

saldo = cargar_saldo()

while True:
    print("1. Ver saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    print("5. Ver historial")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        mostrar_saldo(saldo)
    elif opcion == "2":
        cantidad = float(input("¿Cuánto quieres ingresar? "))
        saldo = ingresar(saldo, cantidad)
    elif opcion == "3":
        cantidad = float(input("¿Cuánto quieres retirar? "))
        saldo = retirar(saldo, cantidad)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    elif opcion == "5":
        if historial:
            print("📋 Historial de movimientos:")
            for movimiento in historial:
                print(movimiento)
        else:
            print("No hay movimientos todavía")
        