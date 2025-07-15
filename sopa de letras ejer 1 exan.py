def buscar_palabras(sopa, palabras):
    filas = len(sopa)
    columnas = len(sopa[0])
    resultados = []

    direcciones = [
        (0, 1),   # derecha
        (0, -1),  # izquierda
        (1, 0),   # abajo
        (-1, 0),  # arriba
        (1, 1),   # diagonal abajo derecha
        (1, -1),  # diagonal abajo izquierda
        (-1, 1),  # diagonal arriba derecha
        (-1, -1), # diagonal arriba izquierda
    ]

    for palabra in palabras:
        encontrada = False
        for f in range(filas):
            for c in range(columnas):
                for df, dc in direcciones:
                    x, y = f, c
                    match = True
                    for letra in palabra:
                        if 0 <= x < filas and 0 <= y < columnas:
                            if sopa[x][y].lower() != letra.lower():
                                match = False
                                break
                        else:
                            match = False
                            break
                        x += df
                        y += dc
                    if match:
                        resultados.append((palabra, f + 1, c + 1))  # formato FIL_COL
                        encontrada = True
                        break
                if encontrada:
                    break
            if encontrada:
                break
    return resultados

# Sopa copiada de la imagen (construida manualmente)
sopa = [
    list("fjfbxmoxonu"),
    list("jhusnlxhegu"),
    list("bbwlngxoryp"),
    list("xixwencqajr"),
    list("roenpznraoj"),
    list("oeccyuetlaq"),
    list("rceytaosjze"),
    list("lrcetuosvff"),
]

# Palabras a buscar
palabras = ["luz", "reto", "clase", "radar", "python"]

# Buscar
resultados = buscar_palabras(sopa, palabras)

# Mostrar resultados
for palabra, fila, columna in resultados:
    print(f"{palabra.upper()} encontrada en: {fila}_{columna}")

