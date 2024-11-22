def mas_corta(palabras):
    pos = 0
    for x in range(len(palabras)):
        if len(palabras[x]) < len(palabras[pos]):
            pos = x

    return palabras[pos]        

palabras = ["Ana", "carlos", "Beatriz", "Juan", "Pedro", "Sofia"]
print("Palabra con menos caracteres:", mas_corta(palabras))