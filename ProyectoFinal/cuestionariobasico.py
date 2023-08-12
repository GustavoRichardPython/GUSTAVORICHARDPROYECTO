class Pregunta:
    def __init__(self, texto, opciones, opcion_correcta):
        self.texto = texto
        self.opciones = opciones
        self.opcion_correcta = opcion_correcta

    def correcta (self, opcion):
        return opcion == self.opcion_correcta


class Prueba:
    def __init__(self):
        self.preguntas = []

    def add_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def run(self):
        puntaje = 0
        for idx, pregunta in enumerate(self.preguntas, start=1):
            print(f"Preguntas {idx}: {pregunta.texto}")
            for i, opcion in enumerate(pregunta.opciones, start=1):
                print(f"{i}. {opcion}")

            usuario_opcion = int(input("Elige la respuesta (ingresa un numero): "))
            if pregunta.correcta(usuario_opcion):
                print("Correcto!\n")
                puntaje += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta.opcion_correcta}\n")

        print(f"Terminaste! Tu puntaje es: {puntaje}/{len(self.preguntas)}")


# Crear preguntas y respuestas
Pregunta1 = Pregunta("En la BioConstruccion los materiales que utilizamos principalmente son?", ["Madera-Tierra", "Plastico", "Hierro", "Cemento"], 1)
Pregunta2 = Pregunta("Cual es el concepto que busca la Permacultura?", ["Eficiencia Energetica", "Ahorro", "Lujo", "Estetica"], 1)
Pregunta3 = Pregunta("Que funcion cumple el elemento paja en el adobe?", ["Reforzar", "Aislante Termico", "Tejer", "Unir"], 2)

# Crear el cuestionario y agregar las preguntas
prueba = Prueba()
prueba.add_pregunta(Pregunta1)
prueba.add_pregunta(Pregunta2)
prueba.add_pregunta(Pregunta3)

# Ejecutar el cuestionario
prueba.run()