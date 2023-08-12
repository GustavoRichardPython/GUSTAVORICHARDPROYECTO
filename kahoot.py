import pygame
import time

# Define algunas constantes para el juego
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Preguntas y respuestas para el cuestionario
preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuestas": ["Londres", "París", "Madrid", "Berlín"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "respuestas": ["Amazonas", "Nilo", "Yangtsé", "Misisipi"],
        "respuesta_correcta": 0
    },
    # Puedes agregar más preguntas aquí
]

# Función para mostrar el cuestionario en pantalla
def mostrar_cuestionario(ventana, pregunta_actual):
    ventana.fill(WHITE)
    font = pygame.font.SysFont(None, 40)

    # Muestra la pregunta
    pregunta_texto = font.render(pregunta_actual["pregunta"], True, BLACK)
    ventana.blit(pregunta_texto, (50, 50))

    # Muestra las opciones de respuesta
    for i, respuesta in enumerate(pregunta_actual["respuestas"]):
        respuesta_texto = font.render(f"{i + 1}. {respuesta}", True, BLACK)
        ventana.blit(respuesta_texto, (50, 100 + i * 50))

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
    pygame.display.set_caption("Cuestionario Kahoot")

    puntos_obtenidos = 0

    for pregunta in preguntas:
        mostrar_cuestionario(ventana, pregunta)

        esperando_respuesta = True
        while esperando_respuesta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_4:
                        respuesta_elegida = event.key - pygame.K_1
                        if respuesta_elegida == pregunta["respuesta_correcta"]:
                            puntos_obtenidos += 1
                        esperando_respuesta = False

    mostrar_resultado(ventana, puntos_obtenidos)
    pygame.quit()

if __name__ == "__main__":
    main()