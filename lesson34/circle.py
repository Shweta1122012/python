import pygame
pygame.init()
screen=pygame.display.set_mode((900,900))
screen.fill((255,255,255))
GREEN=(0,255,0)
pygame.draw.circle(screen,GREEN,(300,400),50)
pygame.draw.circle(screen,(0,0,0),(100,200),50,2)
pygame.display.update()
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()