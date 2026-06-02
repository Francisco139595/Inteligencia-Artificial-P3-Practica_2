from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo Merge Sort (Ordenamiento por mezcla).
    Sigue el paradigma de divide y vencerás.
    
    Args:
        arr: Una lista de elementos (por ejemplo, enteros) a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente (se modifica in-place).
    """
    # Caso recursivo: si la lista tiene más de 1 elemento, la dividimos
    if len(arr) > 1:
        # Encontramos el punto medio de la lista
        mid = len(arr) // 2
        
        # Dividimos la lista en dos mitades: Izquierda (L) y Derecha (R)
        L = arr[:mid]
        R = arr[mid:]

        # Llamadas recursivas para ordenar cada mitad
        merge_sort(L)
        merge_sort(R)

        # Inicializamos los índices para recorrer:
        # i: para la mitad izquierda (L)
        # j: para la mitad derecha (R)
        # k: para la lista principal (arr)
        i = j = k = 0
        
        # Comparamos los elementos de ambas mitades y los colocamos en orden en 'arr'
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Verificamos si quedaron elementos en la mitad izquierda (L)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Verificamos si quedaron elementos en la mitad derecha (R)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [38, 27, 43, 3, 9, 82, 10, 25, 1, 45, 12]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = merge_sort(mi_lista)
    print(f"Lista ordenada por Merge Sort: {lista_ordenada}")