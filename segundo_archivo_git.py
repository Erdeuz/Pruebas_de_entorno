import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
COLOR_FONDO = (50, 50, 100)
COLOR_JUGADOR = (200, 50, 50)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Simple")

# Configuración del jugador
jugador_tamano = 50
jugador_x = ANCHO // 2 - jugador_tamano // 2
jugador_y = ALTO - jugador_tamano - 10
velocidad = 5

# Bucle principal del juego
clock = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Controles del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_tamano:
        jugador_x += velocidad

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, (jugador_x,
                     jugador_y, jugador_tamano, jugador_tamano))

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
