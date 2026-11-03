import json
import os

# ==========================================
# ESTRUCTURAS AUXILIARES (TDA COLA Y ÁRBOL)
# ==========================================

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

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class IndiceTipo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.pokemons = []

class Pokemon:
    def __init__(self, numero, nombre, tipos, debilidades, mega, gigamax):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.debilidades = debilidades
        self.mega = mega
        self.gigamax = gigamax

# ==========================================
# FUNCIONES DE INSERCIÓN Y RECORRIDO DE ÁRBOLES
# ==========================================

def insertar_por_numero(raiz, pokemon):
    if raiz is None:
        return nodoArbol(pokemon)
    elif pokemon.numero < raiz.info.numero:
        raiz.izq = insertar_por_numero(raiz.izq, pokemon)
    else:
        raiz.der = insertar_por_numero(raiz.der, pokemon)
    return raiz

def insertar_por_nombre(raiz, pokemon):
    if raiz is None:
        return nodoArbol(pokemon)
    elif pokemon.nombre.lower() < raiz.info.nombre.lower():
        raiz.izq = insertar_por_nombre(raiz.izq, pokemon)
    else:
        raiz.der = insertar_por_nombre(raiz.der, pokemon)
    return raiz

def insertar_por_tipo(raiz, pokemon, tipo):
    if raiz is None:
        ind = IndiceTipo(tipo)
        ind.pokemons.append(pokemon)
        return nodoArbol(ind)
    elif tipo.lower() < raiz.info.tipo.lower():
        raiz.izq = insertar_por_tipo(raiz.izq, pokemon, tipo)
    elif tipo.lower() > raiz.info.tipo.lower():
        raiz.der = insertar_por_tipo(raiz.der, pokemon, tipo)
    else:
        raiz.info.pokemons.append(pokemon)
    return raiz

def buscar_por_numero(raiz, numero):
    if raiz is not None:
        if raiz.info.numero == numero:
            return raiz
        elif numero < raiz.info.numero:
            return buscar_por_numero(raiz.izq, numero)
        else:
            return buscar_por_numero(raiz.der, numero)
    return None

def buscar_por_nombre_proximidad(raiz, cadena, resultados):
    if raiz is not None:
        buscar_por_nombre_proximidad(raiz.izq, cadena, resultados)
        if cadena.lower() in raiz.info.nombre.lower():
            resultados.append(raiz.info)
        buscar_por_nombre_proximidad(raiz.der, cadena, resultados)

def inorden_numero(raiz):
    if raiz is not None:
        inorden_numero(raiz.izq)
        print(f"Nombre: {raiz.info.nombre} (Nro: #{raiz.info.numero}) | Tipos: {', '.join(raiz.info.tipos)}")
        inorden_numero(raiz.der)

def inorden_nombre(raiz):
    if raiz is not None:
        inorden_nombre(raiz.izq)
        print(f"Nombre: {raiz.info.nombre} (Nro: #{raiz.info.numero}) | Tipos: {', '.join(raiz.info.tipos)}")
        inorden_nombre(raiz.der)

def por_nivel(raiz):
    if raiz is not None:
        pendientes = Cola()
        arribo(pendientes, raiz)
        while not cola_vacia(pendientes):
            nodo = atencion(pendientes)
            print(f"[{nodo.info.nombre} (Nro: #{nodo.info.numero})]")
            if nodo.izq is not None:
                arribo(pendientes, nodo.izq)
            if nodo.der is not None:
                arribo(pendientes, nodo.der)

def inorden_tipos_conteo(raiz):
    if raiz is not None:
        inorden_tipos_conteo(raiz.izq)
        print(f"Tipo: {raiz.info.tipo} - Cantidad de Pokémon: {len(raiz.info.pokemons)}")
        inorden_tipos_conteo(raiz.der)

def contar_mega(raiz, contador):
    if raiz is not None:
        contar_mega(raiz.izq, contador)
        if raiz.info.mega:
            contador[0] += 1
        contar_mega(raiz.der, contador)

def contar_gigamax(raiz, contador):
    if raiz is not None:
        contar_gigamax(raiz.izq, contador)
        if raiz.info.gigamax:
            contador[0] += 1
        contar_gigamax(raiz.der, contador)

def buscar_tipo_especifico(raiz, tipo_buscado, encontrados):
    if raiz is not None:
        buscar_tipo_especifico(raiz.izq, tipo_buscado, encontrados)
        if raiz.info.tipo.lower() == tipo_buscado.lower():
            encontrados.extend(raiz.info.pokemons)
        buscar_tipo_especifico(raiz.der, tipo_buscado, encontrados)

