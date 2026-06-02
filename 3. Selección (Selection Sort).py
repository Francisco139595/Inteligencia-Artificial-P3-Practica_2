from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenamiento por selección (Selection Sort).
    
    Args:
        arr: Una lista de elementos (por ejemplo, enteros) a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente.
    """
    n = len(arr)
    
    # Recorremos toda la lista. Cada iteración de este ciclo coloca
    # el elemento correcto en la posición 'i'.
    for i in range(n):
        # Asumimos temporalmente que el primer elemento de la parte desordenada es el más pequeño.
        min_idx = i
        
        # Buscamos en el resto de la lista (desde i+1 hasta el final)
        # para ver si hay algún elemento más pequeño.
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Actualizamos el índice del elemento más pequeño encontrado.
                
        # Una vez encontrado el elemento más pequeño de la sublista desordenada,
        # lo intercambiamos con el primer elemento de esa sublista (posición i).
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [64, 25, 12, 22, 11, 90, 33, 1, 45, 7, 88]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = selection_sort(mi_lista)
    print(f"Lista ordenada por selección: {lista_ordenada}")