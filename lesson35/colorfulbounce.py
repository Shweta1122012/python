import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE=pygame.USEREVENT+2
BLUE=pygame.Color("blue")
LIGHTBLUE=pygame.Color("lightblue")
DARKBLUE=pygame.Color("darkblue")
YELLOW=pygame.Color("yellow")
RED=pygame.Color("red")
MAGENTA=pygame.Color("magenta")
GREEN=pygame.Color("green")

class sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundry_hit=True
        if self.rect.top<=0 or self.rect.bottom>=500:
            self.velocity[1]=-self.velocity[1]
            boundry_hit=True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE))
    def change_color(self):
        self.image.fill(random.choice([YELLOW,RED,MAGENTA,GREEN]))
def change_background():
    global bg_color
    bg_color=random.choice([BLUE,LIGHTBLUE,DARKBLUE])
al_sprites_list=pygame.sprite.Group()
sp1=sprite(RED,100,100)
sp1.rect.x=random.randint(0,400)
sp1.rect.y=random.randint(0,400)
al_sprites_list.add(sp1)
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("colorful bounce")
bg_color=BLUE
screen.fill(bg_color)
exit=False
clock=pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==SPRITE_COLOR_CHANGE:
            sp1.change_color()
        elif event.type==BACKGROUND_COLOR_CHANGE:
            change_background()
    al_sprites_list.update()
    screen.fill(bg_color)
    al_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()