def usar_la_fuerza(mochila, posicion = 0, contador = 0):
    if posicion >= len(mochila):
        return False, contador

    contador += 1


    if mochila[posicion] == "sable de luz":
        return True, contador

   
    return usar_la_fuerza(mochila, posicion + 1, contador)


#Se genera un vector con los elementos

mochila= ["comida", "ropa", "sable de luz", "mapa"]

encontrado,contador = usar_la_fuerza(mochila)

if encontrado:
    print("sable encontrado, cantidad de objetos retirados",contador)
else:
    print("El sable no ha sido encontrado, cantidad de objetos revisados",contador)