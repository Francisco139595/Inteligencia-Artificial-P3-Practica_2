from typing import List

def heapify(arr: List[int], n: int, i: int):
    """
    Función auxiliar para mantener la propiedad de montículo (Max-Heap).
    Garantiza que el subárbol con raíz en el índice 'i' sea un Max-Heap.
    """
    largest = i        # Inicializamos el nodo actual como el más grande (raíz)
    l = 2 * i + 1      # Índice del hijo izquierdo
    r = 2 * i + 2      # Índice del hijo derecho

    # Verificamos si el hijo izquierdo existe y es mayor que la raíz
    if l < n and arr[i] < arr[l]:
        largest = l

    # Verificamos si el hijo derecho existe y es mayor que el más grande hasta el momento
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Si el elemento más grande ya no es la raíz, intercambiamos los valores
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Llamada recursiva para aplicar heapify en el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo Heap Sort (Ordenamiento por Montículos).
    
    Args:
        arr: Una lista de elementos a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente (modificada in-place).
    """
    n = len(arr)

    # Paso 1: Construir un Max-Heap a partir de la lista desordenada.
    # Empezamos desde el último nodo que no es una hoja, retrocediendo hasta la raíz.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Paso 2: Extraer elementos del Heap uno por uno.
    for i in range(n - 1, 0, -1):
        # Movemos la raíz (el número más grande) al final del arreglo
        arr[i], arr[0] = arr[0], arr[i]
        # Llamamos a heapify en el montículo reducido para restaurar la propiedad Max-Heap
        heapify(arr, i, 0)
        
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [12, 11, 13, 5, 6, 7, 90, 23, 1, 4]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = heap_sort(mi_lista)
    print(f"Lista ordenada por Heap Sort: {lista_ordenada}")