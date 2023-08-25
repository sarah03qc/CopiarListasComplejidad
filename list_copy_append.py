#Programa iterativo para copiar una lista usando append
def list_copy_append(lista):
    copia = []        
    for i in range(len(lista)):
        copia.append(lista[i])  #se gastan n, el append vale uno, se hace n veces, quedando O(n)
    return copia