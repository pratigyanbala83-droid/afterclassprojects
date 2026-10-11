import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("abc")

BG = [pygame.Color("blue"),pygame.Color("lightblue"),pygame.Color("Darkblue")]
Colors = [pygame.Color("green"),pygame.Color("violet"),pygame.Color("grey"),pygame.Color("black")]

sprite_event = pygame.USEREVENT+1
background_event = pygame.USEREVENT+2


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=(random.randint(0,470),random.randint(0,380)))
        self.vel = [1,1]

    def update(self):
        self.rect.move_ip(self.vel)

        if self.rect.left <= 0 or self.rect.right >=500:
            self.vel[0]+=1
            pygame.event.post(pygame.event.Event(sprite_event))
            pygame.event.post(pygame.event.Event(background_event))

        if self.rect.top <= 0 or self.rect.bottom >=400:
                self.vel[1]*=-1
                pygame.event.post(pygame.event.Event(sprite_event))
                pygame.event.post(pygame.event.Event(background_event))

sp = Sprite()
clock = pygame.time.Clock()
bg = "blue"
ref = True
while ref :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            ref = False
        elif e.type == sprite_event :
            sp.image.fill(random.choice(Colors))
        elif e.type == background_event:
            bg = random.choice(BG)

    sp.update()
    screen.fill(bg)
    screen.blit(sp.image,sp.rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()



        
