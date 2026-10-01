# Estructura de datos de prueba
entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 85,
        "pokemons": [
            {"nombre": "Pikachu", "nivel": 88, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Charizard", "nivel": 75, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"}, # Repetido
            {"nombre": "Bulbasaur", "nivel": 60, "tipo": "Planta", "subtipo": "Veneno"}
        ]
    },
    {
        "nombre": "Misty",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemons": [
            {"nombre": "Gyaraos", "nivel": 65, "tipo": "Agua", "subtipo": "Volador"},
            {"nombre": "Psyduck", "nivel": 35, "tipo": "Agua", "subtipo": None},
            {"nombre": "Wingull", "nivel": 28, "tipo": "Agua", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Brock",
        "torneos_ganados": 5,
        "batallas_perdidas": 8,
        "batallas_ganadas": 42,
        "pokemons": [
            {"nombre": "Steelix", "nivel": 70, "tipo": "Acero", "subtipo": "Tierra"},
            {"nombre": "Croagunk", "nivel": 50, "tipo": "Veneno", "subtipo": "Lucha"},
            {"nombre": "Tyrantrum", "nivel": 68, "tipo": "Roca", "subtipo": "Dragón"}
        ]
    }
]


# a. Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(lista_entrenadores, nombre_entrenador):
    for e in lista_entrenadores:
        if e["nombre"].lower() == nombre_entrenador.lower():
            return len(e["pokemons"])
    return 0

print(f"a. Cantidad de Pokémons de Ash Ketchum: {cantidad_pokemons(entrenadores, 'Ash Ketchum')}")


# b. Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_3_torneos(lista_entrenadores):
    print("\nb. Entrenadores con más de 3 torneos ganados:")
    for e in lista_entrenadores:
        if e["torneos_ganados"] > 3:
            print(f" - {e['nombre']} ({e['torneos_ganados']} torneos)")

entrenadores_mas_de_3_torneos(entrenadores)


# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_del_campeon(lista_entrenadores):
    if not lista_entrenadores:
        return
    # Entrenador con mayor cantidad de torneos ganados
    campeon = max(lista_entrenadores, key=lambda e: e["torneos_ganados"])
    if campeon["pokemons"]:
        # Pokémon de mayor nivel del campeón
        pokemon_top = max(campeon["pokemons"], key=lambda p: p["nivel"])
        print(f"\nc. El entrenador con más torneos es '{campeon['nombre']}' ({campeon['torneos_ganados']} torneos).")
        print(f"   Su Pokémon de mayor nivel es {pokemon_top['nombre']} (Nivel {pokemon_top['nivel']}).")

pokemon_mayor_nivel_del_campeon(entrenadores)


# d. Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(lista_entrenadores, nombre_entrenador):
    print(f"\nd. Datos completos del entrenador '{nombre_entrenador}':")
    for e in lista_entrenadores:
        if e["nombre"].lower() == nombre_entrenador.lower():
            print(f"Nombre: {e['nombre']}")
            print(f"Torneos ganados: {e['torneos_ganados']}")
            print(f"Batallas ganadas: {e['batallas_ganadas']} | Perdedas: {e['batallas_perdidas']}")
            print("Pokémons:")
            for p in e["pokemons"]:
                print(f"  - {p['nombre']} | Nivel: {p['nivel']} | Tipo: {p['tipo']} | Subtipo: {p['subtipo']}")
            return
    print("Entrenador no encontrado.")

mostrar_datos_entrenador(entrenadores, "Ash Ketchum")


# e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def entrenadores_efectividad_mayor_79(lista_entrenadores):
    print("\ne. Entrenadores con porcentaje de batallas ganadas > 79%:")
    for e in lista_entrenadores:
        total_batallas = e["batallas_ganadas"] + e["batallas_perdidas"]
        if total_batallas > 0:
            porcentaje = (e["batallas_ganadas"] / total_batallas) * 100
            if porcentaje > 79:
                print(f" - {e['nombre']}: {porcentaje:.2f}% de efectividad")

