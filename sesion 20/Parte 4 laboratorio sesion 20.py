#Funcion con parametros de tipo lista

def suma(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may 
def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    

listadevalores=[45,78,65,23,19,21]
print("La lista completa es: ", listadevalores)
print("La suma de todo los elementos de la lista es: ",suma(listadevalores))
print("El numero mayor encontrado en la lista es: ",mayor(listadevalores))
print("El numero menor encontrado en la lista es: ",menor(listadevalores))    
    