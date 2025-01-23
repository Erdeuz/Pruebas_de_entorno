import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 900
ALTO = 600
COLOR_FONDO = (0, 0, 0)
COLOR_JUGADOR = (50, 150, 50)
COLOR_ENEMIGO = (200, 50, 50)
COLOR_META = (50, 50, 200)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Sigilo")

# Configuración del jugador
jugador_tamano = 20
jugador_x = 50
jugador_y = ALTO // 2
jugador_velocidad = 5
nombre_jugador = "Edu"

# Configuración de los enemigos
enemigos = [
    pygame.Rect(200, 50, 20, 20),
    pygame.Rect(300, 150, 20, 20),
    pygame.Rect(400, 250, 20, 20),
    pygame.Rect(500, 350, 20, 20),
    pygame.Rect(600, 450, 20, 20),
    pygame.Rect(700, 100, 20, 20),
    pygame.Rect(750, 300, 20, 20)
]
enemigo_velocidades = [5, 6, 5, 7, 6, 8, 12]

# Configuración de la meta
meta = pygame.Rect(820, ALTO // 2 - 10, 20, 20)
nombre_meta = "Categoria"
fuente = pygame.font.Font(None, 36)

# Función de festejo


def festejo():
    for _ in range(60):  # Duración del festejo (60 cuadros)
        pantalla.fill((0, 0, 0))  # Fondo negro
        texto_festejo = fuente.render(
            "¡Felicidades, Ale!", True, (255, 255, 0))
        pantalla.blit(texto_festejo, (ANCHO // 2 - texto_festejo.get_width() //
                      2, ALTO // 2 - texto_festejo.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(100)


# Bucle principal del juego
clock = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Controles del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador_y > 0:
        jugador_y -= jugador_velocidad
    if teclas[pygame.K_DOWN] and jugador_y < ALTO - jugador_tamano:
        jugador_y += jugador_velocidad
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_tamano:
        jugador_x += jugador_velocidad

    # Movimiento de los enemigos
    for i, enemigo in enumerate(enemigos):
        enemigo.y += enemigo_velocidades[i]
        if enemigo.y <= 0 or enemigo.y >= ALTO - 20:
            enemigo_velocidades[i] *= -1

    # Colisiones con los enemigos
    jugador_rect = pygame.Rect(
        jugador_x, jugador_y, jugador_tamano, jugador_tamano)
    for enemigo in enemigos:
        if jugador_rect.colliderect(enemigo):
            print("¡Te han descubierto!")
            ejecutando = False

    # Colisión con la meta
    if jugador_rect.colliderect(meta):
        festejo()
        ejecutando = False

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador_rect)
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, COLOR_ENEMIGO, enemigo)
    pygame.draw.rect(pantalla, COLOR_META, meta)

    # Dibujar el nombre del jugador y la meta
    texto_meta = fuente.render(nombre_meta, True, (255, 255, 255))
    pantalla.blit(texto_meta, (meta.x - texto_meta.get_width() //
                  2 + meta.width // 2, meta.y - 30))

    texto_jugador = fuente.render(nombre_jugador, True, (255, 255, 255))
    pantalla.blit(texto_jugador, (jugador_x - texto_jugador.get_width() //
                  2 + jugador_tamano // 2, jugador_y - 30))

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
