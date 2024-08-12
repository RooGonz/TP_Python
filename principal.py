#! /usr/bin/env python
import os
import random
import sys
import math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
from opcionesdejuego import*


def facil(TIME_inicio):
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))
  
    #musica
    musica()

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatoriosFACIL(producto, lista_productos, MARGEN)
    #print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(screen, productos_en_pantalla, producto,
            producto_candidato, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla):
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatoriosFACIL(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""

        segundos = TIME_inicio+TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(screen, productos_en_pantalla, producto,
                producto_candidato, puntos, segundos)

        pygame.display.flip()

    gameOver(puntos)        
  

def normal(TIME_inicio):
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #Música
    musica()

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatoriosNORMAL(producto, lista_productos, MARGEN)
    #print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(screen, productos_en_pantalla, producto,
            producto_candidato, puntos, segundos)
    
    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla):
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatoriosNORMAL(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""

        segundos = TIME_inicio+TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(screen, productos_en_pantalla, producto,
                producto_candidato, puntos, segundos)

        pygame.display.flip()
  
    gameOver(puntos)        
    

def dificil(TIME_inicio): 
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #musica
    musica()

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatoriosDIFICIL(producto, lista_productos, MARGEN)
    #print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(screen, productos_en_pantalla, producto,
            producto_candidato, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla):
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatoriosDIFICIL(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""

        segundos = TIME_inicio+TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(screen, productos_en_pantalla, producto,
                producto_candidato, puntos, segundos)

        pygame.display.flip()
        
    gameOver(puntos)       

# Programa Principal ejecuta Main
if __name__ == "__main__":
    
    while True:
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        # pygame.mixer.init()

        # Preparar la ventana
        pygame.display.set_caption("Peguele al precio")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        
        #menuPrincipal(screen)
            
        choice = menuPrincipal(screen)
        for e in pygame.event.get():

                # QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
            
        if choice == "jugar":
            #TIME_inicio=pygame.time.get_ticks()/1000
            dificultad = niveles(screen)
            if dificultad == "fácil":
                TIME_inicio=pygame.time.get_ticks()/1000
                facil(TIME_inicio)
                
            elif dificultad == "normal":
                TIME_inicio=pygame.time.get_ticks()/1000
                normal(TIME_inicio)
                
            elif dificultad == "dificil":
                TIME_inicio=pygame.time.get_ticks()/1000
                dificil(TIME_inicio)
                
        elif choice == "salir":
            pygame.quit()
            sys.exit()
            
            

    
        
        
       