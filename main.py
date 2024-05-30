import pygame
import random
import math


#funcion jugador
def jugador(img, x, y):
    pantalla.blit(img, (x, y))


#funcion enemigo
def enemigo(img, x, y):
    pantalla.blit(img_enemigo, (x, y))

#funcion disparar bala
def disparar_bala(img, x, y):
    global bala_visible
    bala_visible = True
    #x + 16, y + 10 es para que se vea como si la bala saliera desde el centro de la nave
    pantalla.blit(img, (x + 16, y + 10))

#funcion para detectar colision
def detectar_colision(objeto1_x, objeto1_y, objeto2_x, objeto2_y):
    #math.sqrt() -> raiz cuadrada
    operacion1 = (objeto2_x-objeto1_x)
    operacion2 = (objeto2_y-objeto1_y)
    formula_distancia = math.sqrt(math.pow(operacion1, 2) + math.pow(operacion2, 2))
    if formula_distancia < 10:
        return True
    else:
        return False



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

    #fondo_pantalla
    seleccionar_fondo = random.choice(("background.jpg", "background_2.jpg", "background_3.jpg"))
    fondo = pygame.image.load('resources/{}'.format(seleccionar_fondo))

    #creamos al jugador y sus variables
    img_jugador = pygame.image.load("resources/rocket.png")
    posicion_jugador_x = 368
    posicion_jugador_y = 500

    #creamos al enemigo y sus variables
    img_enemigo = pygame.image.load("resources/spacecraft.png")
    posicion_enemigo_x = random.randint(0, 736)
    posicion_enemigo_y = random.randint(50, 200)
    enemigo_x_cambio = 0.5 #velocidad del enemigo
    enemigo_y_cambio = 50

    # creamos la bala y sus variables
    img_bala = pygame.image.load("resources/bullet.png")
    posicion_bala_x = 0
    posicion_bala_y = 500
    bala_x_cambio = 0
    bala_y_cambio = 3 #velocidad de la bala
    bala_visible = False

    #puntaje
    puntaje = 0

    #Loop del juego
    se_ejecuta = True
    movimiento_x = 0
    while se_ejecuta:
        # RGB pintando pantalla
        pantalla.blit(fondo, (0,0))

        #traemos los eventos de pygame
        for evento in pygame.event.get():
            #activamos evento para cerrar la pantalla del juego
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            #recibimos el evento de tecla presionada
            if evento.type == pygame.KEYDOWN:
                #verificamos si se presionó la tecla de izquierda
                if evento.key == pygame.K_LEFT:
                    movimiento_x = -1
                # verificamos si se presionó la tecla de derecha
                if evento.key == pygame.K_RIGHT:
                    movimiento_x = 1
                if evento.key == pygame.K_UP:
                    if not bala_visible:
                        bala_disparada = posicion_jugador_x
                        disparar_bala(img_bala, bala_disparada, posicion_bala_y)

            #recibimos el evento para saber cuando la tecla fue soltada
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimiento_x = 0

        #modificando la ubicacion de la nave
        posicion_jugador_x += movimiento_x
        # modificando la ubicacion del enemigo
        posicion_enemigo_x += enemigo_x_cambio




        #mantener cohete dentro de los margenes de la pantalla de juego
        if posicion_jugador_x <=0:
           posicion_jugador_x = 0
        if posicion_jugador_x >=736:
           posicion_jugador_x = 736

        # mantener enemigo dentro de los margenes de la pantalla de juego
        if posicion_enemigo_x <= 0:
           enemigo_x_cambio = 0.5
           posicion_enemigo_y += enemigo_y_cambio
        if posicion_enemigo_x >= 736:
           enemigo_x_cambio = -0.5
           posicion_enemigo_y += enemigo_y_cambio

        #movimiento bala
        if posicion_bala_y <= -64:
            posicion_bala_y = 500
            bala_visible = False

        if bala_visible:

            disparar_bala(img_bala, bala_disparada, posicion_bala_y)
            posicion_bala_y -= bala_y_cambio

        # colision detectada
        colision = detectar_colision(posicion_enemigo_x, posicion_enemigo_y, posicion_bala_x, posicion_bala_y)
        if (colision):
            posicion_bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)

        # modificando la ubicacion del enemigo
        enemigo(img_enemigo, posicion_enemigo_x, posicion_enemigo_y)
        # modificando la ubicacion de la nave
        jugador(img_jugador, posicion_jugador_x, posicion_jugador_y)

        #actualizar juego
        pygame.display.update()
