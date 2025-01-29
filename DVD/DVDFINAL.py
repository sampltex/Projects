import pygame
from pygame.locals import *
import random

# I WANT TO ADD MOMENTUM WHEN YOU MOVE IT WITH YOUR MOUSE BUT I CANT FIGURE IT OUT RIGHT NOW
print("Click and hold with your mouse to move the DVD logo!")

pygame.init()

windowHeight = 576 # 576
windowWidth = 1024 # 1024

dvdposx,dvdposy = 512,288

screen = pygame.display.set_mode((windowWidth,windowHeight))

dvd = Rect(dvdposx-113,dvdposy-56,226,112)
dvdreal = Rect(dvdposx-113,dvdposy-112,226,112)

def fill(surface, color):
    # i stole this function; skrx on stack overflow
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def edgeCollisionCheckx(dvdposx):
    # print(f"X AXIS:{dvdposx}")
    if dvdposx < 113 or dvdposx > windowWidth-113:
        return -1
    else:
        return 1
def edgeCollisionChecky(dvdposy):
    # print(f"Y AXIS:{dvdposy}")
    if dvdposy < 56 or dvdposy > windowHeight-56:
        return -1
    else:
        return 1
    
logo = pygame.image.load("logo1.png").convert_alpha()
# imagerect = logo.get_rect()
fill(logo, pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

running = True
clock = pygame.time.Clock()

dvdspeedx = 2
dvdspeedy = 2

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                dvdspeedx,dvdspeedy = 2,2
                print("enter")

    dvdposx += dvdspeedx
    dvdposy += dvdspeedy

    dvdspeedx *= edgeCollisionCheckx(dvdposx)
    dvdspeedy *= edgeCollisionChecky(dvdposy)
    dvd.move_ip(dvdspeedx,dvdspeedy)
    dvdreal.move_ip(dvdspeedx,dvdspeedy)

    prefposx = dvdposx * 1
    prefposy = dvdposy * 1

    clock.tick(60)
    prefpressed = None
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        dvdposx,dvdposy = pygame.mouse.get_pos()
        dvd.move_ip(dvdposx-prefposx,dvdposy-prefposy)
        dvdreal.move_ip(dvdposx-prefposx,dvdposy-prefposy)
        prefpressed = True

    if edgeCollisionCheckx(dvdposx) == -1 or edgeCollisionChecky(dvdposy) == -1:
        fill(logo, pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    screen.fill("black")

    pygame.draw.rect(screen, (0,0,0,128), dvd, 0)
    pygame.draw.rect(screen, (0,0,0,128), dvdreal, 0)
    screen.blit(logo, dvdreal)
    pygame.display.update()

    # if prefpressed:
    #     dvdspeedx = dvdposx - prefposx
    #     dvdspeedy = dvdposy - prefposy 
    #     print(dvdposx,dvdposy)
    #     print(prefposx,prefposy)