import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
COLOR_FONDO = (0, 0, 0)
COLOR_BARRA = (255, 255, 255)
COLOR_BOLA = (200, 50, 50)
COLOR_BLOQUE = (50, 200, 50)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Arkanoid")

# Configuración de la barra
barra_ancho = 100
barra_alto = 15
barra_x = ANCHO // 2 - barra_ancho // 2
barra_y = ALTO - barra_alto - 10
barra_velocidad = 7

# Configuración de la bola
bola_radio = 10
bola_x = ANCHO // 2
bola_y = ALTO // 2
bola_velocidad_x = 4
bola_velocidad_y = -4

# Configuración de los bloques
bloques = []
filas = 5
columnas = 10
bloque_ancho = ANCHO // columnas
bloque_alto = 20

for fila in range(filas):
    for columna in range(columnas):
        bloque_x = columna * bloque_ancho
        bloque_y = fila * bloque_alto
        bloques.append(pygame.Rect(
            bloque_x, bloque_y, bloque_ancho, bloque_alto))

# Bucle principal del juego
clock = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Controles de la barra
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and barra_x > 0:
        barra_x -= barra_velocidad
    if teclas[pygame.K_RIGHT] and barra_x < ANCHO - barra_ancho:
        barra_x += barra_velocidad

    # Movimiento de la bola
    bola_x += bola_velocidad_x
    bola_y += bola_velocidad_y

    # Colisiones con las paredes
    if bola_x - bola_radio <= 0 or bola_x + bola_radio >= ANCHO:
        bola_velocidad_x *= -1
    if bola_y - bola_radio <= 0:
        bola_velocidad_y *= -1

    # Colisión con la barra
    barra_rect = pygame.Rect(barra_x, barra_y, barra_ancho, barra_alto)
    bola_rect = pygame.Rect(bola_x - bola_radio, bola_y -
                            bola_radio, bola_radio * 2, bola_radio * 2)
    if bola_rect.colliderect(barra_rect):
        bola_velocidad_y *= -1

    # Colisiones con los bloques
    for bloque in bloques[:]:
        if bola_rect.colliderect(bloque):
            bloques.remove(bloque)
            bola_velocidad_y *= -1
            break

    # Condición de derrota
    if bola_y - bola_radio > ALTO:
        messagebox.showinfo("Fin del Juego", "Has perdido!")
        ejecutando = False

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_BARRA, barra_rect)
    pygame.draw.circle(pantalla, COLOR_BOLA, (bola_x, bola_y), bola_radio)

    for bloque in bloques:
        pygame.draw.rect(pantalla, COLOR_BLOQUE, bloque)

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
