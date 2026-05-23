numeros = [] 
for i in range(5):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)
for numero in numeros:
    if numero % 2 == 0:
        print(f"Número par: {numero}")
for numero in numeros:
    if numero % 2 != 0:
        print(f"Número impar: {numero}")
print(f"Suma total: {sum(numeros)}")
