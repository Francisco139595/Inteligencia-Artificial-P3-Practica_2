from typing import List

def counting_sort_for_radix(arr: List[int], exp1: int):
    """
    Función auxiliar que realiza el Counting Sort de arr[] según el 
    dígito representado por exp1 (1, 10, 100, etc.).
    """
    n = len(arr)
    output = [0] * n # Arreglo de salida
    count = [0] * 10 # Arreglo para contar la ocurrencia de los dígitos (0-9)
    
    # Contamos la frecuencia de cada dígito en la posición actual
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
        
    # Modificamos count[] para que ahora contenga las posiciones reales
    # de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # Construimos el arreglo de salida 'output'
    # Recorremos el arreglo de atrás hacia adelante para mantener la estabilidad del algoritmo
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    # Copiamos el arreglo de salida al arreglo original arr[], de manera
    # que arr[] ahora contenga los números ordenados según el dígito actual
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de números enteros utilizando el algoritmo Radix Sort.
    
    Args:
        arr: Una lista de números enteros a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente.
    """
    # Si la lista está vacía, la retornamos tal cual
    if not arr:
        return arr
        
    # Encontramos el número máximo para saber la cantidad máxima de dígitos
    max1 = max(arr)
    
    # Aplicamos counting sort a cada dígito. 'exp' es 10^i, 
    # donde i es la posición del dígito actual (1 para unidades, 10 para decenas, etc.)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
        
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = radix_sort(mi_lista)
    print(f"Lista ordenada por Radix Sort: {lista_ordenada}")