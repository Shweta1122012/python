import pygame
pygame.init()
SCREEN_WIDTH ,SCREEN_HEIGHT = 500,500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")
background=pygame.transform.scale(pygame.image.load(r"C:\Users\Public\python\after class project\visualback.jpg").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
penguin=pygame.transform.scale(pygame.image.load(r"C:\Users\Public\python\after class project\robot.jpg").convert_alpha(),(300,300))
rect=penguin.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-30))
def game_loop():
    clock=pygame.time.Clock()
    done=False
    while not done:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                done=True
        screen.blit(background,(0,0))
        screen.blit(penguin,rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=="__main__":
    game_loop()             