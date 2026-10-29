def analizar_token(cadena):
    cadena = cadena.strip()

    if not cadena:
        return "Cadena vacía"

    estado = 0
    i = 0

    operadores = {'+', '-', '*', '/', '=', '<', '>', '%'}

    # Palabras reservadas del lenguaje
    palabras_reservadas = {
        'if', 'else', 'elif', 'for', 'while',
        'def', 'return', 'class', 'import',
        'from', 'in', 'and', 'or', 'not',
        'True', 'False', 'None', 'print'
    }

    while i < len(cadena):
        c = cadena[i]

        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1  # Identificador o palabra reservada
            elif c.isdigit():
                estado = 2  # Número entero
            elif c in operadores:
                estado = 4  # Operador
            else:
                return "No válido / Desconocido"

        elif estado == 1:
            if not (c.isalnum() or c == '_'):
                return "Identificador no válido"

        elif estado == 2:
            if c == '.':
                estado = 3  # Número real
            elif not c.isdigit():
                return "Número no válido"

        elif estado == 3:
            if not c.isdigit():
                return "Número real no válido"

        elif estado == 4:
            return "Operador no válido (demasiados caracteres)"

        i += 1

    # Clasificación final
    if estado == 1:
        if cadena in palabras_reservadas:
            return "Palabra reservada"
        return "Identificador válido"

    elif estado == 2:
        return "Número entero válido"

    elif estado == 3:
        return "Número real válido"

    elif estado == 4:
        return "Operador válido"

    return "Cadena no válida"


# --- Pruebas ---
entradas = [
    "variable1",
    "125",
    "45.67",
    "+",
    "_contador",
    "99num",
    "++",
    "if",
    "while",
    "return",
    "3.1416",
    "0.25",
    "12.5.6"
]

for e in entradas:
    print(f"'{e}' -> {analizar_token(e)}")