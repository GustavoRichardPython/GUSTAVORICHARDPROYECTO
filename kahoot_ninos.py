import pygame
from pygame_widgets import Button
import time

# Define algunas constantes para el juego
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Preguntas y respuestas para el cuestionario
preguntas = [
    {
        "pregunta": "¿Cuál es el animal que dice 'miau'?",
        "respuestas": ["Perro", "Gato", "Vaca", "Pájaro"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuántos lados tiene un triángulo?",
        "respuestas": ["3", "4", "5", "6"],
        "respuesta_correcta": 0
    },
    # Puedes agregar más preguntas aquí
]

# Función para mostrar el cuestionario en pantalla
def mostrar_cuestionario(ventana, pregunta_actual, botones_respuestas):
    ventana.fill(WHITE)
    font = pygame.font.SysFont(None, 40)

    # Muestra la pregunta
    pregunta_texto = font.render(pregunta_actual["pregunta"], True, BLACK)
    ventana.blit(pregunta_texto, (50, 50))

    # Muestra los botones de las opciones de respuesta
    for i, boton in enumerate(botones_respuestas):
        boton.draw()

    pygame.display.flip()

# Función para mostrar el resultado final
def mostrar_resultado(ventana, puntos_obtenidos):
    ventana.fill(WHITE)
    font = pygame.font.SysFont(None, 60)

    mensaje = f"¡Tu puntuación final es: {puntos_obtenidos}!"
    resultado_texto = font.render(mensaje, True, BLACK)
    ventana.blit(resultado_texto, (WIDTH // 2 - resultado_texto.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    time.sleep(3)

# Función principal
def main():
    pygame.init()
    ventana = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cuestionario Kahoot para Niños")

    puntos_obtenidos = 0

    # Crea los botones de las opciones de respuesta
    botones_respuestas = []
    for i in range(4):
        boton = Button(
            ventana, 150, 100 + i * 100, 500, 80, 
            text="", fontSize=30, inactiveColour=BLACK, 
            pressedColour=GREEN, radius=20,
            onClick=lambda respuesta=i: evaluar_respuesta(respuesta)
        )
        botones_respuestas.append(boton)

    # Función para evaluar la respuesta seleccionada
    def evaluar_respuesta(respuesta):
        nonlocal puntos_obtenidos
        if respuesta == preguntas[pregunta_actual]["respuesta_correcta"]:
            puntos_obtenidos += 1
            botones_respuestas[respuesta].config(colour=GREEN)
        else:
            botones_respuestas[respuesta].config(colour=RED)

        for i, boton in enumerate(botones_respuestas):
            boton.hide()
        
        pygame.display.flip()
        time.sleep(1)
        siguiente_pregunta()

    # Función para pasar a la siguiente pregunta
    def siguiente_pregunta():
        nonlocal pregunta_actual
        pregunta_actual += 1
        if pregunta_actual < len(preguntas):
            mostrar_cuestionario(ventana, preguntas[pregunta_actual], botones_respuestas)
        else:
            mostrar_resultado(ventana, puntos_obtenidos)
            pygame.quit()
            exit()

    pregunta_actual = 0
    mostrar_cuestionario(ventana, preguntas[pregunta_actual], botones_respuestas)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()

if __name__ == "__main__":
    main()
