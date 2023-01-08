

import pygame
import sys
from pygame.locals import *


pygame.init()

OKNOGRY_SZER = 800
OKNOGRY_WYS = 400
LT_BLUE = (0, 255, 255)

oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 100, 100)
pygame.display.set_caption('missing name lolz')

PALETKA_SZER = 50 
PALETKA_WYS = 10  
BLUE = (0, 255, 255)  
PALETKA_1_POZ = (350, 360)  
paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1.fill(BLUE)
paletka1_prost = paletka1.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

P_SZER = 20  
P_WYS = 20  
P_PREDKOSC_X = 6  
P_PREDKOSC_Y = 6  
GREEN = (0, 255, 0) 
pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(pilka, GREEN, [0, 0, P_SZER, P_WYS])
pilka_prost = pilka.get_rect()
pilka_prost.x = OKNOGRY_SZER / 2
pilka_prost.y = OKNOGRY_WYS / 2

FPS = 30 
fpsClock = pygame.time.Clock() 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION:
            myszaX, myszaY = event.pos 

            przesuniecie = myszaX - (PALETKA_SZER / 2)

            if przesuniecie > OKNOGRY_SZER - PALETKA_SZER:
                przesuniecie = OKNOGRY_SZER - PALETKA_SZER
            
            if przesuniecie < 0:
                przesuniecie = 0
          
            paletka1_prost.x = przesuniecie

    
    pilka_prost.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)

    
    if pilka_prost.right >= OKNOGRY_SZER:
        P_PREDKOSC_X *= -1
    if pilka_prost.left <= 0:
        P_PREDKOSC_X *= -1

    if pilka_prost.top <= 0:  
        P_PREDKOSC_Y *= -1  
    if pilka_prost.bottom >= OKNOGRY_WYS:  
        pilka_prost.x = OKNOGRY_SZER / 2  
        pilka_prost.y = OKNOGRY_WYS / 2

    if pilka_prost.colliderect(paletka1_prost):
        P_PREDKOSC_Y *= -1
        pilka_prost.bottom = paletka1_prost.top

    oknogry.fill(LT_BLUE)  

    oknogry.blit(paletka1, paletka1_prost)

    oknogry.blit(pilka, pilka_prost)

    pygame.display.update()

    fpsClock.tick(FPS)


