import pygame


#funcion jugador
def jugador(img_jugador, x, y):
    pantalla.blit(img_jugador, (x, y))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #inicializamos pygame
    pygame.init()

    #crear la pantalla
    pantalla = pygame.display.set_mode((800, 600))

    #titulo
    pygame.display.set_caption("Invasión espacial")

    #icono
    icono = pygame.image.load("resources/space.png")
    pygame.display.set_icon(icono)

    #creamos al jugador y sus variables
    img_jugador = pygame.image.load("resources/rocket.png")
    posicion_jugador_x = 368
    posicion_jugador_y = 536

    #Loop del juego
    se_ejecuta = True
    movimiento_x = 0
    while se_ejecuta:
        # RGB pintando pantalla
        pantalla.fill((205, 144, 228))

        #traemos los eventos de pygame
        for evento in pygame.event.get():
            #activamos evento para cerrar la pantalla del juego
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            #recibimos el evento de tecla presionada
            if evento.type == pygame.KEYDOWN:
                #verificamos si se presionó la tecla de izquierda
                if evento.key == pygame.K_LEFT:
                    movimiento_x = -0.3
                # verificamos si se presionó la tecla de derecha
                if evento.key == pygame.K_RIGHT:
                    movimiento_x = 0.3

            #recibimos el evento para saber cuando la tecla es soltada
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimiento_x = 0

        posicion_jugador_x += movimiento_x
        jugador(img_jugador, posicion_jugador_x,posicion_jugador_y)

        pygame.display.update()
