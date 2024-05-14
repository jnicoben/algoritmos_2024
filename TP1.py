#! ejercicio 5

def roman_to_decimal(roman):
    if not roman:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman) > 1 and roman_values[roman[0]] < roman_values[roman[1]]:
        return roman_values[roman[1]] - roman_values[roman[0]] + roman_to_decimal(roman[2:])
    else:
        return roman_values[roman[0]] + roman_to_decimal(roman[1:])

# Ejemplo de uso:
numero_romano = "I"
print(f"{numero_romano} en decimal es: {roman_to_decimal(numero_romano)}")



#! ejercicio 22
def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        # No quedan más objetos en la mochila
        return -1
    
    objeto_actual = mochila[indice]
    if objeto_actual == "sable de luz":
        # Encontramos un sable de luz
        return indice
    else:
        # Seguimos buscando
        return usar_la_fuerza(mochila, indice + 1)

# Ejemplo de uso
mochila_ejemplo = ["comida", "agua", "sable de luz", "mapa"]
resultado = usar_la_fuerza(mochila_ejemplo)
if resultado != -1:
    print(f"Encontramos un sable de luz después de sacar {resultado} objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")
