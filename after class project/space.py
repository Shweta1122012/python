import math
from pygame import mixer
import random
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27


pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("space invader")
icon=pygame.image.load(r"C:\Users\Public\python\lesson37\ufo.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load(r"C:\Users\Public\python\lesson37\player.png")
playerx=PLAYER_START_X
playery=PLAYER_START_Y
playerx_change=0

enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemy=6

for _i in range(num_of_enemy):
    enemyimg.append(pygame.image.load(r"C:\Users\Public\python\lesson37\enemy.png"))
    enemyx.append(random.randint(0,SCREEN_WIDTH-64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_Y)

bulletimg=pygame.image.load(r"C:\Users\Public\python\lesson37\bullet.png")
bulletx=0
bullety=PLAYER_START_Y
bulletx_change=0
bullety_change=BULLET_SPEED_Y
bullet_state="ready"
bullet_sound=pygame.mixer.Sound(r"C:\Users\Public\python\after class project\bul.mp3")
explosion_sound=pygame.mixer.Sound(r"C:\Users\Public\python\after class project\bullet.mp3")


background_sound=pygame.mixer.Sound(r"C:\Users\Public\python\after class project\background.mp3")
pygame.mixer.music.load(r"C:\Users\Public\python\after class project\background.mp3")
pygame.mixer.music.play(-1)

score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
over_font=pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    bullet_sound.play()
    screen.blit(bulletimg,(x+16,y+10))

def is_collision(enemyx,enemyy,bulletx,bullety):
    
    distance=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance<COLLISION_DISTANCE
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(pygame.image.load(r"C:\Users\Public\python\lesson37\background.png"),(0,0))


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_SPACE and  bullet_state=="ready":
                bulletx=playerx
                fire_bullet(bulletx,bullety)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerx_change=0
    playerx+=playerx_change
    playerx=max(0,min(playerx,SCREEN_WIDTH-64))
    for i in range(num_of_enemy):
        if enemyy[i]>340:
            for j in range(num_of_enemy):
                enemyy[j]=2000
            game_over()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0 or enemyx[i]>=SCREEN_WIDTH-64:
            enemyx_change[i]*=-1
            enemyy[i]+=enemyy_change[i]
        if is_collision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety=PLAYER_START_Y
            bullet_state="ready"
            score_value+=1
            explosion_sound.play()
            enemyx[i]=random.randint(0,SCREEN_WIDTH-64)
            enemyy[i]=random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)
        enemy(enemyx[i],enemyy[i],i)
    if bullety<=0:
        bullety=PLAYER_START_Y
        bullet_state="ready"
    elif bullet_state=="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()

        

