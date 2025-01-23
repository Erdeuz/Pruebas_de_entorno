import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
COLOR_FONDO = (135, 206, 235)  # Azul cielo
COLOR_SUELO = (139, 69, 19)  # Café tierra
COLOR_JUGADOR = (255, 0, 0)  # Rojo
COLOR_META = (255, 215, 0)  # Dorado
COLOR_OBSTACULO = (0, 0, 255)  # Azul

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Tipo Mario Bros")

# Configuración del jugador
jugador_ancho = 40
jugador_alto = 60
jugador_x = 50
jugador_y = ALTO - 100
jugador_velocidad = 5
jugador_salto = 15
velocidad_caida = 5
salto_activo = False

# Configuración de la meta
meta_ancho = 40
meta_alto = 60
meta_x = ANCHO - 100
meta_y = ALTO - 100

# Configuración del suelo
suelo_altura = 40

# Configuración de los obstáculos móviles
obstaculos = [
    pygame.Rect(200, ALTO - suelo_altura - 20, 60, 20),
    pygame.Rect(400, ALTO - suelo_altura - 100, 60, 20),
    pygame.Rect(600, ALTO - suelo_altura - 150, 60, 20)
]
velocidades_obstaculos = [3, -4, 2]

# Fuentes
fuente = pygame.font.Font(None, 36)

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
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_ancho:
        jugador_x += jugador_velocidad
    if teclas[pygame.K_SPACE] and not salto_activo:
        salto_activo = True
        velocidad_salto = jugador_salto

    # Movimiento del salto
    if salto_activo:
        jugador_y -= velocidad_salto
        velocidad_salto -= 1
        if velocidad_salto < -jugador_salto:
            salto_activo = False

    # Gravedad
    if jugador_y < ALTO - suelo_altura - jugador_alto:
        jugador_y += velocidad_caida
    else:
        jugador_y = ALTO - suelo_altura - jugador_alto

    # Movimiento de los obstáculos
    for i, obstaculo in enumerate(obstaculos):
        obstaculo.x += velocidades_obstaculos[i]
        if obstaculo.x <= 0 or obstaculo.x >= ANCHO - obstaculo.width:
            velocidades_obstaculos[i] *= -1

    # Colisión con los obstáculos
    jugador_rect = pygame.Rect(
        jugador_x, jugador_y, jugador_ancho, jugador_alto)
    for obstaculo in obstaculos:
        if jugador_rect.colliderect(obstaculo):
            pantalla.fill(COLOR_FONDO)
            texto_derrota = fuente.render("¡Has perdido!", True, (255, 0, 0))
            pantalla.blit(texto_derrota, (ANCHO // 2 - texto_derrota.get_width() //
                          2, ALTO // 2 - texto_derrota.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            ejecutando = False

    # Colisión con la meta
    meta_rect = pygame.Rect(meta_x, meta_y, meta_ancho, meta_alto)
    if jugador_rect.colliderect(meta_rect):
        pantalla.fill(COLOR_FONDO)
        texto_victoria = fuente.render("¡Has ganado!", True, (0, 255, 0))
        pantalla.blit(texto_victoria, (ANCHO // 2 - texto_victoria.get_width() //
                      2, ALTO // 2 - texto_victoria.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        ejecutando = False

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)

    # Dibujar el suelo
    pygame.draw.rect(pantalla, COLOR_SUELO, (0, ALTO -
                     suelo_altura, ANCHO, suelo_altura))

    # Dibujar el jugador
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador_rect)

    # Dibujar la meta
    pygame.draw.rect(pantalla, COLOR_META, meta_rect)

    # Dibujar los obstáculos
    for obstaculo in obstaculos:
        pygame.draw.rect(pantalla, COLOR_OBSTACULO, obstaculo)

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
