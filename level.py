import pygame
pygame.init()
screen = pygame. display.set_mode((400,600))
pygame.display.set_caption("collision")
blue = (0,0,255)
white = (25,255,255)
red = (255,0,0)
p = pygame.Rect(60,60,40,40)
o= pygame.Rect(200,200,50,50)
pv = True
ov = True
run = True
speed = 4
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    is1=pygame.key.get_pressed()
    if is1[pygame.K_LEFT]:
        p.x-=speed
    if is1[pygame.K_RIGHT]:
        p.x+=speed
    if is1[pygame.K_DOWN]:
        p.y+=speed
    if is1[pygame.K_UP]:
        p.y-=speed
    if p.colliderect(o):
        ov=False
    screen.fill(white)
    if pv:
        pygame.draw.rect(screen,blue,p)
    if ov:
        pygame.draw.rect(screen,red,o)
    pygame.display.flip()
pygame.quit()