def sumar(lista):
    suma = 0

    for num in lista:
        suma = suma + num
    return suma

mi_lista = [1, 2, 3]
print("Suma", sumar(mi_lista))
print("Original:", mi_lista)