import pygame

pygame.init()

# Imágenes de las celdas
BL = pygame.image.load('./images/BL.png')
BC = pygame.image.load('./images/BC.png')
BR = pygame.image.load('./images/BR.png')
ML = pygame.image.load('./images/CL.png')
MC = pygame.image.load('./images/MC.png')
MR = pygame.image.load('./images/CR.png')
TL = pygame.image.load('./images/TL.png')
TC = pygame.image.load('./images/TC.png')
TR = pygame.image.load('./images/TR.png')

# Inicializa el array con imágenes en lugar de texto
grid = [[BL, BC, BR],
        [ML, MC, MR],
        [TL, TC, TR]]

# Dentro del bucle principal
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # Encuentra la celda clicada
        row = None
        col = None
        for i in range(3):
            for j in range(3):
                if grid[i][j].get_rect().collidepoint(pygame.mouse.get_pos()):
                    row = i
                    col = j
                    break

        if row is not None and col is not None:
            if "X" in grid[row][col] or "O" in grid[row][col]:
                print("Stop")
            else:
                if Turn:
                    screen.blit(imp22, grid[row][col].get_rect())  # Imagen azul
                    grid[row][col] = "X"
                    Turn = False
                else:
                    screen.blit(imp13, grid[row][col].get_rect())  # Imagen roja
                    grid[row][col] = "O"
                    Turn = True