def buscar_debilidades(raiz, tipo_debilidad, debiles):
    if raiz is not None:
        buscar_debilidades(raiz.izq, tipo_debilidad, debiles)
        for d in raiz.info.debilidades:
            if d.lower() == tipo_debilidad.lower():
                if raiz.info not in debiles:
                    debiles.append(raiz.info)
                break
        buscar_debilidades(raiz.der, tipo_debilidad, debiles)

# ==========================================
# LECTURA DE JSON Y CARGA DE LOS 100 POKÉMON
# ==========================================

arbol_numero = None
arbol_nombre = None
arbol_tipo = None
total_cargados = 0

# Obtener la ruta exacta de la carpeta donde está este script
directorio_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = os.path.join(directorio_actual, 'pokemons.json')

if not os.path.exists(nombre_archivo):
    print(f"Error: No se encontró el archivo en la ruta: {nombre_archivo}")
else:
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        datos_json = json.load(archivo)
        
        # Limitamos la carga estrictamente a los primeros 100 Pokémon del archivo JSON
        for item in datos_json[:100]:
            p = Pokemon(
                numero=item["numero"],
                nombre=item["nombre"],
                tipos=item["tipos"],
                debilidades=item["debilidades"],
                mega=item["mega"],
                gigamax=item["gigamax"]
            )
            arbol_numero = insertar_por_numero(arbol_numero, p)
            arbol_nombre = insertar_por_nombre(arbol_nombre, p)
            for t in p.tipos:
                arbol_tipo = insertar_por_tipo(arbol_tipo, p, t)
            total_cargados += 1

    print(f"¡Se cargaron e indexaron exitosamente {total_cargados} Pokémon!\n")

    # ==========================================
    # EJECUCIÓN DE LAS CONSIGNAS DEL EJERCICIO 1
    # ==========================================

    print("=== a. BÚSQUEDA POR NÚMERO (Ejemplo: #135) ===")
    res_num = buscar_por_numero(arbol_numero, 135)
    if res_num:
        pk = res_num.info
        print(f"Encontrado: {pk.nombre} (Nro: #{pk.numero}) | Tipos: {pk.tipos} | Debilidades: {pk.debilidades}")
    else:
        print("No se encontró el Pokémon con ese número.")

    print("\n=== a. BÚSQUEDA POR PROXIMIDAD DE NOMBRE ('Bulb') ===")
    resultados_prox = []
    buscar_por_nombre_proximidad(arbol_nombre, "Bulb", resultados_prox)
    for pk in resultados_prox:
        print(f"Coincidencia: {pk.nombre} (Nro: #{pk.numero}) | Tipos: {pk.tipos}")

    print("\n=== b. POKÉMONS DE TIPOS FANTASMA, FUEGO, ACERO Y ELÉCTRICO ===")
    tipos_solicitados = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
    for ts in tipos_solicitados:
        pok_tipo = []
        buscar_tipo_especifico(arbol_tipo, ts, pok_tipo)
        print(f"\n--- Tipo: {ts} (Total: {len(pok_tipo)}) ---")
        for pk in pok_tipo:
            print(f"  * {pk.nombre} (Nro: #{pk.numero})")

    print("\n=== c. MOSTRAR LISTADO EN ORDEN ASCENDENTE POR NÚMERO ===")
    inorden_numero(arbol_numero)

    print("\n=== c. MOSTRAR LISTADO EN ORDEN ASCENDENTE POR NOMBRE ===")
    inorden_nombre(arbol_nombre)

    print("\n=== c. MOSTRAR LISTADO POR NIVEL (ORGANIZADO POR NOMBRE) ===")
    por_nivel(arbol_nombre)

    print("\n=== d. POKÉMONS DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM ===")
    # Tipos correspondientes a estos Pokémon: Eléctrico, Roca y Dragón
    debilidades_objetivo = ["Eléctrico", "Roca", "Dragón"]
    for dob in debilidades_objetivo:
        debiles_list = []
        buscar_debilidades(arbol_nombre, dob, debiles_list)
        print(f"\nDébiles frente al tipo {dob}:")
        for pk in debiles_list:
            print(f"  - {pk.nombre} (Nro: #{pk.numero})")

    print("\n=== e. MOSTRAR TODOS LOS TIPOS DE POKÉMON Y SU CANTIDAD ===")
    inorden_tipos_conteo(arbol_tipo)

    print("\n=== ESTADÍSTICAS EXTRA DE MEGAEVOLUCIÓN Y GIGAMAX ===")
    contador_mega = [0]
    contar_mega(arbol_nombre, contador_mega)
    print(f"Pokémon con Megaevolución: {contador_mega[0]}")

    contador_giga = [0]
    contar_gigamax(arbol_nombre, contador_giga)
    print(f"Pokémon con forma Gigamax: {contador_giga[0]}")