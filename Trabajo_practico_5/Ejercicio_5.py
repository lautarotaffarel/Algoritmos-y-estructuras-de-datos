
class Personaje:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True: Héroe, False: Villano


    def __lt__(self, otro):
        return self.nombre < otro.nombre

    def __gt__(self, otro):
        return self.nombre > otro.nombre

    def __eq__(self, otro):
        return self.nombre == otro.nombre

    def __str__(self):
        tipo = "Héroe" if self.es_heroe else "Villano"
        return f"{self.nombre} ({tipo})"


class nodoArbol(object):
    """Clase nodo árbol binario[cite: 141]."""
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None



def insertar_nodo(raiz, dato):
    """Inserta un dato en el árbol manteniendo el orden alfabético por nombre[cite: 142]."""
    if raiz is None:
        raiz = nodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz



def listar_villanos(raiz):
    if raiz is not None:
        listar_villanos(raiz.izq)
        if not raiz.info.es_heroe:
            print(raiz.info.nombre)
        listar_villanos(raiz.der)



def heroes_empiezan_con_c(raiz):
    if raiz is not None:
        heroes_empiezan_con_c(raiz.izq)
        if raiz.info.es_heroe and raiz.info.nombre.startswith('C'):
            print(raiz.info.nombre)
        heroes_empiezan_con_c(raiz.der)


def contar_superheroes(raiz):
    if raiz is None:
        return 0
    contador = 1 if raiz.info.es_heroe else 0
    return contador + contar_superheroes(raiz.izq) + contar_superheroes(raiz.der)


def busqueda_proximidad(raiz, termino):
    """Busca nodos cuyo nombre contenga el término de proximidad (búsqueda parcial)."""
    if raiz is not None:
        busqueda_proximidad(raiz.izq, termino)
        if termino.lower() in raiz.info.nombre.lower():
            print(f"Encontrado por proximidad: {raiz.info.nombre}")
            # Modificar nombre corregido
            raiz.info.nombre = "Doctor Strange"
            print(f"Nombre actualizado a: {raiz.info.nombre}")
        busqueda_proximidad(raiz.der, termino)


def listar_heroes_descendente(raiz):
    if raiz is not None:
        listar_heroes_descendente(raiz.der)
        if raiz.info.es_heroe:
            print(raiz.info.nombre)
        listar_heroes_descendente(raiz.izq)


def generar_bosque(raiz, arbol_heroes, arbol_villanos):
    if raiz is not None:
        arbol_heroes, arbol_villanos = generar_bosque(raiz.izq, arbol_heroes, arbol_villanos)
        if raiz.info.es_heroe:
            arbol_heroes = insertar_nodo(arbol_heroes, raiz.info)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, raiz.info)
        arbol_heroes, arbol_villanos = generar_bosque(raiz.der, arbol_heroes, arbol_villanos)
    return arbol_heroes, arbol_villanos


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)


def barrido_alfabetico(raiz):
    if raiz is not None:
        barrido_alfabetico(raiz.izq)
        print(raiz.info)
        barrido_alfabetico(raiz.der)




        # Inicialización del árbol MCU
arbol_mcu = None

# Carga de datos de ejemplo (Nombre, Es Héroe [True/False])
personajes = [
    Personaje("Iron Man", True),
    Personaje("Thanos", False),
    Personaje("Capitan America", True),
    Personaje("Loki", False),
    Personaje("Dr. Stange", True),  # Cargado erróneamente para la prueba de proximidad
    Personaje("Ultron", False),
    Personaje("Thor", True),
    Personaje("Hela", False),
    Personaje("Capitana Marvel", True),
    Personaje("Spider-Man", True)
]

for p in personajes:
    arbol_mcu = insertar_nodo(arbol_mcu, p)

print("--- b. Listado de Villanos ordenados alfabéticamente ---")
listar_villanos(arbol_mcu)

print("\n--- c. Superhéroes que empiezan con C ---")
heroes_empiezan_con_c(arbol_mcu)

print(f"\n--- d. Cantidad de Superhéroes ---")
print(f"Total: {contar_superheroes(arbol_mcu)}")

print("\n--- e. Búsqueda por proximidad ('Stange') y corrección ---")
busqueda_proximidad(arbol_mcu, "Stange")

print("\n--- f. Superhéroes ordenados de manera descendente ---")
listar_heroes_descendente(arbol_mcu)

print("\n--- g. Generación de Bosque (Héroes y Villanos) ---")
arbol_h, arbol_v = None, None
arbol_h, arbol_v = generar_bosque(arbol_mcu, arbol_h, arbol_v)

print(f"G.I. Nodos en Árbol de Héroes: {contar_nodos(arbol_h)}")
print(f"G.I. Nodos en Árbol de Villanos: {contar_nodos(arbol_v)}")

print("\nG.II. Barrido alfabético del Árbol de Héroes:")
barrido_alfabetico(arbol_h)

print("\nG.II. Barrido alfabético del Árbol de Villanos:")
barrido_alfabetico(arbol_v)