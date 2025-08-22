import pygame
pygame.init()
SCREEN_WIDTH ,SCREEN_HEIGHT = 800,600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("welcome to pygame")
background=pygame.transform.scale(pygame.image.load(r"C:\Users\Public\python\lesson 33\background.png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
penguin=pygame.transform.scale(pygame.image.load(r"C:\Users\Public\python\lesson 33\penguin.png").convert_alpha(),(100,100))
rect=penguin.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-30))
text=pygame.font.Font(None,50).render("hello i am penguin",True,pygame.Color("black"))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))
def game_loop():
    clock=pygame.time.Clock()
    done=False
    while not done:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                done=True
        screen.blit(background,(0,0))
        screen.blit(penguin,rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=="__main__":
    game_loop()