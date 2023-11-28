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
Black =(255,255,255)
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
##############imagen de fondo#################
background_image = pygame.image.load("./images/Map.png").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

#####################detalles, coronas y outline##############
details = pygame.image.load("./images/details.png")
details = pygame.transform.scale(details, (screen_width, screen_height))
outline = pygame.image.load("./images/outline.png")
outline = pygame.transform.scale(outline, (screen_width, screen_height))
red = pygame.image.load("./images/red.png")
blue = pygame.image.load("./images/blue.png")


 
#Load The images
####mapa
imp = pygame.image.load("./images/Map.png")
imp = pygame.transform.scale(imp,(700,700))

####detalles y outline
imp11 = pygame.image.load("./images/details.png")
imp11 = pygame.transform.scale(imp11,(700,700))
imp12 = pygame.image.load("./images/outline.png")
imp12 = pygame.transform.scale(imp12,(700,700))
imp31 = pygame.image.load("./images/red.png")
imp32 = pygame.image.load("./images/blue.png")


#inicializar el puntaje
puntos_rojo = 0
puntos_azul= 0


 
#initilize the font
font = pygame.font.Font("Alkhemikal.ttf", 32)
points_font = pygame.font.Font("Alkhemikal.ttf", 48)



 
def RedrawGameWindow():
  
  # Dibujar las imágenes centradas
  ####Mapa
  screen.blit(background_image, ((screen_width - background_image.get_width()) // 2, (screen_height - background_image.get_height()) // 2))
  
  ####detalles y outline
  screen.blit(details, ((screen_width - details.get_width()) // 2, (screen_height - details.get_height()) // 2))
  screen.blit(outline, ((screen_width - outline.get_width()) // 2, (screen_height - outline.get_height()) // 2))
  ####países rojos
  
  #renderiza puntajes
  text4 = points_font.render(str(puntos_rojo), True, (0, 0, 0))
  text_rect4 =text4.get_rect(center=(503, 610))
  screen.blit(text4, text_rect4)

  text5 = points_font.render(str(puntos_azul), True, (0, 0, 0))
  text_rect5 =text5.get_rect(center=(603, 610))
  screen.blit(text5, text_rect5)


  

  global G00
  global G01
  global G02
  global G10
  global G11
  global G12
  global G20
  global G21
  global G22
 
  G00 =pygame.draw.rect(screen, Black, (115, 60, 100, 100), 1)
 
  G01 = pygame.draw.rect(screen, Black, (300, 100, 100, 50), 1)
 
  G02 = pygame.draw.rect(screen, Black, (430, 50, 100, 100), 1)  
 
  G10 = pygame.draw.rect(screen, Black, (120, 290, 100, 100), 1)
   
  G11 = pygame.draw.rect(screen, Black, (230, 170, 160, 150), 1)
 
  G12 =pygame.draw.rect(screen, Black, (420, 200, 130, 130), 1)
 
  G20 =pygame.draw.rect(screen, Black, (170, 430, 100, 100), 1)
 
  G21 = pygame.draw.rect(screen, Black, (290, 400, 70, 130), 1)
 
  G22 = pygame.draw.rect(screen, Black, (370, 400, 100, 100), 1)
 
  grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
 
  pygame.display.update()
 
def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])
 
def checkGridX(grid):
  global puntos_rojo
  global RowMsg

  #Chequea las filas

  if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    
    print(RowMsg)
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
     
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
     
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100,670))
    screen.blit(text3, text_rect3)
 
  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)

  #Chequea las columnas
  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  #Chequea las diagonales
  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    puntos_rojo+=1
    RowMsg = "Gana el Rey Rojo."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Rojo.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
def checkGrid0(grid):
  global puntos_azul
 
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  #Checks The Collums
 
  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  #Checks Diagonals
 
  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
    screen.blit(text3, text_rect3)
 
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    puntos_azul+=1
    RowMsg = "Gana el Rey Azul."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Gana el Rey Azul.")
    print("Poder del Rey Rojo: ", puntos_rojo)
    print("Poder del Rey Azul: ", puntos_azul)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presione R para reiniciar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(100, 670))
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
                screen.blit(imp31, (125,70))
              else:
                screen.blit(imp32, (125,70))
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
                screen.blit(imp31, (305,70))
              else:
                screen.blit(imp32, (305,70))
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
                screen.blit(imp31, (430,50))
              else:
                screen.blit(imp32, (430,50))
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
                screen.blit(imp31, (130,270))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (130,270))
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
                screen.blit(imp31, (250,200))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (250,200))
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
                screen.blit(imp31, (430,200))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (430,200))
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
                screen.blit(imp31, (160,420))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp32, (160,420))
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
                screen.blit(imp31, (280,400))
                grid[row][col] = "X"
                Turn = False
               
              else:
                screen.blit(imp32, (280,400))
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
                screen.blit(imp31, (380,400))
                grid[row][col] = "X"
                Turn = False
                checkGridX(grid)
              else:
                screen.blit(imp32, (380,400))
               
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
               
              displayGrid(grid)
             
              pygame.display.flip()
              checkGridX(grid)
 
      if event.type == pygame.QUIT: #Checks whether you pressed the X button
        running = False
   
    text = font.render("", True, (0, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(100, 630))  # Get the rectangle for the text
   
    #text2 = font.render(RowMsg, True, (0, 0, 0))  # Render the text
    text_rect2 = text.get_rect(center=(100, 630))

    

    
   
    screen.blit(text, text_rect)
    pygame.display.flip()  # Update the screen
 
 
# Quit pygame
pygame.quit()