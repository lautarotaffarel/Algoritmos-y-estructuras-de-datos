import json

def generar_json_1024():
    tipos_posibles = [
        "Planta", "Fuego", "Agua", "Eléctrico", "Fantasma", 
        "Acero", "Roca", "Dragón", "Normal", "Veneno", "Psíquico", "Lucha"
    ]
    debilidades_posibles = [
        "Agua", "Fuego", "Planta", "Eléctrico", 
        "Roca", "Dragón", "Tierra", "Hielo", "Psíquico"
    ]
    
    lista_1024 = []
    
    # Nombres representativos para algunas posiciones destacadas
    nombres_destacados = {
        1: ("Bulbasaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Psíquico", "Volador"]),
        6: ("Charizard", ["Fuego", "Volador"], ["Agua", "Eléctrico", "Roca"]),
        25: ("Pikachu", ["Eléctrico"], ["Tierra"]),
        94: ("Gengar", ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"]),
        135: ("Jolteon", ["Eléctrico"], ["Tierra"]),
        448: ("Lucario", ["Lucha", "Acero"], ["Fuego", "Lucha", "Tierra"]),
        697: ("Tyrantrum", ["Roca", "Dragón"], ["Acero", "Dragón", "Hada", "Hielo", "Lucha", "Tierra"]),
        745: ("Lycanroc", ["Roca"], ["Agua", "Lucha", "Planta", "Tierra", "Acero"])
    }

    for i in range(1, 1025):
        if i in nombres_destacados:
            nombre, tipos, debilidades = nombres_destacados[i]
        else:
            nombre = f"Pokemon-{i}"
            tipos = [tipos_posibles[i % len(tipos_posibles)]]
            if i % 3 == 0:
                tipos.append(tipos_posibles[(i + 2) % len(tipos_posibles)])
                
            debilidades = [debilidades_posibles[i % len(debilidades_posibles)]]
            if i % 2 == 0:
                debilidades.append(debilidades_posibles[(i + 4) % len(debilidades_posibles)])

        mega = (i % 15 == 0)
        gigamax = (i % 25 == 0)

        pokemon_dict = {
            "numero": i,
            "nombre": nombre,
            "tipos": tipos,
            "debilidades": debilidades,
            "mega": mega,
            "gigamax": gigamax
        }
        lista_1024.append(pokemon_dict)

    with open('pokemons.json', 'w', encoding='utf-8') as f:
        json.dump(lista_1024, f, ensure_ascii=False, indent=4)

    print(f"¡Archivo 'pokemons.json' generado exitosamente con {len(lista_1024)} Pokémon!")

if __name__ == '__main__':
    generar_json_1024()