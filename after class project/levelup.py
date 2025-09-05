import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE=pygame.USEREVENT+2
GREEN=pygame.Color("green")
DARKGREEN=pygame.Color("darkgreen")
LIGHTGREEN=pygame.Color("lightgreen")
YELLOW=pygame.Color("yellow")       
RED=pygame.Color("red")
MAGENTA=pygame.Color("magenta")
BLUE=pygame.Color("blue")


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
        self.image.fill(random.choice([YELLOW,RED,MAGENTA,BLUE]))
def change_background():
    global bg_color
    bg_color=random.choice([GREEN,LIGHTGREEN,DARKGREEN])
al_sprites_list=pygame.sprite.Group()
sp1=sprite(RED,100,100)
sp1.rect.x=random.randint(0,400)
sp1.rect.y=random.randint(0,400)
al_sprites_list.add(sp1)



colors={
        "purple":pygame.Color('purple'),
        "pink":pygame.Color('pink'),
        "orange":pygame.Color('orange'),
        "brown":pygame.Color('brown'),
        "white":pygame.Color('white'),
    }
current_color=colors["white"]
x, y = 30, 30
sprite_width, sprite_height = 70, 70
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("sprite game")
bg_color = BLUE

exit = False
clock = pygame.time.Clock()
while not exit:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, y), screen_height - sprite_height)
    if x == 0: current_color = colors["purple"]
    elif x == screen_width - sprite_width: current_color = colors["brown"]
    elif y == 0: current_color = colors["pink"]
    elif y == screen_height - sprite_height: current_color = colors["orange"]
    else: current_color = colors["white"]
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
    al_sprites_list.update()
    
    screen.fill(bg_color)
    al_sprites_list.draw(screen)
    pygame.draw.rect(screen, current_color, pygame.Rect(x, y, sprite_width, sprite_height))
    pygame.display.flip()
    clock.tick(240)
pygame.quit()
