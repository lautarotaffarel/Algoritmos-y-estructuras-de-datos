# Lista de superhéroes de ejemplo con los datos requeridos
superheroes = [
    {
        "nombre": "Linterna Verde",
        "anio": 1940,
        "casa": "DC",
        "biografia": "Obtiene sus poderes de un anillo de poder y viste un traje verde."
    },
    {
        "nombre": "Wolverine",
        "anio": 1974,
        "casa": "Marvel",
        "biografia": "Mutante con garras de adamantium y factor de curación acelerado."
    },
    {
        "nombre": "Dr. Strange",
        "anio": 1963,
        "casa": "DC",  # Error intencional para resolver el inciso c
        "biografia": "Hechicero supremo que protege la Tierra contra amenazas místicas."
    },
    {
        "nombre": "Iron Man",
        "anio": 1963,
        "casa": "Marvel",
        "biografia": "Un multimillonario que utiliza una avanzada armadura de alta tecnología."
    },
    {
        "nombre": "Capitana Marvel",
        "anio": 1968,
        "casa": "Marvel",
        "biografia": "Posee fuerza sobrehumana y vuelo tras fusionar su ADN."
    },
    {
        "nombre": "Mujer Maravilla",
        "anio": 1941,
        "casa": "DC",
        "biografia": "Princesa amazona con habilidades divinas y guerrera experta."
    },
    {
        "nombre": "Flash",
        "anio": 1940,
        "casa": "DC",
        "biografia": "Velocista que se conecta a la Fuerza de la Velocidad mediante un traje especial."
    },
    {
        "nombre": "Star-Lord",
        "anio": 1976,
        "casa": "Marvel",
        "biografia": "Líder de los Guardianes de la Galaxia que viaja por el cosmos."
    },
    {
        "nombre": "Batman",
        "anio": 1939,
        "casa": "DC",
        "biografia": "Justiciero de Gotham que combate el crimen usando un traje blindado."
    }
]

# a. Eliminar el nodo que contiene la información de Linterna Verde
def eliminar_superheroe(lista, nombre):
    for i, hero in enumerate(lista):
        if hero["nombre"].lower() == nombre.lower():
            del lista[i]
            print(f"a. Se eliminó a {nombre} de la lista.")
            return
    print(f"a. No se encontró a {nombre}.")

eliminar_superheroe(superheroes, "Linterna Verde")


# b. Mostrar el año de aparición de Wolverine
def mostrar_anio_aparicion(lista, nombre):
    for hero in lista:
        if hero["nombre"].lower() == nombre.lower():
            print(f"b. El año de aparición de {nombre} es: {hero['anio']}")
            return
    print(f"b. No se encontró a {nombre}.")

mostrar_anio_aparicion(superheroes, "Wolverine")


# c. Cambiar la casa de Dr. Strange a Marvel
def cambiar_casa(lista, nombre, nueva_casa):
    for hero in lista:
        if hero["nombre"].lower() == nombre.lower():
            hero["casa"] = nueva_casa
            print(f"c. Se cambió la casa de {nombre} a '{nueva_casa}'.")
            return
    print(f"c. No se encontró a {nombre}.")

cambiar_casa(superheroes, "Dr. Strange", "Marvel")


# d. Mostrar el nombre de aquellos superhéroes que en su biografía menciona "traje" o "armadura"
def buscar_por_palabras_clave(lista, palabras):
    print("\nd. Superhéroes con 'traje' o 'armadura' en su biografía:")
    for hero in lista:
        bio_lower = hero["biografia"].lower()
        if any(palabra in bio_lower for palabra in palabras):
            print(f" - {hero['nombre']}")

buscar_por_palabras_clave(superheroes, ["traje", "armadura"])


# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def mostrar_anteriores_a(lista, anio_limite):
    print(f"\ne. Superhéroes cuya fecha de aparición es anterior a {anio_limite}:")
    for hero in lista:
        if hero["anio"] < anio_limite:
            print(f" - Nombre: {hero['nombre']} | Casa: {hero['casa']} (Año: {hero['anio']})")

mostrar_anteriores_a(superheroes, 1963)


# f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
def mostrar_casa_heroes(lista, nombres):
    print("\nf. Casa de cómic de personajes específicos:")
    for hero in lista:
        if hero["nombre"] in nombres:
            print(f" - {hero['nombre']}: {hero['casa']}")

mostrar_casa_heroes(superheroes, ["Capitana Marvel", "Mujer Maravilla"])


# g. Mostrar toda la información de Flash y Star-Lord
def mostrar_info_completa(lista, nombres):
    print("\ng. Información completa de Flash y Star-Lord:")
    for hero in lista:
        if hero["nombre"] in nombres:
            print(f" - Nombre: {hero['nombre']}")
            print(f"   Año: {hero['anio']}")
            print(f"   Casa: {hero['casa']}")
            print(f"   Biografía: {hero['biografia']}")

mostrar_info_completa(superheroes, ["Flash", "Star-Lord"])


# h. Listar los superhéroes que comienzan con la letra B, M y S
def listar_por_iniciales(lista, letras):
    print(f"\nh. Superhéroes que comienzan con las letras {', '.join(letras)}:")
    for hero in lista:
        if hero["nombre"][0].upper() in letras:
            print(f" - {hero['nombre']}")

listar_por_iniciales(superheroes, ["B", "M", "S"])


# i. Determinar cuántos superhéroes hay de cada casa de cómic
def contar_por_casa(lista):
    conteo = {}
    for hero in lista:
        casa = hero["casa"]
        conteo[casa] = conteo.get(casa, 0) + 1
    
    print("\ni. Cantidad de superhéroes por casa de cómic:")
    for casa, cantidad in conteo.items():
        print(f" - {casa}: {cantidad}")

contar_por_casa(superheroes)