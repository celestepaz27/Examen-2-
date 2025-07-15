
# ejercicio2.py

# pip install pandas  # Si usaras pandas para leer Excel

import re

class ProcesadorTexto:
    def __init__(self, registros):
        self.registros = registros

    def eliminar_espacios_y_detectar_animal(self):
        for texto in self.registros:
            limpio = texto.strip()
            if "gato" in limpio.lower():
                return limpio
        return "Animal no encontrado"

    def detectar_lenguaje_programacion(self):
        for texto in self.registros:
            if texto.strip() == "python":
                return texto.upper()
        return "Lenguaje no encontrado"

    def verificar_numero(self):
        for texto in self.registros:
            if texto.strip().replace('.', '', 1).isdigit():
                return texto.strip()
        return "No es número válido"

    def extraer_frase_agua(self):
        for texto in self.registros:
            if "agua" in texto.lower():
                palabras = texto.strip().split()
                visibles = [p for p in palabras if "agua" in p.lower()]
                return " ".join(visibles)
        return "Frase no encontrada"

    def validar_identificador_alfabetico(self):
        for texto in self.registros:
            if texto.strip().isalpha():
                return texto.strip()
        return "No hay identificador alfabético puro"

    def normalizar_lenguajes_similares(self):
        resultados = []
        for texto in self.registros:
            if texto.lower().startswith("java"):
                resultados.append("java")
        return resultados

    def transformar_frase_pacifica(self):
        for texto in self.registros:
            if "paz" in texto.lower():
                return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(texto.strip())])
        return "No se encontró frase"

    def detectar_division_cadenas(self):
        for i, texto in enumerate(self.registros):
            if "split" in texto:
                return f"Mención empieza en posición {i}"
        return "No se menciona"

    def limpiar_residuos(self):
        resultados = []
        for texto in self.registros:
            limpio = texto.strip().rstrip("#$%&/()")
            resultados.append(limpio)
        return resultados

    def recuperar_titulo_oculto(self):
        for texto in self.registros:
            if texto.strip():
                return texto.strip().capitalize()
        return "No se encontró título"

# Ejemplo de registros de prueba
registros_prueba = [
    "   gato   ",
    "python",
    " 123.45 ",
    "La corriente de agua visible es fuerte",
    "identificador",
    "JavaScript",
    "vivamos en paz",
    "Se puede usar split para dividir cadenas",
    "Frase útil con residuos%%%###",
    "     el gran título escondido     ",
]

# Uso
procesador = ProcesadorTexto(registros_prueba)

print("Animal:", procesador.eliminar_espacios_y_detectar_animal())
print("Lenguaje:", procesador.detectar_lenguaje_programacion())
print("Número:", procesador.verificar_numero())
print("Frase agua:", procesador.extraer_frase_agua())
print("Identificador:", procesador.validar_identificador_alfabetico())
print("Lenguajes normalizados:", procesador.normalizar_lenguajes_similares())
print("Frase opuesta:", procesador.transformar_frase_pacifica())
print("Split en:", procesador.detectar_division_cadenas())
print("Sin residuos:", procesador.limpiar_residuos())
print("Título oculto:", procesador.recuperar_titulo_oculto())
