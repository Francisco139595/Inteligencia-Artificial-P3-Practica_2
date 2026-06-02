from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenamiento por inserción (Insertion Sort).
    
    Args:
        arr: Una lista de elementos (por ejemplo, enteros) a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente.
    """
    # Recorremos la lista desde el segundo elemento (índice 1) hasta el final.
    # Asumimos que el primer elemento (índice 0) ya está "ordenado" por sí solo.
    for i in range(1, len(arr)):
        # 'key' es el valor actual que queremos insertar en la posición correcta
        # dentro de la sublista que ya está ordenada a la izquierda de 'i'.
        key = arr[i]
        
        # 'j' es el índice del elemento justo a la izquierda de nuestro 'key'.
        # Usaremos 'j' para recorrer la sublista ordenada de derecha a izquierda.
        j = i - 1
        
        # Movemos los elementos de la sublista ordenada [0...i-1] que sean mayores
        # que 'key', una posición hacia la derecha para hacer espacio.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Desplaza el elemento mayor hacia la derecha
            j -= 1               # Retrocede al siguiente elemento a comparar
            
        # Una vez que encontramos la posición correcta, insertamos 'key'
        # en el espacio libre (j + 1).
        arr[j + 1] = key
        
    return arr

if __name__ == "__main__":
    # 1. Creamos una lista de ejemplo desordenada
    mi_lista = [12, 11, 13, 5, 6, 1, 9, 3, 8, 7, 88, 63, 45, 23, 34, 56, 78, 90, 2, 4, 10   ]
    print(f"Lista original desordenada: {mi_lista}")
    
    # 2. Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = insertion_sort(mi_lista)
    print(f"Lista ordenada por inserción: {lista_ordenada}")