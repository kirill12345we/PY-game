import pygame
import math
import random

# Beginning
pygame.init()

screen = pygame.display.set_mode((800, 800))

sprites = [
    "mario.png",
    "marion.png",
    "marioj.png",
    "mariorev.png",
    "marionrev.png",
    "mariojrev.png",
    "mariob.png",
    "mariost.png",
    "mariostrev.png",
    "mariostend.png",
    "mariostendrev.png",
    "dk.png",
    "dkb.png",
    "phelp.png",
    "plove.png",
    "marioll.png",
    "marioh.png",
    "logo.png",
    "lotsofbarrels.png"
]

platforms = [
    ((800, 740), (800, 770), (0, 800), (0, 770)),
    ((26, 619), (720, 653), (720, 683), (26, 649)),
    ((774, 504), (774, 534), (80, 562), (80, 532)),
    ((26, 382), (720, 416), (720, 446), (26, 412)),
    ((774, 266), (774, 296), (80, 325), (80, 295)),
    ((320, 159), (720, 178), (720, 208), (320, 189)),
    ((320, 69), (480, 69), (480, 99), (320, 99)),
    ((26, 159), (320, 159), (320, 189), (26, 189)),
    ((240, 99), (320, 99), (320, 129), (240, 129))
]

# Characters / Texts
Mario = pygame.transform.scale(pygame.image.load(sprites[1]), (30, 45))
Dk = pygame.transform.scale(pygame.image.load(sprites[11]), (150, 110))
Princess = pygame.transform.scale(pygame.image.load(sprites[13]), (80, 60))
last_sprt = sprites[1]

# Draw Functions 
def draw_screen(stairs, stairs_broken, platforms):
    for s in stairs:
        pygame.draw.polygon(screen, pygame.Color('blue'), s[1])
    for sb in stairs_broken:
        pygame.draw.polygon(screen, pygame.Color('brown'), sb[1])
    for p in platforms:
        pygame.draw.polygon(screen, pygame.Color('red'), p)
    screen.blit(pygame.transform.scale(pygame.image.load(sprites[18]), (75, 100)), (25, 60))

# Stairs Detection Functions
def inst(x, y, plat, size):
    stairs_plat = []
    for s in stairs:
        if s[0] == plat:
            stairs_plat.append(s[1])
    for ss in stairs_plat:
        if int(x) + (size[0] / 2) in range(ss[0][0], ss[1][0]) and y <= y_min(x, cplat) - size[1]:
            return True
    return False

def inbst(x, y, plat, size):
    bstairs_plat = []
    for sb in stairs_broken:
        if sb[0] == plat:
            bstairs_plat.append(sb[1])
    for ssb in bstairs_plat:
        if int(x) + (size[0] / 2) in range(ssb[0][0], ssb[1][0]) and y <= y_min(x, cplat) - size[1]:
            return True
    return False

# Main Game Loop
x = 180
y = 763
cplat = 0
plat_max = 0
jumptime = 0
climbing = False
lost_life = False
win = False
time_last_barrel = pygame.time.get_ticks()
score = 0
rscore = 0

while True:
    dt = clock.tick(30) / 50
    if dt > 3:
        dt = 1

    keys = pygame.key.get_pressed()

    if inst(x, y, cplat - 1, (30, 45)) is True and keys[pygame.K_DOWN]:
        cplat -= 1
        climbing = True

    if keys[pygame.K_q]:
        running = False

    if keys[pygame.K_m]:
        play = False
        menu = True

    if keys[pygame.K_SPACE]:
        if y == y_min(x, cplat) - 45:
            jumptime = 10

    if keys[pygame.K_RIGHT]:
        if int(x) < 760 and climbing is False:
            x += 5 * dt

    if keys[pygame.K_LEFT]:
        if cplat < 5:
            if int(x) > 0 and climbing is False:
                x -= 5 * dt
        else:
            if int(x) > 320 and climbing is False:
                x -= 5
