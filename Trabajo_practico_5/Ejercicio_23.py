from collections import deque

class Criatura:
    def __init__(self, nombre, derrotado_por="-", descripcion="", capturada="-"):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.capturada = capturada

    def __lt__(self, otro):
        return self.nombre < otro.nombre

    def __gt__(self, otro):
        return self.nombre > otro.nombre

    def __eq__(self, otro):
        return self.nombre == otro.nombre

    def __str__(self):
        return (f"Criatura: {self.nombre} | Derrotado por: {self.derrotado_por} | "
                f"Capturada por: {self.capturada} | Descripción: {self.descripcion}")

class NodoArbol:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

# Inserción en el Árbol Binario de Búsqueda (ABB)
def insertar_nodo(raiz, dato):
    if raiz is None:
        return NodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    elif dato > raiz.info:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

# Búsqueda exacta por nombre
def buscar(raiz, clave):
    if raiz is None:
        return None
    if raiz.info.nombre.lower() == clave.lower():
        return raiz
    elif clave.lower() < raiz.info.nombre.lower():
        return buscar(raiz.izq, clave)
    else:
        return buscar(raiz.der, clave)

# a. Listado inorden de las criaturas y quién las derrotó
def inorden_criaturas(raiz):
    if raiz is not None:
        inorden_criaturas(raiz.izq)
        print(f"• {raiz.info.nombre} — Derrotado por: {raiz.info.derrotado_por}")
        inorden_criaturas(raiz.der)

# c. Mostrar toda la información de una criatura específica (ej. Talos)
def mostrar_informacion(raiz, nombre):
    nodo = buscar(raiz, nombre)
    if nodo:
        print(nodo.info)
    else:
        print(f"La criatura '{nombre}' no se encuentra en el árbol.")

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
def top_derrotadores(raiz):
    conteo = {}
    
    def recorrer(nodo):
        if nodo:
            recorrer(nodo.izq)
            h = nodo.info.derrotado_por
            if h and h != "-":
                conteo[h] = conteo.get(h, 0) + 1
            recorrer(nodo.der)
            
    recorrer(raiz)
    top_3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    print("--- Top 3 Héroes / Dioses con más derrotas ---")
    for heroe, cantidad in top_3:
        print(f"{heroe}: {cantidad} criaturas")

# e. Listar las criaturas derrotadas por un héroe específico (ej. Heracles)
def listar_por_heroe(raiz, heroe_buscado):
    if raiz is not None:
        listar_por_heroe(raiz.izq, heroe_buscado)
        if raiz.info.derrotado_por.lower() == heroe_buscado.lower():
            print(f"• {raiz.info.nombre}")
        listar_por_heroe(raiz.der, heroe_buscado)

# f. Listar las criaturas que no han sido derrotadas
def listar_no_derrotadas(raiz):
    if raiz is not None:
        listar_no_derrotadas(raiz.izq)
        if raiz.info.derrotado_por == "-":
            print(f"• {raiz.info.nombre}")
        listar_no_derrotadas(raiz.der)

# i. Búsquedas por coincidencia (parcial)
def busqueda_coincidencia(raiz, termino):
    if raiz is not None:
        busqueda_coincidencia(raiz.izq, termino)
        if termino.lower() in raiz.info.nombre.lower():
            print(f"Coincidencia encontrada: {raiz.info}")
        busqueda_coincidencia(raiz.der, termino)

# j. Eliminación de nodos
def reemplazar(raiz):
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if raiz is not None:
        if clave.lower() < raiz.info.nombre.lower():
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave.lower() > raiz.info.nombre.lower():
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

# m. Listado por nivel del árbol (Barrido por amplitud usando Cola)
def por_nivel(raiz):
    if raiz is not None:
        cola = deque([raiz])
        while cola:
            nodo = cola.popleft()
            print(f"• {nodo.info.nombre} (Derrotado por: {nodo.info.derrotado_por} | Capturado: {nodo.info.capturada})")
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)

# n. Mostrar las criaturas capturadas por un héroe (ej. Heracles)
def listar_capturadas_por(raiz, heroe):
    if raiz is not None:
        listar_capturadas_por(raiz.izq, heroe)
        if raiz.info.capturada.lower() == heroe.lower():
            print(f"• {raiz.info.nombre}")
        listar_capturadas_por(raiz.der, heroe)



        # Inicializar el árbol
