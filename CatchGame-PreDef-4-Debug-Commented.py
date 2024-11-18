import pygame                    #- import the graphics module


##== INITIAL SETUP
#- Initialize Pygame
pygame.init()                        #- initialize the module

#- Activate the graphical window
WindowWidth = 1200                        #- fixed width and height of the game window
WindowHeight = 900
Window = pygame.display.set_mode ([WindowWidth, WindowHeight])    #- activate the window
pygame.display.set_caption ("Catch game")        #- set the window title


#- Prepare the timer
Clock = pygame.time.Clock()                #- initialize the timing module

#- Initial variable setup

Stamina = 1000                    #- Setting up variables
SprintBarX = Stamina                          #- Setting up variables

Fps = 60                    #- Frames per second
MainLoop = True                #- main loop flag to keep the game running

#- Initial classes setup

Playerspawnlocationx = 1160                   #- Setting up variables
Playerspawnlocationy = 860                  #- Setting up variables
Zombiespawnlocationx = 10                   #- Setting up variables
Zombiespawnlocationy = 10                   #- Setting up variables
ClassPlayer = 0
ClassZombie = 0


class Zombies:
  def __init__ (self, centerY, centerX, WalkSpeed, size):
    self.centerX = centerX   
    self.centerY = centerY
    self.WalkSpeed = WalkSpeed  
    self.size = size  #[Self.Face.Size]
    self.Surface2 = pygame.Surface ([self.size,self.size], pygame.SRCALPHA, 32)    #- Game surface
    self.Surface2.fill ([200,200,200])                    #- fill surface with a color  
    pygame.draw.circle (self.Surface2, [255,0,0], [self.centerX, self.centerY], self.size)        #- draw a circle 
    self.ZombieRect2 = self.Surface2.get_rect (x=Zombiespawnlocationx, y=Zombiespawnlocationy)        #- set the position of the top-left corner
  def draw (self, Window):
    """ Drawing into the window
        parameters:
          Window - surface to perform the drawing [pygame.Surface] """
    Window.blit (self.Surface2, self.ZombieRect2)  


  
    

class Player:
  def __init__ (self, centerY, centerX, WalkSpeed, size,Health):
    self.Health = Health   
    self.centerX = centerX   
    self.centerY = centerY
    self.WalkSpeed = WalkSpeed   
    self.size = size   
    self.Surface = pygame.Surface ([self.size,self.size], pygame.SRCALPHA, 32)    #- Game surface
    self.Surface.fill ([200,200,200])                    #- fill surface with a color
    pygame.draw.circle (self.Surface, [255,0,0], [self.centerX, self.centerY], self.size)        #- draw a circle 
    self.PlayerRect = self.Surface.get_rect (x=Playerspawnlocationx, y=Playerspawnlocationy)        #- set the position of the top-left corner
  def draw (self, Window):
    """ Drawing into the window
        parameters:
          Window - surface to perform the drawing [pygame.Surface] """
    Window.blit (self.Surface, self.CircleRect)      
    

Player1 = Player(Playerspawnlocationx, Playerspawnlocationy, 4, 10,1000) #- Note: 'Player1' is now created from the 'Player' class
Player2 = Player(Playerspawnlocationx, Playerspawnlocationy, 4, 10,700) #- Note: 'Player2' is now created from the 'Player' class

Zombie1 = Zombies(Zombiespawnlocationx, Zombiespawnlocationy, 5, 20)  #- Note: 'Zombie1' is now created from the 'Zombies' class
Zombie2 = Zombies(Zombiespawnlocationx, Zombiespawnlocationy, 5, 20)  #- Note: 'Zombie2' is now created from the 'Zombies' class

Playersclasses = [Player1,Player2]	
Zombiesclasses = [Zombie1,Zombie2]	

