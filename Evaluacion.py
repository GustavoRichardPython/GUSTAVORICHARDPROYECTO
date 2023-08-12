class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def mostrar_pregunta(self):
        print(self.enunciado)
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}. {opcion}")
        respuesta_usuario = int(input("Ingresa el número de la opción correcta: "))
        return respuesta_usuario == self.respuesta_correcta


def evaluar_cuestionario(cuestionario):
    puntaje = 0
    for pregunta in cuestionario:
        if pregunta.mostrar_pregunta():
            puntaje += 1
        print()  # Agregar una línea en blanco entre preguntas
    return puntaje


if __name__ == "__main__":
    # Crea tus preguntas aquí (agrega más si lo deseas)
    preguntas = [
        Pregunta("¿Cuál es la capital de Francia?", ["París", "Londres", "Berlín"], 1),
        Pregunta("¿En qué año se lanzó el primer iPhone?", ["2005", "2007", "2010"], 2),
        Pregunta("¿Cuál es el río más largo del mundo?", ["Nilo", "Amazonas", "Mississippi"], 2),
        Pregunta("¿Quién escribió 'Romeo y Julieta'?", ["William Shakespeare", "Jane Austen", "Friedrich Nietzsche"], 1),
    ]

    # Evaluar el cuestionario y mostrar el resultado
    puntaje_obtenido = evaluar_cuestionario(preguntas)
    total_preguntas = len(preguntas)
    print(f"\nObtuviste {puntaje_obtenido} de {total_preguntas} preguntas correctamente.")
    porcentaje_acierto = (puntaje_obtenido / total_preguntas) * 100
    print(f"Porcentaje de acierto: {porcentaje_acierto:.2f}%")