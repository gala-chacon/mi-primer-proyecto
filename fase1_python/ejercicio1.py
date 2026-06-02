productos = {
    "manzana": 1.20,
    "pan": 0.90,
    "leche": 1.50,
    "queso": 3.80,
    "café": 4.20
}
for producto in productos:
    print(f"producto: {producto}, precio: {productos[producto]}")
total = 0
for producto in productos:
    total += productos[producto]
print(f"Total: {total:.2f}€")
for producto in productos:
    if productos[producto] > 2:
        print(producto)
    
