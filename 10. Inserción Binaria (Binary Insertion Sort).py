from typing import List

def binary_search(arr: List[int], val: int, start: int, end: int) -> int:
    """
    Busca la posición correcta para insertar 'val' en la sublista ordenada arr[start:end+1]
    utilizando el algoritmo de búsqueda binaria.
    """
    # Caso base: si el rango se reduce a un solo elemento
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
            
    # Si los índices se cruzan, retornamos el punto de inicio como posición de inserción
    if start > end:
        return start
        
    # Encontramos el punto medio
    mid = (start + end) // 2
    
    # Si el valor en el medio es menor que el valor a insertar,
    # buscamos en la mitad derecha.
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    # Si el valor en el medio es mayor, buscamos en la mitad izquierda.
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    # Si son iguales, encontramos la posición exacta.
    else:
        return mid

def binary_insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo de Inserción Binaria.
    Utiliza búsqueda binaria para optimizar la cantidad de comparaciones
    necesarias para encontrar la posición correcta de cada elemento.
    """
    for i in range(1, len(arr)):
        val = arr[i]
        
        # Encontramos la posición 'j' donde el valor actual debe ser insertado
        j = binary_search(arr, val, 0, i - 1)
        
        # Reconstruimos la lista insertando 'val' en la posición 'j'.
        # arr[:j] -> Elementos antes de la posición de inserción.
        # [val] -> El elemento actual que estamos reubicando.
        # arr[j:i] -> Elementos que son mayores que 'val' y se desplazan a la derecha.
        # arr[i+1:] -> El resto de la lista desordenada.
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = binary_insertion_sort(mi_lista)
    print(f"Lista ordenada por Inserción Binaria: {lista_ordenada}")