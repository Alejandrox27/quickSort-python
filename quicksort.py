lista = [3,6,76,34,2,31,1,9,0]

def separacion(lista):
    if len(lista) < 1:
        return []
    
    izquierda = []
    derecha = []
    pivote = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            izquierda.append(lista[i])
        else:
            derecha.append(lista[i])
            
    return izquierda, pivote, derecha

def quickSort(lista):
    if len(lista) < 2:
        return lista
    
    izquierda, pivote, derecha = separacion(lista)
    
    return quickSort(izquierda) + [pivote] + quickSort(derecha)
