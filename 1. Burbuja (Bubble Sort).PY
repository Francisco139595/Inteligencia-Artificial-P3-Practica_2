def bubble_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento de burbuja (Bubble Sort).
    
    Incluye una optimización para detener la ejecución si la lista ya se encuentra ordenada.
    
    Complejidad de tiempo: O(n^2) en el peor/promedio caso, O(n) en el mejor caso.
    Complejidad de espacio: O(1) ya que modifica la lista in-place.
    """
    n = len(arr)
    for i in range(n - 1):
        intercambiado = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambiado:
            break
            
    return arr

if __name__ == "__main__":
    lista_prueba = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {lista_prueba}")
    bubble_sort(lista_prueba)
    print(f"Lista ordenada: {lista_prueba}")