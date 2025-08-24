import pygame
pygame.init()
SCREEN_WIDTH ,SCREEN_HEIGHT = 640,480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My first Game Screen")

rect = pygame.Rect(150, 150, 100, 100)
text = pygame.font.Font(None, 50).render("welcome to pygame screen", True, pygame.Color("white"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    done = False
    while not done:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                done = True
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 125, 255), rect)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
     
    rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    game_loop()