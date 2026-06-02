numeros = [15, 42, 8, 23, 4, 16, 99, 7]
def calcular_media(numeros):
    media = sum(numeros) / len(numeros)
    return media
media = calcular_media(numeros)
print(f"Media: {media:.2f}")
def calcular_numero_mayor(numeros):
    numero_mayor = max(numeros)
    return numero_mayor
numero_mayor = calcular_numero_mayor(numeros)
print(f"Número mayor: {numero_mayor}")
def calcular_numero_menor(numeros):
    numero_menor = min(numeros)
    return numero_menor 
numero_menor = calcular_numero_menor(numeros)
print(f"Número menor: {numero_menor}")       