arbol_mitologia = None

# Lista de datos extraídos de la tabla original
datos_tabla = [
    ("Ceto", "-"), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"), ("Dino", "-"),
    ("Pefredo", "-"), ("Enio", "-"), ("Escila", "-"), ("Caribdis", "-"),
    ("Euríale", "-"), ("Esteno", "-"), ("Medusa", Perseo := "Perseo"), ("Ladón", "Heracles"),
    ("Águila del Cáucaso", "-"), ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"), ("Dragón de la Cólquida", "-"),
    ("Cerbero", "-"), ("Cerda de Cromión", "Teseo"), ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"), ("Jabalí de Calidón", "Atalanta"), ("Carcinos", "-"),
    ("Gerión", "Heracles"), ("Cloto", "-"), ("Láquesis", "-"), ("Átropos", "-"),
    ("Minotauro de Creta", "Teseo"), ("Harpías", "-"), ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", "-"), ("Talos", "Medea"), ("Sirenas", "-"),
    ("Pitón", "Apolo"), ("Cierva de Cerinea", "-"), ("Basilisco", "-"),
    ("Jabalí de Erimanto", "-")
]

# Poblar el árbol con descripciones por defecto (punto b)
for nombre, derrotado in datos_tabla:
    criatura = Criatura(nombre, derrotado, descripcion=f"Mitológica criatura llamada {nombre}.")
    arbol_mitologia = insertar_nodo(arbol_mitologia, criatura)

# h. Modificar nodos de Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto (capturadas por Heracles)
for nombre_criatura in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    nodo = buscar(arbol_mitologia, nombre_criatura)
    if nodo:
        nodo.info.capturada = "Heracles"

# k. Modificar aves del Estínfalo (Heracles derrotó a varias)
aves = buscar(arbol_mitologia, "Aves del Estínfalo")
if aves:
    aves.info.derrotado_por = "Heracles (varias)"

# l. Modificar el nombre de la criatura Ladón por Dragón Ladón
ladon_nodo = buscar(arbol_mitologia, "Ladón")
if ladon_nodo:
    # Como es un ABB ordenado por nombre, reinsertamos con el nuevo nombre y eliminamos el viejo
    datos_ladon = ladon_nodo.info
    datos_ladon.nombre = "Dragón Ladón"
    arbol_mitologia, _ = eliminar_nodo(arbol_mitologia, "Ladón")
    arbol_mitologia = insertar_nodo(arbol_mitologia, datos_ladon)

# j. Eliminar al Basilisco y a las Sirenas
arbol_mitologia, _ = eliminar_nodo(arbol_mitologia, "Basilisco")
arbol_mitologia, _ = eliminar_nodo(arbol_mitologia, "Sirenas")


print("=== a. LISTADO INORDEN (Criaturas y quién las derrotó) ===")
inorden_criaturas(arbol_mitologia)

print("\n=== c. INFORMACIÓN DE LA CRIATURA 'Talos' ===")
mostrar_informacion(arbol_mitologia, "Talos")

print("\n=== d. TOP 3 HÉROES / DIOSES QUE DERROTARON MÁS CRIATURAS ===")
top_derrotadores(arbol_mitologia)

print("\n=== e. CRIATURAS DERROTADAS POR HERACLES ===")
listar_por_heroe(arbol_mitologia, "Heracles")
listar_por_heroe(arbol_mitologia, "Heracles (varias)")

print("\n=== f. CRIATURAS QUE NO HAN SIDO DERROTADAS ===")
listar_no_derrotadas(arbol_mitologia)

print("\n=== i. BÚSQUEDA POR COINCIDENCIA ('Dragón') ===")
busqueda_coincidencia(arbol_mitologia, "Dragón")

print("\n=== m. LISTADO POR NIVEL DEL ÁRBOL ===")
por_nivel(arbol_mitologia)

print("\n=== n. CRIATURAS CAPTURADAS POR HERACLES ===")
listar_capturadas_por(arbol_mitologia, "Heracles")