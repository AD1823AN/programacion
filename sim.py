numeros = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
cantidad_pares = sum(1 for numero in numeros if numero % 2 == 0)
print("Cantidad de números pares:", cantidad_pares)
