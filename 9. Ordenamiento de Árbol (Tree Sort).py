from typing import List, Optional

class Node:
    """
    Clase que representa un nodo en un Árbol Binario de Búsqueda (BST).
    """
    def __init__(self, key):
        self.left: Optional['Node'] = None   # Hijo izquierdo
        self.right: Optional['Node'] = None  # Hijo derecho
        self.val: int = key                  # Valor del nodo

def insert(root: Optional[Node], key: int) -> Node:
    """
    Inserta un nuevo valor en el Árbol Binario de Búsqueda.
    
    Args:
        root: El nodo raíz del árbol (o subárbol) actual.
        key: El valor a insertar.
        
    Returns:
        La raíz del árbol modificado tras la inserción.
    """
    # Si el árbol está vacío, creamos un nuevo nodo y lo retornamos
    if root is None:
        return Node(key)
    else:
        # Si el valor a insertar es mayor que el valor del nodo actual,
        # lo insertamos en el subárbol derecho
        if root.val < key:
            root.right = insert(root.right, key)
        # Si es menor o igual, lo insertamos en el subárbol izquierdo
        else:
            root.left = insert(root.left, key)
    return root

def store_in_order(root: Optional[Node], arr: List[int], idx: List[int]):
    """
    Realiza un recorrido en inorden (in-order traversal) del árbol y 
    almacena los valores ordenados en la lista original.
    
    Args:
        root: El nodo raíz del árbol (o subárbol) actual.
        arr: La lista donde se guardarán los elementos ordenados.
        idx: Una lista con un solo elemento que actúa como contador por referencia.
    """
    if root:
        # Primero visitamos el subárbol izquierdo (elementos menores)
        store_in_order(root.left, arr, idx)
        
        # Almacenamos el valor del nodo actual en la posición que indica idx
        arr[idx[0]] = root.val
        idx[0] += 1
        
        # Finalmente visitamos el subárbol derecho (elementos mayores)
        store_in_order(root.right, arr, idx)

def tree_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista de elementos utilizando el algoritmo Tree Sort.
    
    Args:
        arr: Una lista de elementos a ordenar.
        
    Returns:
        La misma lista ordenada de forma ascendente (modificada in-place).
    """
    # Si la lista está vacía, la retornamos tal cual
    if not arr:
        return arr
        
    # Paso 1: Construir el Árbol Binario de Búsqueda (BST)
    root = None
    for key in arr:
        root = insert(root, key)
        
    # Paso 2: Extraer los elementos en orden usando un recorrido inorden
    idx = [0] # Usamos una lista de un elemento para modificar el índice por referencia
    store_in_order(root, arr, idx)
    
    return arr

if __name__ == "__main__":
    # Creamos una lista de ejemplo desordenada
    mi_lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f"Lista original desordenada: {mi_lista}")
    
    # Llamamos a nuestra función y guardamos el resultado
    lista_ordenada = tree_sort(mi_lista)
    print(f"Lista ordenada por Tree Sort: {lista_ordenada}")