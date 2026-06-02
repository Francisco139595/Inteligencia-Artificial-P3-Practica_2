from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo QuickSort (Ordenamiento rápido).
    Utiliza el paradigma de divide y vencerás.
    
    Args:
        arr: Una lista de elementos (por ejemplo, enteros) a ordenar.
        
    Returns:
        Una nueva lista ordenada de forma ascendente.
    """
    # Caso base: Si la lista tiene 1 o 0 elementos, ya está ordenada.
    if len(arr) <= 1:
        return arr
        
    # Elegimos un 'pivote'. En este caso, el elemento central de la lista.
    pivot = arr[len(arr) // 2]
    
    # Particionamos la lista en tres sublistas:
    # 1. Elementos menores que el pivote
    left = [x for x in arr if x < pivot]
    
    # 2. Elementos iguales al pivote (maneja duplicados del pivote)
    middle = [x for x in arr if x == pivot]
    
    # 3. Elementos mayores que el pivote
    right = [x for x in arr if x > pivot]
    
    # Llamada recursiva para ordenar las sublistas 'left' y 'right',
    # y luego concatenamos los resultados junto con 'middle'.
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [3, 6, 8, 10, 1, 2, 1, 4, 7, 9, 5, 22, 15, 30]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = quick_sort(mi_lista)
    print(f"Lista ordenada por QuickSort: {lista_ordenada}")
