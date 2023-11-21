#test
#battle ships

#Instrucciones para INSTALAR y ACTIVAR un entorno virtual porque soy burra:
#instalar virtualenv poniendo en la terminal pip install virtualenv
#ejecutar en la terminal python -m virtualenv env
#para activarlo:
#source env/Scripts/activate
#para chequear que esté activado ver si aparece el (env) antes de toda la otra mersa

import pygame
print(pygame.__version__)

 
# Initialize pygame
pygame.init()
 
# Set up the screen
Black = (255,255,255)
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
##############imagen de fondo#################
background_image = pygame.image.load("./images/Map.png").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
##############países originales ##############
BL = pygame.image.load("./images/BL.png")
BL = pygame.transform.scale(BL, (screen_width, screen_height))
BC = pygame.image.load("./images/BC.png")
BC = pygame.transform.scale(BC, (screen_width, screen_height))
BR = pygame.image.load("./images/BR.png")
BR = pygame.transform.scale(BR, (screen_width, screen_height))
CL = pygame.image.load("./images/CL.png")
CL = pygame.transform.scale(CL, (screen_width, screen_height))
MC = pygame.image.load("./images/MC.png")
MC = pygame.transform.scale(MC, (screen_width, screen_height))
CR = pygame.image.load("./images/CR.png")
CR = pygame.transform.scale(CR, (screen_width, screen_height))
TL = pygame.image.load("./images/TL.png")
TL = pygame.transform.scale(TL, (screen_width, screen_height))
TC = pygame.image.load("./images/TC.png")
TC = pygame.transform.scale(TC, (screen_width, screen_height))
TR = pygame.image.load("./images/TR.png")
TR = pygame.transform.scale(TR, (screen_width, screen_height))
#####################detalles, coronas y outline##############
details = pygame.image.load("./images/details.png")
details = pygame.transform.scale(details, (screen_width, screen_height))
outline = pygame.image.load("./images/outline.png")
outline = pygame.transform.scale(outline, (screen_width, screen_height))
red = pygame.image.load("./images/red.png")
blue = pygame.image.load("./images/blue.png")
##################países en rojo######################
BLR = pygame.image.load("./images/RED BL.png")
BLR = pygame.transform.scale(BLR, (screen_width, screen_height))

BCR = pygame.image.load("./images/RED BC.png")
BCR = pygame.transform.scale(BCR, (screen_width, screen_height))

BRR = pygame.image.load("./images/RED BR.png")
BRR = pygame.transform.scale(BLR, (screen_width, screen_height))

CLR = pygame.image.load("./images/RED CL.png")
CLR = pygame.transform.scale(CLR, (screen_width, screen_height))

MCR = pygame.image.load("./images/RED MIDDLE.png")
MCR = pygame.transform.scale(MCR, (screen_width, screen_height))

CRR = pygame.image.load("./images/RED CR.png")
CRR = pygame.transform.scale(CRR, (screen_width, screen_height))

TLR = pygame.image.load("./images/RED TL.png")
TLR = pygame.transform.scale(TLR, (screen_width, screen_height))

TCR = pygame.image.load("./images/RED TC.png")
TCR = pygame.transform.scale(TCR, (screen_width, screen_height))

TRR = pygame.image.load("./images/RED TR.png")
TRR = pygame.transform.scale(TRR, (screen_width, screen_height))
##################países en azul######################
BLB = pygame.image.load("./images/BLUE BL.png")
BLB = pygame.transform.scale(BLB, (screen_width, screen_height))

BCB = pygame.image.load("./images/BLUE BC.png")
BCB = pygame.transform.scale(BCB, (screen_width, screen_height))

BRB = pygame.image.load("./images/BLUE BR.png")
BRB = pygame.transform.scale(BRB, (screen_width, screen_height))

CLB = pygame.image.load("./images/BLUE CL.png")
CLB = pygame.transform.scale(CLB, (screen_width, screen_height))

MCB = pygame.image.load("./images/BLUE MIDDLE.png")
MCB = pygame.transform.scale(MCB, (screen_width, screen_height))

CRB = pygame.image.load("./images/BLUE CR.png")
CRB = pygame.transform.scale(CRB, (screen_width, screen_height))

TLB = pygame.image.load("./images/BLUE TL.png")
TLB = pygame.transform.scale(TLB, (screen_width, screen_height))

TCB = pygame.image.load("./images/BLUE TC.png")
TCB = pygame.transform.scale(TCB, (screen_width, screen_height))

