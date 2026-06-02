from typing import List

def shell_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenamiento Shell Sort.
    Es una versión optimizada del ordenamiento por Inserción (Insertion Sort).
    
    Args:
        arr: Una lista de elementos (por ejemplo, enteros) a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente.
    """
    n = len(arr)
    
    # Inicializamos el tamaño de la 'brecha' (gap).
    # Tradicionalmente, la secuencia original de Shell comienza con N // 2.
    gap = n // 2
    
    # Continuamos reduciendo el gap hasta llegar a 0.
    while gap > 0:
        # Hacemos un ordenamiento por inserción para los elementos separados por el 'gap'.
        for i in range(gap, n):
            # Guardamos el elemento actual que queremos colocar en la posición correcta.
            temp = arr[i]
            j = i
            
            # Recorremos hacia atrás los elementos separados por la distancia 'gap'.
            # Si el elemento anterior es mayor que 'temp', lo desplazamos hacia adelante.
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                
            # Colocamos el valor 'temp' en su posición correcta dentro de esta sublista.
            arr[j] = temp
            
        # Reducimos el gap a la mitad para la siguiente iteración.
        gap //= 2
        
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [45, 23, 11, 89, 77, 98, 4, 28, 65, 43, 10, 2, 15, 67, 34, 56, 12, 9, 1, 8   ]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = shell_sort(mi_lista)
    print(f"Lista ordenada por Shell Sort: {lista_ordenada}")