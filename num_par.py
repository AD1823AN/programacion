def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador
    
entrada = input("Ingrese una lista de números separados por espacios: ")

numeros = [int(x) for x in entrada.split()]

cantidad_pares = contar_pares(numeros)
print("Cantidad de números pares:", cantidad_pares)
