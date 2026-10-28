def eliminar_arista(vertice, destino):
    """
    Elimina y devuelve del vértice la arista que coincida con el destino dado 
    (el primero que encuentre). Si no se encuentra, devuelve None.
    """
    # Suponiendo que 'vertice.aristas' es una lista enlazada o una lista común 
    # que almacena las aristas (donde cada arista tiene un campo 'destino')
    
    # Si la arista a eliminar está al principio de la lista de adyacencia del vértice:
    if vertice.aristas.inicio is not None:
        # Verificamos si el primer elemento coincide con el destino
        if criterio(vertice.aristas.inicio.info, 'destino') == destino:
            dato = eliminar(vertice.aristas, vertice.aristas.inicio.info, 'destino')
            return dato
        else:
            # Si no está al inicio, recorremos con punteros anterior y actual
            anterior = vertice.aristas.inicio
            actual = vertice.aristas.inicio.sig
            
            while actual is not None and criterio(actual.info, 'destino') != destino:
                anterior = anterior.sig
                actual = actual.sig
                
            # Si 'actual' no es None, significa que encontró la arista
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                vertice.aristas.tamanio -= 1
                return dato
                
    return None