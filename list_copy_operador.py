#Programa iterativo para copiar una lista usando +
def list_copy_operador(lista):  
    copia = []        
    for i in range(len(lista)):
        copia = copia + [lista[i]] #el operador + crea una segunda #lista por cada n iteraciones, o sea 2n, que se simplifica en O(n)
    return copia