#test
#battle ships
import pygame

# Initialize pygame
pygame.init()

# Set up the screen
Black = (0,0,0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 252))

#Load The imagesz
imp = pygame.image.load("Cross.png")
imp = pygame.transform.scale(imp, (100,100))
imp2 = pygame.image.load("Nought.png")
imp2 = pygame.transform.scale(imp2, (100,100))

#initilize the font
font = pygame.font.SysFont("Arial", 32)

#CONTADOR DE PUNTOS
class ContadorDePuntos:
    def __init__(self):
        self.puntos = 0
        print("Puntos iniciales:", self.obtener_puntos())

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad
        print("Puntos después de sumar:", self.obtener_puntos())

    def restar_puntos(self, cantidad):
        self.puntos -= cantidad
        print("Puntos después de restar:", self.obtener_puntos())

    def reiniciar_puntos(self):
        self.puntos = 0
        print("Puntos después de reiniciar:", self.obtener_puntos())

    def obtener_puntos(self):
        return self.puntos

def ejecutar_programa():
    contador = ContadorDePuntos()

    while True:
        print("\n1. Sumar puntos")
        print("2. Restar puntos")
        print("3. Reiniciar puntos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            cantidad = int(input("Ingrese la cantidad de puntos a sumar: "))
            contador.sumar_puntos(cantidad)
        elif opcion == '2':
            cantidad = int(input("Ingrese la cantidad de puntos a restar: "))
            contador.restar_puntos(cantidad)
        elif opcion == '3':
            contador.reiniciar_puntos()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Llamada a la función para ejecutar el programa
ejecutar_programa()

def RedrawGameWindow():

  screen.fill((255, 255, 255))
  
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
    RowMsg = "Tres X seguidas."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
    #CONTADOR
    ejecutar_programa
   
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
      
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    RowMsg = "Tres X seguidas."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    RowMsg = "Tres X seguidas"
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres X seguidas")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  #Checks The Collums

  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    RowMsg = "Tres X en una columna."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres X en una columna-")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    RowMsg = "Tres X en una columna"
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres X en una columna")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    RowMsg = "Tres X en una columna."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres X en una columna.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks Diagonals

  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    RowMsg = "Tres X en una diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres X en una diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
    #CONTADOR
   
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    RowMsg = "Tres X en una diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres X en una diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
    #CONTADOR

def checkGrid0(grid):
  
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    RowMsg = "Tres O seguidos."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O seguidos.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    RowMsg = "Tres O seguidos."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O seguidos.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    RowMsg = "Tres O seguidos."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O seguidos.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks The Collums

  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    RowMsg = "Tres O en una columna."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O en una columna.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    RowMsg = "Tres O en una columna."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O en una columna.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    RowMsg = "Tres O en una columna."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O en una columna.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks Diagonals

  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    RowMsg = "Tres O en diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O en diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    RowMsg = "Tres O en diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Tres O en diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Presionar R para restaurar", True, (0, 0, 0))  # Render the text
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
              print("Pare")
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
    
    text = font.render("Ta Te Ti ", True, (0, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(screen_width/2, 100))  # Get the rectangle for the text
    
    #text2 = font.render(RowMsg, True, (0, 0, 0))  # Render the text
    text_rect2 = text.get_rect(center=(350, 500))
    
    screen.blit(text, text_rect)
    pygame.display.flip()  # Update the screen

  
# Quit pygame
pygame.quit()
