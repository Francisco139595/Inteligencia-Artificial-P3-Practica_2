from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenamiento por enumeración (Counting Sort).
    
    Args:
        arr: Una lista de números enteros a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente.
    """
    # Si la lista está vacía, la retornamos tal cual
    if not arr:
        return arr
        
    # Encontramos el valor máximo y mínimo para determinar el rango de los datos
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    # Inicializamos el arreglo de conteo y el arreglo de salida
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # 1. Contamos las frecuencias de cada elemento en la lista original
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_val] += 1

    # 2. Modificamos el arreglo de conteo para que almacene las posiciones reales
    # (sumas acumuladas) de los elementos en el arreglo de salida
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # 3. Construimos el arreglo de salida iterando de atrás hacia adelante 
    # para mantener la estabilidad del algoritmo
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    # 4. Copiamos los elementos ordenados del arreglo de salida al arreglo original
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
        
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada (incluyendo números negativos y repetidos)
    mi_lista = [4, 2, 2, 8, 3, 3, 1, -2, 5, -5, 0]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = counting_sort(mi_lista)
    print(f"Lista ordenada por Counting Sort: {lista_ordenada}")