##== MAIN GAME LOOP
while MainLoop:

  #- Handle user input
  for event in pygame.event.get():            #- handle input events (keyboard, mouse)
    if event.type == pygame.QUIT:            #- quit program if requested (Alt+F4, close button)
      MainLoop = False
  

  #Debug

  print("Zombie coordinates",Zombie1.ZombieRect2.x,Zombie1.ZombieRect2.y)  #- Debugging print of Zombie1's X and Y position
  print("Player coordinates",Player1.PlayerRect.x,Player1.PlayerRect.y)  #- Debugging print of Player1's X and Y position
  print("Zombies stamina",Stamina)  #- Debugging print of Zombie's Stamina
  
  #- Drawing
  Window.fill ([0,0,0])                    #- fill the window with black color

  #- Program
  SprintBarX = Stamina                          #- Setting up variables
  
  if Player1.PlayerRect.colliderect (Zombie1.ZombieRect2):
      Player1.Health = Player1.Health - 10
      
  if Stamina >= 1000:
      Stamina = 1000
      
      
  if Zombiesclasses[ClassZombie].ZombieRect2.x >= WindowWidth-Zombiesclasses[ClassZombie].size:
    Zombiesclasses[ClassZombie].ZombieRect2.x = WindowWidth-Zombiesclasses[ClassZombie].size
  if Zombiesclasses[ClassZombie].ZombieRect2.x <= 0:
    Zombiesclasses[ClassZombie].ZombieRect2.x = 0
  if Zombiesclasses[ClassZombie].ZombieRect2.y >= WindowHeight-Zombiesclasses[ClassZombie].size:
    Zombiesclasses[ClassZombie].ZombieRect2.y = WindowHeight-Zombiesclasses[ClassZombie].size
  if Zombiesclasses[ClassZombie].ZombieRect2.y <= 0:
    Zombiesclasses[ClassZombie].ZombieRect2.y = 0

  if Playersclasses[ClassPlayer].PlayerRect.x >= WindowWidth-Playersclasses[ClassPlayer].size*2:
    Playersclasses[ClassPlayer].PlayerRect.x = WindowWidth-Playersclasses[ClassPlayer].size*2
  if Playersclasses[ClassPlayer].PlayerRect.x <= 0:
    Playersclasses[ClassPlayer].PlayerRect.x = 0
  if Playersclasses[ClassPlayer].PlayerRect.y >= WindowHeight-Playersclasses[ClassPlayer].size*2:
    Playersclasses[ClassPlayer].PlayerRect.y = WindowHeight-Playersclasses[ClassPlayer].size*2
  if Playersclasses[ClassPlayer].PlayerRect.y <= 0:
    Playersclasses[ClassPlayer].PlayerRect.y = 0

  Window.blit (Player1.Surface, Player1.PlayerRect)  #- draw the player on the screen
  Window.blit (Zombie1.Surface2, Zombie1.ZombieRect2)  #- draw the zombie on the screen
  
  pygame.draw.rect (Window, [255,0,0], (100,WindowHeight-100,SprintBarX,10))
  pygame.draw.rect (Window, [0,255,0], (100,WindowHeight-50,Player1.Health,10))
  
  #- Controls
  KeyboardState = pygame.key.get_pressed()            #- get the state of the keyboard

  if KeyboardState[pygame.K_RIGHT]:                #- if right arrow key is pressed
    Player1.PlayerRect.x = Player1.PlayerRect.x + Player1.WalkSpeed        
  if KeyboardState[pygame.K_LEFT]:                #- if left arrow key is pressed
    Player1.PlayerRect.x = Player1.PlayerRect.x - Player1.WalkSpeed            
  if KeyboardState[pygame.K_UP]:                #- if up arrow key is pressed
    Player1.PlayerRect.y = Player1.PlayerRect.y - Player1.WalkSpeed        
  if KeyboardState[pygame.K_DOWN]:                #- if down arrow key is pressed
    Player1.PlayerRect.y = Player1.PlayerRect.y + Player1.WalkSpeed        
    
  if KeyboardState[pygame.K_d]:                #- if 'd' key is pressed
    Zombie1.ZombieRect2.x = Zombie1.ZombieRect2.x + Zombie1.WalkSpeed        
  if KeyboardState[pygame.K_a]:                #- if 'a' key is pressed
    Zombie1.ZombieRect2.x = Zombie1.ZombieRect2.x - Zombie1.WalkSpeed        
  if KeyboardState[pygame.K_w]:                #- if 'w' key is pressed
    Zombie1.ZombieRect2.y = Zombie1.ZombieRect2.y - Zombie1.WalkSpeed        
  if KeyboardState[pygame.K_s]:                #- if 's' key is pressed
    Zombie1.ZombieRect2.y = Zombie1.ZombieRect2.y + Zombie1.WalkSpeed  

  if KeyboardState[pygame.K_LSHIFT] and Stamina > 0:                #- if 'Left Shift' key is pressed
    Zombie1.WalkSpeed   = 6
    Stamina = Stamina - 10
  else: 
    Zombie1.WalkSpeed   = 3                         #- Sprint Ability
    
    
  pygame.display.flip()                    #- update the screen with the new drawing

  #- Time delay
  Clock.tick (Fps)                    #- delay the loop according to the set FPS (frames per second)
  
  
  #Notes:
  #     That point of one zombie being just a circle that is cut off is intencional. DO NOT CORRECT MY PROGRAM
  #     Plans: Start screen and End screen , More Classes
