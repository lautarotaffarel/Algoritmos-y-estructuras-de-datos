import sys

# ==========================================
# ESTRUCTURAS AUXILIARES (TDA LISTA Y COLA)
# ==========================================

class nodoLista(object):
    def __init__(self):
        self.info = None
        self.sig = None

class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (criterio(lista.inicio.info, campo) > criterio(dato, campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not None) and (criterio(act.info, campo) < criterio(dato, campo)):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1

def eliminar(lista, clave, campo=None):
    dato = None
    if lista.inicio is not None:
        if criterio(lista.inicio.info, campo) == criterio(clave, campo):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while (act is not None) and (criterio(act.info, campo) != criterio(clave, campo)):
                ant = act
                act = act.sig
            if act is not None:
                dato = act.info
                ant.sig = act.sig
                lista.tamanio -= 1
    return dato

def buscar(lista, buscado, campo=None):
    aux = lista.inicio
    while (aux is not None) and (criterio(aux.info, campo) != criterio(buscado, campo)):
        aux = aux.sig
    return aux

def criterio(dato, campo=None):
    if campo is None:
        return dato
    partes = campo.split('.')
    obj = dato
    for parte in partes:
        if hasattr(obj, '__dict__') and parte in obj.__dict__:
            obj = obj.__dict__[parte]
        elif hasattr(obj, parte):
            obj = getattr(obj, parte)
        else:
            return dato
    return obj

class nodoCola(object):
    def __init__(self):
        self.info = None
        self.sig = None

class Cola(object):
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato

def cola_vacia(cola):
    return cola.frente is None

class nodoPila(object):
    def __init__(self):
        self.info = None
        self.sig = None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

def apilar(pila, dato):
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

def pila_vacia(pila):
    return pila.cima is None

# ==========================================
# TDA GRAFO (IMPLEMENTACIÓN ADYACENCIA)
# ==========================================

class NodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.visitado = False
        self.adyacentes = Lista()

class NodoArista(object):
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

class Grafo(object):
    def __init__(self, dirijido=False):
        self.vertices = Lista()
        self.dirijido = dirijido

def insertar_vertice(grafo, dato):
    nodo = NodoVertice(dato)
    insertar(grafo.vertices, nodo, 'info')

def insertar_arista(grafo, peso, origen, destino):
    ver_origen = buscar(grafo.vertices, origen, 'info')
    ver_destino = buscar(grafo.vertices, destino, 'info')
    if (ver_origen is not None) and (ver_destino is not None):
        # Se extrae .info para almacenar directamente el NodoVertice
        arista = NodoArista(ver_destino.info, peso)
        insertar(ver_origen.info.adyacentes, arista, 'destino.info')
        if not grafo.dirijido:
            arista = NodoArista(ver_origen.info, peso)
            insertar(ver_destino.info.adyacentes, arista, 'destino.info')

def buscar_vertice(grafo, criterio_busqueda):
    return buscar(grafo.vertices, criterio_busqueda, 'info')

# ==========================================
# ALGORITMO DE PRIM (ÁRBOL DE EXPANSIÓN MÍNIMO)
# ==========================================

def prim(grafo, inicio):
    vertice_origen = buscar_vertice(grafo, inicio)
    if vertice_origen is None:
        return None
    
    aux = grafo.vertices.inicio
    while aux is not None:
        aux.info.visitado = False
        aux = aux.sig
        
    bosque = Lista()
    vertice_origen.info.visitado = True
    
    cant_vertices = grafo.vertices.tamanio
    for _ in range(cant_vertices - 1):
        menor_peso = sys.maxsize
        v_origen = None
        v_destino = None
        
        curr = grafo.vertices.inicio
        while curr is not None:
            if curr.info.visitado:
                ady = curr.info.adyacentes.inicio
                while ady is not None:
                    if not ady.info.destino.visitado:
                        if ady.info.peso < menor_peso:
                            menor_peso = ady.info.peso
                            v_origen = curr.info
                            v_destino = ady.info.destino
                    ady = ady.sig
            curr = curr.sig
            
        if v_destino is not None:
            v_destino.visitado = True
            reg = f"{v_origen.info} - {v_destino.info} (Episodios juntos: {menor_peso})"
            insertar(bosque, reg)
            
    return bosque

# ==========================================
# ALGORITMO DE DIJKSTRA (CAMINO MÁS CORTO)
# ==========================================

def dijkstra(grafo, origen, destino):
    ver_origen = buscar_vertice(grafo, origen)
    ver_destino = buscar_vertice(grafo, destino)
    if ver_origen is None or ver_destino is None:
        return None, None
        
    dist = {}
    padre = {}
    
    curr = grafo.vertices.inicio
    while curr is not None:
        dist[curr.info.info] = sys.maxsize
        padre[curr.info.info] = None
        curr.info.visitado = False
        curr = curr.sig
        
    dist[origen] = 0
    
    for _ in range(grafo.vertices.tamanio):
        min_dist = sys.maxsize
        u = None
        curr = grafo.vertices.inicio
        while curr is not None:
            if not curr.info.visitado and dist[curr.info.info] < min_dist:
                min_dist = dist[curr.info.info]
                u = curr.info
            curr = curr.sig
            
        if u is None:
            break
            
        u.visitado = True
        
        ady = u.adyacentes.inicio
        while ady is not None:
            v = ady.info.destino
            peso = ady.info.peso
            if not v.visitado and dist[u.info] + peso < dist[v.info]:
                dist[v.info] = dist[u.info] + peso
                padre[v.info] = u.info
            ady = ady.sig
            
    camino = Pila()
    paso = destino
    while paso is not None:
        apilar(camino, paso)
        paso = padre[paso]
        
    return dist[destino], camino

# ==========================================
# RESOLUCIÓN DE CONSIGNAS
# ==========================================

grafo_starwars = Grafo(dirijido=False)

personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for p in personajes:
    insertar_vertice(grafo_starwars, p)

# Carga de relaciones (peso = cantidad de episodios compartidos)
insertar_arista(grafo_starwars, 5, "C-3PO", "R2-D2")
insertar_arista(grafo_starwars, 6, "C-3PO", "Luke Skywalker")
insertar_arista(grafo_starwars, 6, "C-3PO", "Leia")
insertar_arista(grafo_starwars, 4, "C-3PO", "Han Solo")
insertar_arista(grafo_starwars, 4, "C-3PO", "Chewbacca")
insertar_arista(grafo_starwars, 4, "C-3PO", "Darth Vader")
insertar_arista(grafo_starwars, 3, "C-3PO", "Yoda")
insertar_arista(grafo_starwars, 3, "C-3PO", "BB-8")
insertar_arista(grafo_starwars, 3, "C-3PO", "Rey")

insertar_arista(grafo_starwars, 6, "R2-D2", "Luke Skywalker")
insertar_arista(grafo_starwars, 6, "R2-D2", "Leia")
insertar_arista(grafo_starwars, 4, "R2-D2", "Han Solo")
insertar_arista(grafo_starwars, 4, "R2-D2", "Chewbacca")
insertar_arista(grafo_starwars, 4, "R2-D2", "Darth Vader")
insertar_arista(grafo_starwars, 3, "R2-D2", "Yoda")
insertar_arista(grafo_starwars, 3, "R2-D2", "BB-8")

insertar_arista(grafo_starwars, 5, "Luke Skywalker", "Leia")
insertar_arista(grafo_starwars, 4, "Luke Skywalker", "Han Solo")
insertar_arista(grafo_starwars, 4, "Luke Skywalker", "Chewbacca")
insertar_arista(grafo_starwars, 4, "Luke Skywalker", "Darth Vader")
insertar_arista(grafo_starwars, 3, "Luke Skywalker", "Yoda")
insertar_arista(grafo_starwars, 2, "Luke Skywalker", "Rey")
insertar_arista(grafo_starwars, 2, "Luke Skywalker", "Kylo Ren")

insertar_arista(grafo_starwars, 4, "Leia", "Han Solo")
insertar_arista(grafo_starwars, 4, "Leia", "Chewbacca")
insertar_arista(grafo_starwars, 3, "Leia", "Darth Vader")
insertar_arista(grafo_starwars, 3, "Leia", "Rey")
insertar_arista(grafo_starwars, 3, "Leia", "Kylo Ren")

insertar_arista(grafo_starwars, 4, "Han Solo", "Chewbacca")
insertar_arista(grafo_starwars, 2, "Han Solo", "Darth Vader")
insertar_arista(grafo_starwars, 2, "Han Solo", "Boba Fett")
insertar_arista(grafo_starwars, 2, "Han Solo", "Rey")
insertar_arista(grafo_starwars, 2, "Han Solo", "Kylo Ren")

insertar_arista(grafo_starwars, 2, "Chewbacca", "Darth Vader")
insertar_arista(grafo_starwars, 2, "Chewbacca", "Boba Fett")
insertar_arista(grafo_starwars, 3, "Chewbacca", "Rey")
insertar_arista(grafo_starwars, 3, "Chewbacca", "Kylo Ren")
insertar_arista(grafo_starwars, 3, "Chewbacca", "BB-8")

insertar_arista(grafo_starwars, 2, "Darth Vader", "Boba Fett")
insertar_arista(grafo_starwars, 2, "Darth Vader", "Yoda")

insertar_arista(grafo_starwars, 3, "Rey", "Kylo Ren")
insertar_arista(grafo_starwars, 3, "Rey", "BB-8")
insertar_arista(grafo_starwars, 3, "Kylo Ren", "BB-8")

print("=== ÁRBOL DE EXPANSIÓN MÍNIMO (PRIM) DESDE C-3PO ===")
mst_c3po = prim(grafo_starwars, "C-3PO")
if mst_c3po:
    aux = mst_c3po.inicio
    while aux is not None:
        print(f"  {aux.info}")
        aux = aux.sig

print("\n=== ÁRBOL DE EXPANSIÓN MÍNIMO (PRIM) DESDE YODA ===")
mst_yoda = prim(grafo_starwars, "Yoda")
if mst_yoda:
    aux = mst_yoda.inicio
    while aux is not None:
        print(f"  {aux.info}")
        aux = aux.sig

print("\n=== ÁRBOL DE EXPANSIÓN MÍNIMO (PRIM) DESDE LEIA ===")
mst_leia = prim(grafo_starwars, "Leia")
if mst_leia:
    aux = mst_leia.inicio
    while aux is not None:
        print(f"  {aux.info}")
        aux = aux.sig

print("\n=== MÁXIMO NÚMERO DE EPISODIOS COMPARTIDOS Y PARES COINCIDENTES ===")
max_episodios = 0
pares_max = Lista()

curr_v = grafo_starwars.vertices.inicio
while curr_v is not None:
    curr_a = curr_v.info.adyacentes.inicio
    while curr_a is not None:
        peso = curr_a.info.peso
        if peso > max_episodios:
            max_episodios = peso
        curr_a = curr_a.sig
    curr_v = curr_v.sig

curr_v = grafo_starwars.vertices.inicio
while curr_v is not None:
    curr_a = curr_v.info.adyacentes.inicio
    while curr_a is not None:
        if curr_a.info.peso == max_episodios:
            p1 = curr_v.info.info
            p2 = curr_a.info.destino.info
            if p1 < p2:
                par_str = f"{p1} y {p2}"
                if buscar(pares_max, par_str) is None:
                    insertar(pares_max, par_str)
        curr_a = curr_a.sig
    curr_v = curr_v.sig

print(f"Número máximo de episodios compartidos: {max_episodios}")
print("Pares de personajes:")
aux = pares_max.inicio
while aux is not None:
    print(f"  - {aux.info}")
    aux = aux.sig

print