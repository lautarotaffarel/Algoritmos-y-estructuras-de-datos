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
        print(f"Nro: {raiz.info.numero} | Nombre: {raiz.info.nombre} | Tipos: {raiz.info.tipos}")
        inorden_numero(raiz.der)

def inorden_nombre(raiz):
    if raiz is not None:
        inorden_nombre(raiz.izq)
        print(f"Nombre: {raiz.info.nombre} | Nro: {raiz.info.numero} | Tipos: {raiz.info.tipos}")
        inorden_nombre(raiz.der)

def por_nivel(raiz):
    if raiz is not None:
        pendientes = Cola()
        arribo(pendientes, raiz)
        while not cola_vacia(pendientes):
            nodo = atencion(pendientes)
            print(f"[{nodo.info.nombre} (# {nodo.info.numero})]")
            if nodo.izq is not None:
                arribo(pendientes, nodo.izq)
            if nodo.der is not None:
                arribo(pendientes, nodo.der)

def inorden_tipos_conteo(raiz):
    if raiz is not None:
        inorden_tipos_conteo(raiz.izq)
        print(f"Tipo: {raiz.info.tipo} - Cantidad: {len(raiz.info.pokemons)}")
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

tipos_posibles = ["Planta", "Fuego", "Agua", "Eléctrico", "Fantasma", "Acero", "Roca", "Dragón", "Normal", "Veneno"]
debilidades_posibles = ["Agua", "Fuego", "Planta", "Eléctrico", "Roca", "Dragón", "Tierra", "Hielo"]

arbol_numero = None
arbol_nombre = None
arbol_tipo = None

lista_pokemons_generados = []

datos_especificos = [
    Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Psíquico", "Volador"], False, False),
    Pokemon(135, "Jolteon", ["Eléctrico"], ["Tierra"], False, False),
    Pokemon(745, "Lycanroc", ["Roca"], ["Agua", "Lucha", "Planta", "Tierra", "Acero"], False, False),
    Pokemon(697, "Tyrantrum", ["Roca", "Dragón"], ["Acero", "Dragón", "Hada", "Hielo", "Lucha", "Tierra"], False, False),
]

for p in datos_especificos:
    lista_pokemons_generados.append(p)

nombres_base = ["Pikachu", "Charizard", "Gengar", "Lucario", "Snorlax", "Mewtwo", "Dragonite", "Tyranitar", "Blaziken", "Gardevoir",
                "Greninja", "Mimikyu", "Rayquaza", "Dialga", "Palkia", "Giratina", "Arceus", "Zekrom", "Reshiram", "Kyurem",
                "Xerneas", "Yveltal", "Zygarde", "Solgaleo", "Lunala", "Necrozma", "Zacian", "Zamazenta", "Eternatus", "Urshifu",
                "Calyrex", "Infernape", "Torterra", "Empoleon", "Staraptor", "Luxray", "Garchomp", "Lucario", "Abomasnow", "Weavile",
                "Magnezone", "Rhyperior", "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor",
                "Mamoswaine", "Porygon-Z", "Gallade", "Dusknoir", "Froslass", "Rotom", "Uxie", "Mesprit", "Azelf", "Heatran",
                "Regigigas", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Arceus", "Victini", "Snivy", "Servine",
                "Serperior", "Pignite", "Emboar", "Oshawott", "Dewott", "Samurott", "Patrat", "Watchog", "Lillipup", "Herdier",
                "Stoutland", "Purrloin", "Liepard", "Pansage", "Simisage", "Pansear", "Simisear", "Panpour", "Simipour", "Munna",
                "Musharna", "Pidove", "Tranquill", "Unfezant", "Blitzle", "Zebstrika", "Roggenrola", "Boldore", "Gigalith", "Woobat"]

for i in range(5, 125):
    num = i
    nombre = f"{nombres_base[(i-5) % len(nombres_base)]}-{i}"
    if i == 6:
        nombre = "Charizard"
    elif i == 94:
        nombre = "Gengar"
    elif i == 448:
        nombre = "Lucario"
    
    t = [tipos_posibles[i % len(tipos_posibles)]]
    if i % 3 == 0:
        t.append(tipos_posibles[(i+1) % len(tipos_posibles)])
    
    deb = [debilidades_posibles[i % len(debilidades_posibles)]]
    if i % 2 == 0:
        deb.append(debilidades_posibles[(i+2) % len(debilidades_posibles)])
        
    mega = (i % 7 == 0)
    gigamax = (i % 11 == 0)
    
    p = Pokemon(num, nombre, t, deb, mega, gigamax)
    lista_pokemons_generados.append(p)

for p in lista_pokemons_generados:
    arbol_numero = insertar_por_numero(arbol_numero, p)
    arbol_nombre = insertar_por_nombre(arbol_nombre, p)
    for t in p.tipos:
        arbol_tipo = insertar_por_tipo(arbol_tipo, p, t)

print("=== BÚSQUEDA POR NÚMERO (Ej: 135) ===")
res_num = buscar_por_numero(arbol_numero, 135)
if res_num:
    pk = res_num.info
    print(f"Encontrado -> #{pk.numero} {pk.nombre}, Tipos: {pk.tipos}, Debilidades: {pk.debilidades}, Mega: {pk.mega}, Gigamax: {pk.gigamax}")

print("\n=== BÚSQUEDA POR PROXIMIDAD DE NOMBRE ('bul') ===")
resultados_prox = []
buscar_por_nombre_proximidad(arbol_nombre, "bul", resultados_prox)
for pk in resultados_prox:
    print(f"Coincidencia -> #{pk.numero} {pk.nombre}, Tipos: {pk.tipos}")

print("\n=== POKÉMONS DE TIPOS: FANTASMA, FUEGO, ACERO Y ELÉCTRICO ===")
tipos_solicitados = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for ts in tipos_solicitados:
    pok_tipo = []
    buscar_tipo_especifico(arbol_tipo, ts, pok_tipo)
    print(f"--- Tipo: {ts} (Total: {len(pok_tipo)}) ---")
    for pk in pok_tipo:
        print(f"  * {pk.nombre} (#{pk.numero})")

print("\n=== LISTADO EN ORDEN ASCENDENTE POR NÚMERO ===")
inorden_numero(arbol_numero)

print("\n=== LISTADO EN ORDEN ASCENDENTE POR NOMBRE ===")
inorden_nombre(arbol_nombre)

print("\n=== LISTADO POR NIVEL POR NOMBRE ===")
por_nivel(arbol_nombre)

print("\n=== POKÉMONS DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM ===")
debilidades_objetivo = ["Eléctrico", "Roca", "Dragón"]
for dob in debilidades_objetivo:
    debiles_list = []
    buscar_debilidades(arbol_nombre, dob, debiles_list)
    print(f"Débiles frente al tipo {dob} (por Pokémon como Jolteon/Lycanroc/Tyrantrum):")
    for pk in debiles_list:
        print(f"  - {pk.nombre} (#{pk.numero})")

print("\n=== TODOS LOS TIPOS Y CANTIDAD DE POKÉMONS ===")
inorden_tipos_conteo(arbol_tipo)

print("\n=== ESTADÍSTICAS DE MEGAEVOLUCIÓN Y GIGAMAX ===")
contador_mega = [0]
contar_mega(arbol_nombre, contador_mega)
print(f"Pokémons con Megaevolución: {contador_mega[0]}")

contador_giga = [0]
contar_gigamax(arbol_nombre, contador_giga)
print(f"Pokémons con forma Gigamax: {contador_giga[0]}")