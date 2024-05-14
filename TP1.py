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
