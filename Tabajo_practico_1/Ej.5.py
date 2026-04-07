def valor(c):
    valores = {
        'I': 1,
        'V': 5, 
        'X': 10,
        'L': 50, 
        'C': 100,
        'D': 500, 
        'M': 1000
    }
    return valores[c]


def cambio_a_decimal(romano):
    # Caso base
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valor(romano[0])

    # Comparación de los dos primeros
    if valor(romano[0]) < valor(romano[1]):
        return -valor(romano[0]) + cambio_a_decimal(romano[1:])
    else:
        return valor(romano[0]) + cambio_a_decimal(romano[1:])
    

print(cambio_a_decimal("XV"))
print(cambio_a_decimal("IM"))
print(cambio_a_decimal("MMXXVI"))