TRB = pygame.image.load("./images/BLUE TR.png")
TRB = pygame.transform.scale(TRB, (screen_width, screen_height))

 
#Load The images
####mapa
imp = pygame.image.load("./images/Map.png")
imp = pygame.transform.scale(imp,(700,700))
####países originales
imp2 = pygame.image.load("./images/BL.png")
imp2 = pygame.transform.scale(imp2,(700,700))
imp3 = pygame.image.load("./images/BC.png")
imp3 = pygame.transform.scale(imp3,(700,700))
imp4 = pygame.image.load("./images/BR.png")
imp4 = pygame.transform.scale(imp4,(700,700))
imp5 = pygame.image.load("./images/CL.png")
imp5 = pygame.transform.scale(imp5,(700,700))
imp6 = pygame.image.load("./images/MC.png")
imp6 = pygame.transform.scale(imp6,(700,700))
imp7 = pygame.image.load("./images/CR.png")
imp7 = pygame.transform.scale(imp7,(700,700))
imp8 = pygame.image.load("./images/TL.png")
imp8 = pygame.transform.scale(imp8,(700,700))
imp9 = pygame.image.load("./images/TC.png")
imp9 = pygame.transform.scale(imp9,(700,700))
imp10 = pygame.image.load("./images/TR.png")
imp10 = pygame.transform.scale(imp10,(700,700))
####detalles y outline
imp11 = pygame.image.load("./images/details.png")
imp11 = pygame.transform.scale(imp11,(700,700))
imp12 = pygame.image.load("./images/outline.png")
imp12 = pygame.transform.scale(imp12,(700,700))
imp31 = pygame.image.load("./images/red.png")
imp32 = pygame.image.load("./images/blue.png")
####países en rojo
imp13 = pygame.image.load("./images/RED BL.png")
imp13 = pygame.transform.scale(imp13,(700,700))
imp14 = pygame.image.load("./images/RED BC.png")
imp14 = pygame.transform.scale(imp14,(700,700))
imp15 = pygame.image.load("./images/RED BR.png")
imp15 = pygame.transform.scale(imp15,(700,700))
imp16 = pygame.image.load("./images/RED CL.png")
imp16 = pygame.transform.scale(imp16,(700,700))
imp17 = pygame.image.load("./images/RED MIDDLE.png")
imp17 = pygame.transform.scale(imp17,(700,700))
imp18 = pygame.image.load("./images/RED CR.png")
imp18 = pygame.transform.scale(imp18,(700,700))
imp19 = pygame.image.load("./images/RED TL.png")
imp19 = pygame.transform.scale(imp19,(700,700))
imp20 = pygame.image.load("./images/RED TC.png")
imp20 = pygame.transform.scale(imp20,(700,700))
imp21 = pygame.image.load("./images/RED TR.png")
imp21 = pygame.transform.scale(imp21,(700,700))
####países en azul
imp22 = pygame.image.load("./images/BLUE BL.png")
imp22 = pygame.transform.scale(imp22,(700,700))
imp23 = pygame.image.load("./images/BLUE BC.png")
imp23 = pygame.transform.scale(imp23,(700,700))
imp24 = pygame.image.load("./images/BLUE BR.png")
imp24 = pygame.transform.scale(imp24,(700,700))
imp25 = pygame.image.load("./images/BLUE CL.png")
imp25 = pygame.transform.scale(imp25,(700,700))
imp26 = pygame.image.load("./images/BLUE MIDDLE.png")
imp26 = pygame.transform.scale(imp26,(700,700))
imp27 = pygame.image.load("./images/BLUE CR.png")
imp27 = pygame.transform.scale(imp27,(700,700))
imp28 = pygame.image.load("./images/BLUE TL.png")
imp28 = pygame.transform.scale(imp28,(700,700))
imp29 = pygame.image.load("./images/BLUE TC.png")
imp29 = pygame.transform.scale(imp29,(700,700))
imp30 = pygame.image.load("./images/BLUE TR.png")
imp30 = pygame.transform.scale(imp30,(700,700))




 
#initilize the font
font = pygame.font.SysFont("Times New Roman", 32)



 
def RedrawGameWindow():
  
  # Dibujar las imágenes centradas
  ####Mapa
  screen.blit(background_image, ((screen_width - background_image.get_width()) // 2, (screen_height - background_image.get_height()) // 2))
  ####países originales
  screen.blit(BL, ((screen_width - BL.get_width()) // 2, (screen_height - BL.get_height()) // 2))
  screen.blit(BC, ((screen_width - BC.get_width()) // 2, (screen_height - BC.get_height()) // 2))
  screen.blit(BR, ((screen_width - BR.get_width()) // 2, (screen_height - BR.get_height()) // 2))
  screen.blit(CL, ((screen_width - CL.get_width()) // 2, (screen_height - CL.get_height()) // 2))
  screen.blit(MC, ((screen_width - MC.get_width()) // 2, (screen_height - MC.get_height()) // 2))
  screen.blit(CR, ((screen_width - CR.get_width()) // 2, (screen_height - CR.get_height()) // 2))
  screen.blit(TL, ((screen_width - TL.get_width()) // 2, (screen_height - TL.get_height()) // 2))
  screen.blit(TC, ((screen_width - TC.get_width()) // 2, (screen_height - TC.get_height()) // 2))
  screen.blit(TR, ((screen_width - TR.get_width()) // 2, (screen_height - TR.get_height()) // 2))
  ####detalles y outline
  screen.blit(details, ((screen_width - details.get_width()) // 2, (screen_height - details.get_height()) // 2))
  screen.blit(outline, ((screen_width - outline.get_width()) // 2, (screen_height - outline.get_height()) // 2))
  ####países rojos
  
  ####países azules


  

  global G00
  global G01
  global G02
  global G10
  global G11
  global G12
  global G20
  global G21
  global G22
 
  G00 =pygame.draw.rect(screen, Black, (250, 150, 100, 100), 1)
 
  G01 = pygame.draw.rect(screen, Black, (350, 150, 100, 100), 1)
 
  G02 = pygame.draw.rect(screen, Black, (450, 150, 100, 100), 1)  
 
  G10 = pygame.draw.rect(screen, Black, (250, 250, 100, 100), 1)
   
  G11 = pygame.draw.rect(screen, Black, (350, 250, 100, 100), 1)
 
  G12 =pygame.draw.rect(screen, Black, (450, 250, 100, 100), 1)
 
  G20 =pygame.draw.rect(screen, Black, (250, 350, 100, 100), 1)
 
  G21 = pygame.draw.rect(screen, Black, (350, 350, 100, 100), 1)
 
  G22 = pygame.draw.rect(screen, Black, (450, 350, 100, 100), 1)
 
  grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
 
  pygame.display.update()
 
def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])
 
def checkGridX(grid):
  global RowMsg

  #Chequea las filas

  if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
     
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, screen_height/3))
    screen.blit(text3, text_rect3)
     
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Chequea las columnas
  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  #Chequea las diagonales
  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
def checkGrid0(grid):
 
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  #Checks The Collums
 
  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  #Checks Diagonals
 
  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
#Inicialización de más variables
grid = [[" "," "," "],[" "," "," "],[" "," "," "]] #creates the Consle Reperezentaio of the Grid
Turn = True # Determina si es el turno del Rey Rojo o el Rey Azul
#winner = False
 
#Creates the Grid In Pygame
 
 
displayGrid(grid)
RedrawGameWindow()
# Set up the game loop
running = True
while running:
    # Handle events
 
    for event in pygame.event.get():
     
      #Mouse Detection
      #Checks For mouse clicking within each aquare
      #pygame.KEYDOWN hace que el juego se reinicie al apretar la tecla R.
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          RedrawGameWindow()
          grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
          Turn = True
 
      if event.type == pygame.MOUSEBUTTONDOWN:
         
          if G00.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 0
            if "X" in grid[0][0] or "O" in grid[0][0]: # Checks wether the grid is empty
              print("stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp31, (250,150))
              else:
                screen.blit(imp32, (250, 150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
             
             
           
              displayGrid(grid)
           
              pygame.display.flip()
              checkGridX(grid)
          if G01.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 1
            if "X" in grid[0][1] or "O" in grid[0][1]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp31, (350,150))
              else:
                screen.blit(imp32, (350,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
 
              pygame.display.flip()
              checkGridX(grid)
             
          if G02.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 2
            if "X" in grid[0][2] or "O" in grid[0][2]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp31, (450,150))
              else:
                screen.blit(imp32, (450,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                displayGrid(grid)
             
              pygame.display.flip()
              checkGridX(grid)
          if G10.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 0
            if "X" in grid[1][0] or "O" in grid[1][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp31, (250,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (250,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
           
              pygame.display.flip()
              checkGridX(grid)
          if G11.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 1
            if "X" in grid[1][1] or "O" in grid[1][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp31, (350,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (350,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
           
              pygame.display.flip()
              checkGridX(grid)
          if G12.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 2
            if "X" in grid[1][2] or "O" in grid[1][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp31, (450,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (450,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
             
              pygame.display.flip()
              checkGridX(grid)
          if G20.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 0
            if "X" in grid[2][0] or "O" in grid[2][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp31, (250,350))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (250,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
             
              pygame.display.flip()
              checkGridX(grid)
          if G21.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 1
            if "X" in grid[2][1] or "O" in grid[2][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp31, (350,350))
                grid[row][col] = "X"
                Turn = False
               
              else:
                screen.blit(imp32, (350,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
             
              pygame.display.flip()
              checkGridX(grid)
          if G22.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 2
            if "X" in grid[2][2] or "O" in grid[2][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp31, (450,350))
                grid[row][col] = "X"
                Turn = False
                checkGridX(grid)
              else:
                screen.blit(imp32, (450,350))
               
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
               
              displayGrid(grid)
             
              pygame.display.flip()
              checkGridX(grid)
 
      if event.type == pygame.QUIT: #Checks whether you pressed the X button
        running = False
   
    text = font.render("", True, (0, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(screen_width/2, 100))  # Get the rectangle for the text
   
    #text2 = font.render(RowMsg, True, (0, 0, 0))  # Render the text
    text_rect2 = text.get_rect(center=(350, 350))
   
    screen.blit(text, text_rect)
    pygame.display.flip()  # Update the screen
 
 
# Quit pygame
pygame.quit()