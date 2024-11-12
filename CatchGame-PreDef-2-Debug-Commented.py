import pygame                    #- import the graphics module


##== INITIAL SETUP
#- Initialize Pygame
pygame.init()                        #- initialize the module

#- Activate the graphical window
WindowWidth = 800                        #- fixed width and height of the game window
WindowHeight = 600

x1 = 10
y1 = 10
Window = pygame.display.set_mode ([WindowWidth, WindowHeight])    #- activate the window
pygame.display.set_caption ("Pygame Template")        #- set the window title

#- Prepare the timer
Clock = pygame.time.Clock()                #- initialize the timing module

#- Initial variable setup
Fps = 60                    #- number of game ticks per second
MainLoop = True                #- main loop flag to keep the game running

#- Initial classes setup
class Zombies:
  def __init__ (self, centerY, centerX, WalkSpeed, size):
    self.centerX = centerX   
    self.centerY = centerY
    self.WalkSpeed = WalkSpeed  
    self.size = size  #[Self.Face.Size]
    self.Surface2 = pygame.Surface ([20,20], pygame.SRCALPHA, 32)    #- Game surface
    self.Surface2.fill ([200,200,200])                    #- fill surface with a color  
    pygame.draw.circle (self.Surface2, [255,0,0], [self.centerX, self.centerY], self.size)        #- draw a circle 
    self.ZombieRect2 = self.Surface2.get_rect (x=10, y=10)        #- set the position of the top-left corner
  def draw (self, Window):
    """ Drawing into the window
        parameters:
          Window - surface to perform the drawing [pygame.Surface] """
    Window.blit (self.Surface2, self.ZombieRect2)  


  
    

class Player:
  def __init__ (self, centerY, centerX, WalkSpeed, size):
    self.centerX = centerX   
    self.centerY = centerY
    self.WalkSpeed = WalkSpeed   
    self.size = size   
    self.Surface = pygame.Surface ([20,20], pygame.SRCALPHA, 32)    #- Game surface
    self.Surface.fill ([200,200,200])                    #- fill surface with a color
    pygame.draw.circle (self.Surface, [255,0,0], [self.centerX, self.centerY], self.size)        #- draw a circle 
    self.PlayerRect = self.Surface.get_rect (x=10, y=10)        #- set the position of the top-left corner
  def draw (self, Window):
    """ Drawing into the window
        parameters:
          Window - surface to perform the drawing [pygame.Surface] """
    Window.blit (self.Surface, self.CircleRect)      

Player1 = Player(x1, y1, 5, 10,)
Zombie1 = Zombies(x1, y1, 3, 20)  #- Note: 'Zombie1' is now created from the 'Zombies' class


##== MAIN GAME LOOP
while MainLoop:

  #- Handle user input
  for event in pygame.event.get():            #- handle input events (keyboard, mouse)
    if event.type == pygame.QUIT:            #- quit program if requested (Alt+F4, close button)
      MainLoop = False
      
  #Debug

  print("Zombie coordinates",Zombie1.ZombieRect2.x,Zombie1.ZombieRect2.y)  #- Debugging print of Zombie1's X and Y position
  print("Player coordinates",Player1.PlayerRect.x,Player1.PlayerRect.y)  #- Debugging print of Player1's X and Y position
  
  #- Drawing
  Window.fill ([0,0,0])                    #- fill the window with black color

  if Zombie1.ZombieRect2.x >= WindowWidth-Zombie1.size:
    Zombie1.ZombieRect2.x = WindowWidth-Zombie1.size
  if Zombie1.ZombieRect2.x <= 0:
    Zombie1.ZombieRect2.x = 0
  if Zombie1.ZombieRect2.y >= WindowHeight-Zombie1.size:
    Zombie1.ZombieRect2.y = WindowHeight-Zombie1.size
  if Zombie1.ZombieRect2.y <= 0:
    Zombie1.ZombieRect2.y = 0

  if Player1.PlayerRect.x >= WindowWidth-Player1.size*2:
    Player1.PlayerRect.x = WindowWidth-Player1.size*2
  if Player1.PlayerRect.x <= 0:
    Player1.PlayerRect.x = 0
  if Player1.PlayerRect.y >= WindowHeight-Player1.size*2:
    Player1.PlayerRect.y = WindowHeight-Player1.size*2
  if Player1.PlayerRect.y <= 0:
    Player1.PlayerRect.y = 0

  Window.blit (Player1.Surface, Player1.PlayerRect)  #- draw the player on the screen
  Window.blit (Zombie1.Surface2, Zombie1.ZombieRect2)  #- draw the zombie on the screen
  
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
  pygame.display.flip()                    #- update the screen with the new drawing

  #- Time delay
  Clock.tick (Fps)                    #- delay the loop according to the set FPS (frames per second)
  
  
  #Notes:
  #     That point of one zombie being just a circle that is cut off is intencional. DO NOT CORRECT MY PROGRAM
