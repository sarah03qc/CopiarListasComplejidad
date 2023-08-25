#Programa recursivo de pila para copiar una lista usando +
def list_copy_stack(lista, i):
    #en esta el operador + igual crea una lista extra por cada n vez
    #y la cantidad de iteraciones seran n, siendo 2n que
    #se simplifica en O(n)
    if i == len(lista):
        return []  
    return [lista[i]] + list_copy_stack(lista, i + 1)