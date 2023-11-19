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
Black = (0,0,0)
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load("./images/Map.png").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
BL = pygame.image.load("./images/BL.png").convert()
BL = pygame.transform.scale(BL, (screen_width, screen_height))
BC = pygame.image.load("./images/BC.png").convert()
BC = pygame.transform.scale(BC, (screen_width, screen_height))
BR = pygame.image.load("./images/BR.png").convert()
BR = pygame.transform.scale(BR, (screen_width, screen_height))
CL = pygame.image.load("./images/CL.png").convert()
CL = pygame.transform.scale(CL, (screen_width, screen_height))
MC = pygame.image.load("./images/MC.png").convert()
MC = pygame.transform.scale(MC, (screen_width, screen_height))
CR = pygame.image.load("./images/CR.png").convert()
CR = pygame.transform.scale(CR, (screen_width, screen_height))
TL = pygame.image.load("./images/TL.png").convert()
TL = pygame.transform.scale(TL, (screen_width, screen_height))
TC = pygame.image.load("./images/TC.png").convert()
TC = pygame.transform.scale(TC, (screen_width, screen_height))
TR = pygame.image.load("./images/TR.png").convert()
TR = pygame.transform.scale(TR, (screen_width, screen_height))
details = pygame.image.load("./images/details.png").convert()
details = pygame.transform.scale(details, (screen_width, screen_height))
 
#Load The images
imp = pygame.image.load("./images/Map.png")
imp = pygame.transform.scale(imp,(700,700))
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
imp11 = pygame.image.load("./images/details.png")
imp11 = pygame.transform.scale(imp11,(700,700))



 
#initilize the font
font = pygame.font.SysFont("Times New Roman", 32)

# Dibujar el fondo del mapa centrado
screen.blit(background_image, ((screen_width - background_image.get_width()) // 2, (screen_height - background_image.get_height()) // 2))

 
def RedrawGameWindow():
 
  
  BL
  BC
  BR
  CL
  MC
  CR
  TL
  TC
  TR
  background_image
 
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
 
  pygame.display.flip()
 
def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])
 
def checkGridX(grid):
  global RowMsg
  #Checks The Rows
 
  if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
     
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
     
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  #Checks The Collums
 
  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  #Checks Diagonals
 
  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    RowMsg = "Three Xs in a Diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a Diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
def checkGrid0(grid):
 
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  #Checks The Collums
 
  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  #Checks Diagonals
 
  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    RowMsg = "Three 0s in a diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Os in a Diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Os in a diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
 
#Intializing More varibles
grid = [[" "," "," "],[" "," "," "],[" "," "," "]] #creates the Consle Reperezentaio of the Grid
Turn = True # Deterumins wether its X or Os turn
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
                screen.blit(imp, (250,150))
              else:
                screen.blit(imp2, (250, 150))
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
                screen.blit(imp, (350,150))
              else:
                screen.blit(imp2, (350,150))
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
                screen.blit(imp, (450,150))
              else:
                screen.blit(imp2, (450,150))
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
                screen.blit(imp, (250,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,250))
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
                screen.blit(imp, (350,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (350,250))
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
                screen.blit(imp, (450,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (450,250))
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
                screen.blit(imp, (250,350))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,350))
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
                screen.blit(imp, (350,350))
                grid[row][col] = "X"
                Turn = False
               
              else:
                screen.blit(imp2, (350,350))
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
                screen.blit(imp, (450,350))
                grid[row][col] = "X"
                Turn = False
                checkGridX(grid)
              else:
                screen.blit(imp2, (450,350))
               
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
    text_rect2 = text.get_rect(center=(350, 500))
   
    screen.blit(text, text_rect)
    pygame.display.flip()  # Update the screen
 
 
# Quit pygame
pygame.quit()