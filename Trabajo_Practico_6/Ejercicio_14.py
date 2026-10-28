def existe_paso(grafo, origen, destino):
    """
    Devuelve True si es posible ir desde el vértice origen hasta el vértice destino, 
    caso contrario retorna False. Utiliza un recorrido (como DFS o BFS) con un conjunto 
    o lista de visitados para evitar ciclos.
    """
    # Verificamos si ambos vértices existen en el grafo
    if origen not in grafo.vertices or destino not in grafo.vertices:
        return False

    visitados = set()
    
    # Función auxiliar recursiva para realizar el recorrido en profundidad (DFS)
    def dfs(vertice_actual):
        # Si llegamos al destino, encontramos un camino
        if vertice_actual == destino:
            return True
        
        visitados.add(vertice_actual)
        
        # Obtenemos las aristas o adyacencias del vértice actual
        # (Dependiendo de la implementación del TDA grafo del libro)
        nodo_adj = grafo.vertices[vertice_actual].aristas.inicio
        while nodo_adj is not None:
            adyacente = nodo_adj.info.destino  # O el campo que almacene el vértice destino de la arista
            if adyacente not in visitados:
                if dfs(adyacente):
                    return True
            nodo_adj = nodo_adj.sig
            
        return False

    return dfs(origen)