entrenadores_efectividad_mayor_79(entrenadores)


# f. Entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def entrenadores_con_tipos_especificos(lista_entrenadores):
    print("\nf. Entrenadores con tipos (Fuego y Planta) o (Agua / Volador):")
    for e in lista_entrenadores:
        tiene_fuego = False
        tiene_planta = False
        tiene_agua_volador = False

        for p in e["pokemons"]:
            tipo = p["tipo"].capitalize() if p["tipo"] else ""
            subtipo = p["subtipo"].capitalize() if p["subtipo"] else ""

            if tipo == "Fuego":
                tiene_fuego = True
            if tipo == "Planta":
                tiene_planta = True
            if (tipo == "Agua" and subtipo == "Volador") or (tipo == "Volador" and subtipo == "Agua"):
                tiene_agua_volador = True

        if (tiene_fuego and tiene_planta) or tiene_agua_volador:
            print(f" - {e['nombre']}")

entrenadores_con_tipos_especificos(entrenadores)


# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(lista_entrenadores, nombre_entrenador):
    for e in lista_entrenadores:
        if e["nombre"].lower() == nombre_entrenador.lower():
            if not e["pokemons"]:
                return 0
            suma_niveles = sum(p["nivel"] for p in e["pokemons"])
            return suma_niveles / len(e["pokemons"])
    return 0

prom_ash = promedio_nivel_pokemons(entrenadores, "Ash Ketchum")
print(f"\ng. Promedio de nivel de Pokémons de Ash Ketchum: {prom_ash:.2f}")


# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(lista_entrenadores, nombre_pokemon):
    conteo = 0
    for e in lista_entrenadores:
        if any(p["nombre"].lower() == nombre_pokemon.lower() for p in e["pokemons"]):
            conteo += 1
    return conteo

cant = cantidad_entrenadores_con_pokemon(entrenadores, "Charizard")
print(f"\nh. Cantidad de entrenadores que tienen a Charizard: {cant}")


# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(lista_entrenadores):
    print("\ni. Entrenadores que tienen Pokémons repetidos:")
    for e in lista_entrenadores:
        nombres_pokemons = [p["nombre"].lower() for p in e["pokemons"]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            print(f" - {e['nombre']}")

entrenadores_con_pokemons_repetidos(entrenadores)


# j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos(lista_entrenadores, buscados):
    print(f"\nj. Entrenadores que poseen a {', '.join(buscados)}:")
    buscados_lower = [b.lower() for b in buscados]
    for e in lista_entrenadores:
        if any(p["nombre"].lower() in buscados_lower for p in e["pokemons"]):
            print(f" - {e['nombre']}")

entrenadores_con_pokemons_especificos(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])


# k. Determinar si un entrenador "X" tiene al Pokémon "Y", mostrando datos de ambos
def consultar_entrenador_y_pokemon(lista_entrenadores, nombre_entrenador, nombre_pokemon):
    print(f"\nk. Búsqueda: Entrenador '{nombre_entrenador}' y Pokémon '{nombre_pokemon}':")
    for e in lista_entrenadores:
        if e["nombre"].lower() == nombre_entrenador.lower():
            for p in e["pokemons"]:
                if p["nombre"].lower() == nombre_pokemon.lower():
                    print(f"-> ¡ENCONTRADO!")
                    print(f"   Entrenador: {e['nombre']} | Torneos: {e['torneos_ganados']} | Batallas G/P: {e['batallas_ganadas']}/{e['batallas_perdidas']}")
                    print(f"   Pokémon: {p['nombre']} | Nivel: {p['nivel']} | Tipo: {p['tipo']} / {p['subtipo']}")
                    return True
            print(f"-> El entrenador {e['nombre']} NO posee a {nombre_pokemon}.")
            return False
    print(f"-> El entrenador {nombre_entrenador} NO existe en la lista.")
    return False

# Ejemplo de prueba para el inciso k
consultar_entrenador_y_pokemon(entrenadores, "Misty", "Wingull")