import os
import random
import sys
import math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
from principal import *

def menuPrincipal(screen): 
    font = pygame.font.Font(None, 60) #cargar una fuente y crear un objeto de fuente
    menu_items = ("Jugar","Salir")
    item_posiciones=[(100,100),(100,150)] # Posiciones de los textos
    fondo = pygame.image.load("supert.jpg") # Carga la imagen de fondo
    menu_surface = pygame.Surface((ANCHO,ALTO)) #Superficie para el menú
    menu_surface.set_colorkey ((0,0,0)) # Establecer el color transparente
    
    musica()

    while True:
        menu_surface.fill ((0,0,0)) #(0, 0, 0) color negro
        # Limpiar la superficie del menú
        for index, item in enumerate(menu_items):
            label = font.render(item, True, (255,165,0))
            # Color naranja (R:255, G:165, B:0)
            pos = item_posiciones[index]
            screen.blit(label, pos)
            menu_surface.blit(label, pos)

        screen.blit(fondo, (0, 0))# Dibuja el fondo

        screen.blit(menu_surface, (250, 150))# Dibuja el menu sobre el fondo


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                for index, pos in enumerate(item_posiciones):
                    if pos[0] < mouse_pos[0] < pos[0] + 350 and pos[1] < mouse_pos[1] < pos[1] + 200:
                        if index == 0: # Jugar
                            #niveles()
                            return "jugar"
                        elif index == 1: # Salir
                            #pygame.quit()
                            return "salir"

def niveles(screen):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Peguele al precio")
    font = pygame.font.Font(None, 60) #cargar una fuente y crear un objeto de fuente
    menu_items = ("Fácil","Medio","Dificil")
    item_posiciones=[(100,100),(100,150),(100,200)]# Posiciones de los textos
    fondo = pygame.image.load("supert.jpg") # Carga la imagen de fondo
    menu_surface = pygame.Surface((ANCHO,ALTO)) #Superficie para el menú
    menu_surface.set_colorkey ((0,0,0)) # Establecer el color transparente

    while True:
        for e in pygame.event.get():

                # QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return ()
                
        menu_surface.fill ((0,0,0)) #(0, 0, 0) color negro
        # Limpiar la superficie del menú
        for index, item in enumerate(menu_items):
            label = font.render(item, True, (255,165,0))
            # Color naranja (R:255, G:165, B:0)
            pos = item_posiciones[index]
            screen.blit(label, pos)
            menu_surface.blit(label, pos)

        screen.blit(fondo, (0, 0))# Dibuja el fondo

        screen.blit(menu_surface, (250, 100))# Dibuja el menu sobre el fondo
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for index, pos in enumerate(item_posiciones):
                    #print(event)
                    if pos[0] < mouse_pos[0] < pos[0] + 350 and pos[1] < mouse_pos[1] < pos[1] + 200:
                        if index == 0: # Fácil
                            #TIME_inicio=pygame.time.get_ticks()/1000
                            #facil(TIME_inicio)
                            return "fácil"
                        elif index == 1: # dificultad Medio
                            #TIME_inicio=pygame.time.get_ticks()/1000
                            #normal(TIME_inicio)
                            return "normal"
                        elif index == 2:
                            #TIME_inicio=pygame.time.get_ticks()/1000
                            #dificil(TIME_inicio)
                            return "dificil"

def gameOver(puntos):
    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    font = pygame.font.Font(None, 60) #cargar una fuente y crear un objeto de fuente
    menu_items = ("Volver a jugar","Salir")
    item_posiciones=[(30,150),(90,250)] # Posiciones de los textos
    #fondo = pygame.image.load("compras.jpeg")
    fondo = pygame.image.load("supert.jpg") # Carga la imagen de fondo
    menu_surface = pygame.Surface((ANCHO,ALTO)) #Superficie para el menú
    menu_surface.set_colorkey ((0,0,0)) # Establecer el color transparente

    while True:
        menu_surface.fill ((0,0,0)) #(0, 0, 0) color negro
        # Limpiar la superficie del menú
        for index, item in enumerate(menu_items):
            label = font.render(item, True, (255,165,0))
            # Color naranja (R:255, G:165, B:0)
            pos = item_posiciones[index]
            screen.blit(label, pos)
            menu_surface.blit(label, pos)
        screen.blit(fondo, (0, 0))# Dibuja el fondo
        screen.blit(menu_surface, (250, 150))# Dibuja el menu sobre el fondo
        defaultFont = pygame.font.Font(pygame.font.get_default_font(), 60)
        ptos = defaultFont.render("PUNTOS", 1, COLOR_PUNTOS)
        screen.blit(ptos,(270,100))
        ptos1 = defaultFont.render(str(puntos), 1, COLOR_PUNTOS)
        screen.blit(ptos1,(325,200))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for index, pos in enumerate(item_posiciones):
                    if 300-pos[0] < mouse_pos[0] < pos[0] + 350 and pos[1] < mouse_pos[1] < pos[1] + 200:
                        if index == 0: # Jugar
                            #TIME_inicio=pygame.time.get_ticks()/1000
                            #niveles(screen)
                            return "Volver a jugar"

                        elif index == 1: # Salir
                            pygame.quit()
                            sys.exit()
                            return "salir"