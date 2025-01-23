import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 800
COLOR_FONDO = (0, 0, 0)  # Negro
COLOR_JUGADOR = (255, 255, 0)  # Amarillo
COLOR_ENEMIGO = (255, 0, 0)  # Rojo
COLOR_META = (0, 255, 0)  # Verde
COLOR_PARED = (0, 0, 255)  # Azul

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Tipo Pacman con Laberinto")

# Configuración del jugador
jugador_ancho = 20
jugador_alto = 20
jugador_x = ANCHO // 2 - jugador_ancho // 2
jugador_y = ALTO // 2 - jugador_alto // 2
jugador_velocidad = 5

# Configuración de la meta
meta_ancho = 20
meta_alto = 20
meta_x = random.randint(0, ANCHO - meta_ancho)
meta_y = random.randint(0, ALTO - meta_alto)

# Configuración de los enemigos
numero_enemigos = 7  # 50% más de enemigos
enemigos = []
velocidades_enemigos = []
for _ in range(numero_enemigos):
    enemigo_x = random.randint(0, ANCHO - 20)
    enemigo_y = random.randint(0, ALTO - 20)
    # Tamaño reducido
    enemigos.append(pygame.Rect(enemigo_x, enemigo_y, 20, 20))
    velocidades_enemigos.append(
        (random.choice([-3, 3]), random.choice([-3, 3])))

# Configuración de las paredes del laberinto
paredes = [
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 200, 20, 300),
    pygame.Rect(200, 500, 400, 20),
    pygame.Rect(700, 200, 20, 300),
    pygame.Rect(300, 300, 200, 20)
]

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
    nuevo_jugador_x = jugador_x
    nuevo_jugador_y = jugador_y
    if teclas[pygame.K_LEFT]:
        nuevo_jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT]:
        nuevo_jugador_x += jugador_velocidad
    if teclas[pygame.K_UP]:
        nuevo_jugador_y -= jugador_velocidad
    if teclas[pygame.K_DOWN]:
        nuevo_jugador_y += jugador_velocidad

    jugador_rect = pygame.Rect(
        nuevo_jugador_x, nuevo_jugador_y, jugador_ancho, jugador_alto)
    colision_con_pared = False
    for pared in paredes:
        if jugador_rect.colliderect(pared):
            colision_con_pared = True
            break

    if not colision_con_pared:
        jugador_x = nuevo_jugador_x
        jugador_y = nuevo_jugador_y

    # Movimiento de los enemigos
    for i, enemigo in enumerate(enemigos):
        dx, dy = velocidades_enemigos[i]
        enemigo.x += dx
        enemigo.y += dy

        # Rebotar en los bordes
        if enemigo.x <= 0 or enemigo.x >= ANCHO - enemigo.width:
            velocidades_enemigos[i] = (-dx, dy)
        if enemigo.y <= 0 or enemigo.y >= ALTO - enemigo.height:
            velocidades_enemigos[i] = (dx, -dy)

        # Colisión con paredes
        if any(enemigo.colliderect(pared) for pared in paredes):
            velocidades_enemigos[i] = (-dx, -dy)

    # Colisión con los enemigos
    jugador_rect = pygame.Rect(
        jugador_x, jugador_y, jugador_ancho, jugador_alto)
    for enemigo in enemigos:
        if jugador_rect.colliderect(enemigo):
            pantalla.fill(COLOR_FONDO)
            texto_derrota = fuente.render(
                "¡Has perdido!", True, (255, 255, 255))
            pantalla.blit(texto_derrota, (ANCHO // 2 - texto_derrota.get_width() //
                          2, ALTO // 2 - texto_derrota.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            ejecutando = False

    # Colisión con la meta
    meta_rect = pygame.Rect(meta_x, meta_y, meta_ancho, meta_alto)
    if jugador_rect.colliderect(meta_rect):
        pantalla.fill(COLOR_FONDO)
        texto_victoria = fuente.render("¡Has ganado!", True, (255, 255, 255))
        pantalla.blit(texto_victoria, (ANCHO // 2 - texto_victoria.get_width() //
                      2, ALTO // 2 - texto_victoria.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        ejecutando = False

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)

    # Dibujar el jugador
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador_rect)

    # Dibujar la meta
    pygame.draw.rect(pantalla, COLOR_META, meta_rect)

    # Dibujar los enemigos
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, COLOR_ENEMIGO, enemigo)

    # Dibujar las paredes
    for pared in paredes:
        pygame.draw.rect(pantalla, COLOR_PARED, pared)

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
