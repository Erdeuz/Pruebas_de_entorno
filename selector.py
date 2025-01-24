import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 600
ALTO = 600
COLOR_FONDO = (30, 30, 30)  # Gris oscuro
COLOR_BOTON = (50, 150, 255)  # Azul
COLOR_TEXTO = (255, 255, 255)  # Blanco

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Selector de Aplicaciones")

# Fuente
fuente = pygame.font.Font(None, 36)

# Configuración de los botones
botones = []
boton_ancho = 150
boton_alto = 50
espaciado = 20

for fila in range(3):
    for columna in range(3):
        x = columna * (boton_ancho + espaciado) + 75
        y = fila * (boton_alto + espaciado) + 75
        rect = pygame.Rect(x, y, boton_ancho, boton_alto)
        botones.append(rect)

# Nombres de los archivos .py a ejecutar
aplicaciones = [
    "mario.py", "pacman.py", "pacman2.py",
    "app4.py", "app5.py", "app6.py",
    "app7.py", "app8.py", "app9.py"
]


def ejecutar_aplicacion(nombre_archivo):
    try:
        os.system(f"python {nombre_archivo}")
    except Exception as e:
        print(f"Error al ejecutar {nombre_archivo}: {e}")


# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = pygame.mouse.get_pos()
            for i, boton in enumerate(botones):
                if boton.collidepoint(pos_mouse):
                    ejecutar_aplicacion(aplicaciones[i])

    # Dibujar la pantalla
    pantalla.fill(COLOR_FONDO)

    # Dibujar botones
    for i, boton in enumerate(botones):
        pygame.draw.rect(pantalla, COLOR_BOTON, boton)
        texto = fuente.render(f"Juego {i + 1}", True, COLOR_TEXTO)
        texto_rect = texto.get_rect(center=boton.center)
        pantalla.blit(texto, texto_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
