import pygame
print(pygame.__version__)

screen_width = 700
screen_height = 700
BL = pygame.image.load("./images/BL.png")
BL = pygame.transform.scale(BL, (screen_width, screen_height))
BLR = pygame.image.load("./images/Bottom left/RED BL.png")
BLR = pygame.transform.scale(BLR, (screen_width, screen_height))

imp = pygame.image.load("./images/BL.png")
imp = pygame.transform.scale(imp,(700,700))
imp2 = pygame.image.load("./images/Bottom left/RED BL.png")
imp2 = pygame.transform.scale(imp2,(700,700))


turn = 1 
if turn == 1:
    Screen.blit(BLR, ((screen_width - BLR.get_width()) // 2, (screen_height - BLR.get_height()) // 2))
