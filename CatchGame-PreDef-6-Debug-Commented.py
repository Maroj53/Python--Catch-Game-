import pygame                    #- Import the Pygame graphics module

##== INITIAL SETUP
#- Initialize Pygame
pygame.init()                        #- Initialize the module

#- Activate the graphical window
WindowWidth = 1200                        #- Set the width of the game window
WindowHeight = 1000                       #- Set the height of the game window
Window = pygame.display.set_mode ([WindowWidth, WindowHeight])    #- Activate the window
pygame.display.set_caption ("Catch game")        #- Set the window title

#- Prepare the timer
Clock = pygame.time.Clock()                #- Initialize the timing module

#- Initial variable setup
Stamina = 1000                    #- Set up stamina value (starts at 1000)
SprintBarX = Stamina              #- Set the sprint bar width equal to stamina (this will be visualized later)
Fps = 60                    #- Set the frames per second to 60
MainLoop = True                #- Main game loop flag, used to keep the game running

#- Initial classes setup
Zombiespawnlocationx = 1160                   #- Set the initial X position for the zombie spawn
Zombiespawnlocationy = 860                   #- Set the initial Y position for the zombie spawn
Playerspawnlocationx = 10                   #- Set the initial X position for the player spawn
Playerspawnlocationy = 10                   #- Set the initial Y position for the player spawn
ClassZombie = 1
ClassPlayer = 1
WalkInWalls = False                       #- A boolean flag for handling wall collisions (optional)

# Define the Wall class
class Wall:
  def __init__(self, Wallspawnlocationy, Wallspawnlocationx, sizex, sizey):
    self.Wallspawnlocationx = Wallspawnlocationx  #- Wall X position
    self.Wallspawnlocationy = Wallspawnlocationy  #- Wall Y position
    self.sizex = sizex  #- Wall width
    self.sizey = sizey  #- Wall height
    self.Surface2 = pygame.Surface([self.sizex, self.sizey], pygame.SRCALPHA, 32)  #- Create surface for the wall
    self.Surface2.fill([0, 200, 200])  #- Fill the wall with a color
    pygame.draw.rect(self.Surface2, [255, 0, 0], [self.Wallspawnlocationx, self.Wallspawnlocationy, self.sizex, self.sizey], 100)  #- Draw a red rectangle (the wall)
    self.WallRect2 = self.Surface2.get_rect(x=Wallspawnlocationx, y=Wallspawnlocationy)  #- Set the position of the wall

  def draw(self, Window):
    """ Drawing the wall into the window """
    Window.blit(self.Surface2, self.WallRect2)  #- Blit (draw) the wall on the screen

# Define the Player class
class Players:
  def __init__(self, centerY, centerX, WalkSpeed, size, Health):
    self.Health = Health  #- Zombie health
    self.centerX = centerX  #- Player's X position
    self.centerY = centerY  #- Player's Y position
    self.WalkSpeed = WalkSpeed  #- Player's walk speed
    self.size = size  #- Player's size
    self.resetspeed = WalkSpeed
    self.Surface2 = pygame.Surface([self.size, self.size], pygame.SRCALPHA, 32)  #- Create surface for the player
    self.Surface2.fill([200, 200, 200])  #- Fill the player with a color
    pygame.draw.circle(self.Surface2, [255, 0, 0], [self.centerX, self.centerY], self.size)  #- Draw a red circle (the player)
    self.PlayerRect2 = self.Surface2.get_rect(x=Playerspawnlocationx, y=Playerspawnlocationy)  #- Set the position of the player

  def draw(self, Window):
    """ Drawing the player into the window """
    Window.blit(self.Surface2, self.PlayerRect2)  #- Blit (draw) the player on the screen

     
     

# Define the Zombie class
class Zombie:
  def __init__(self, centerY, centerX, WalkSpeed, size1): 
    self.centerX = centerX  #- Zombie's X position
    self.centerY = centerY  #- Zombie's Y position
    self.WalkSpeed = WalkSpeed  #- Zombie's walking speed
    self.size1 = size1  #- Zombie's size
    self.resetspeed = WalkSpeed
    self.Surface = pygame.Surface([self.size1, self.size1], pygame.SRCALPHA, 32)  #- Create surface for the zombie
    self.Surface.fill([200, 200, 200])  #- Fill the zombie with a color
    pygame.draw.circle(self.Surface, [255, 0, 0], [self.centerX, self.centerY], self.size1)  #- Draw a red circle (the zombie)
    self.ZombieRect = self.Surface.get_rect(x=Zombiespawnlocationx, y=Zombiespawnlocationy)  #- Set the position of the zombie

  def draw(self, Window):
    """ Drawing the zombie into the window """
    Window.blit(self.Surface, self.ZombieRect)  #- Blit (draw) the zombie on the screen


# Initialize the objects for zombies and players
Zombie1 = Zombie(Zombiespawnlocationx, Zombiespawnlocationy, 8, 10)  #- Initialize Zombie1
Zombie2 = Zombie(Zombiespawnlocationx, Zombiespawnlocationy, 7, 15)  #- Initialize Zombie2
Player1 = Players(Playerspawnlocationx, Playerspawnlocationy, 6, 15,700)  #- Initialize Player1
Player2 = Players(Playerspawnlocationx, Playerspawnlocationy, 5, 20,1000)  #- Initialize Player2
Wall1 = Wall(400, 300, 500, 100)  #- Initialize Wall1

##== MAIN GAME LOOP
while MainLoop:
  #- Handle user input (keyboard events, etc.)
  for event in pygame.event.get():  #- Handle events (like quit)
    if event.type == pygame.QUIT:  #- If the quit event is triggered (e.g., window close button pressed)
      MainLoop = False  #- Exit the main loop and end the game

  # Debug prints to check positions and stamina values
  print("Player coordinates", Player1.PlayerRect2.x, Player1.PlayerRect2.y)  #- Print Player1's X and Y position
  print("Zombie coordinates", Zombie1.ZombieRect.x, Zombie1.ZombieRect.y)  #- Print Zombie1's X and Y position
  print("Players stamina", Stamina)  #- Print Player's Stamina value
  
  #- Drawing
  Window.fill([0, 0, 0])  #- Fill the window with black color (background)

  #- Program function that manages all game logic
  def Program(PlayerClasses1, Zombiesclasses1, SprintBarX, OneWayWall, WalkInWalls):
    global Stamina
    SprintBarX = Stamina  #- Update the SprintBarX based on the player's stamina

    # If the zombie collides with the player, reduce the zombie's health
    if Zombiesclasses1.ZombieRect.colliderect(PlayerClasses1.PlayerRect2):
        PlayerClasses1.Health = PlayerClasses1.Health - 10

    # If stamina is full, make sure it doesn't exceed 1000
    if Stamina >= 1000:
        Stamina = 1000
    
    # Handle player and zombie collisions with the wall
    if PlayerClasses1.PlayerRect2.colliderect(OneWayWall.WallRect2):
        PlayerClasses1.PlayerRect2.y = PlayerClasses1.PlayerRect2.y + 10  #- Prevent player from walking through wall
        
    if Zombiesclasses1.ZombieRect.colliderect(OneWayWall.WallRect2):
        Zombiesclasses1.ZombieRect.y = Zombiesclasses1.ZombieRect.y + 10  #- Prevent zombie from walking through wall


    # Optional: Allow characters to walk through walls (wrap around)
    if WalkInWalls == True:  
      if PlayerClasses1.PlayerRect2.x >= WindowWidth:
          PlayerClasses1.PlayerRect2.x = 0
      if PlayerClasses1.PlayerRect2.x <= 0 - PlayerClasses1.size:
          PlayerClasses1.PlayerRect2.x = WindowWidth

      if PlayerClasses1.PlayerRect2.y >= WindowHeight:
          PlayerClasses1.PlayerRect2.y = 0 - PlayerClasses1.size
      if PlayerClasses1.PlayerRect2.y <= -1 - PlayerClasses1.size:
          PlayerClasses1.PlayerRect2.y = WindowHeight

      if Zombiesclasses1.ZombieRect.x >= WindowWidth:
          Zombiesclasses1.ZombieRect.x = 0
      if Zombiesclasses1.ZombieRect.x <= 0 - Zombiesclasses1.size1:
          Zombiesclasses1.ZombieRect.x = WindowWidth

      if Zombiesclasses1.ZombieRect.y >= WindowHeight:
          Zombiesclasses1.ZombieRect.y = 0 - Zombiesclasses1.size1
      if Zombiesclasses1.ZombieRect.y <= -1 - Zombiesclasses1.size1:
          Zombiesclasses1.ZombieRect.y = WindowHeight  
    else:
      # If no walk-through walls, constrain movement within window boundaries
      if PlayerClasses1.PlayerRect2.x <= 0:
          PlayerClasses1.PlayerRect2.x = 0
      if PlayerClasses1.PlayerRect2.x >= WindowWidth - PlayerClasses1.size:
          PlayerClasses1.PlayerRect2.x = WindowWidth - PlayerClasses1.size
      if PlayerClasses1.PlayerRect2.y <= 0:
          PlayerClasses1.PlayerRect2.y = 0
      if PlayerClasses1.PlayerRect2.y >= WindowHeight - PlayerClasses1.size:
          PlayerClasses1.PlayerRect2.y = WindowHeight - PlayerClasses1.size

      if Zombiesclasses1.ZombieRect.x <= 0:
          Zombiesclasses1.ZombieRect.x = 0
      if Zombiesclasses1.ZombieRect.x >= WindowWidth - Zombiesclasses1.size1:
          Zombiesclasses1.ZombieRect.x = WindowWidth - Zombiesclasses1.size1
      if Zombiesclasses1.ZombieRect.y <= 0:
          Zombiesclasses1.ZombieRect.y = 0
      if Zombiesclasses1.ZombieRect.y >= WindowHeight - Zombiesclasses1.size1:
          Zombiesclasses1.ZombieRect.y = WindowHeight - Zombiesclasses1.size1
      
      #Drawing

      PlayerClasses1.draw(Window)  #- Draw Player

      Zombiesclasses1.draw(Window)  #- Draw Zombie

      OneWayWall.draw(Window)  #- Draw OneWayWall     
    
      pygame.draw.rect (Window, [255,0,0], (100,WindowHeight-100,SprintBarX,10))
      pygame.draw.rect (Window, [0,255,0], (100,WindowHeight-50,PlayerClasses1.Health,10))

    #- Control player movement
      Keyboard = pygame.key.get_pressed()	

      if Keyboard[pygame.K_w]:				#Player movement up
          PlayerClasses1.PlayerRect2.y = PlayerClasses1.PlayerRect2.y - PlayerClasses1.WalkSpeed
      Keyboard = pygame.key.get_pressed()			
      if Keyboard[pygame.K_s]:				#Player movement down
          PlayerClasses1.PlayerRect2.y = PlayerClasses1.PlayerRect2.y + PlayerClasses1.WalkSpeed
      Keyboard = pygame.key.get_pressed()			
      if Keyboard[pygame.K_a]:				#Player movement left
          PlayerClasses1.PlayerRect2.x = PlayerClasses1.PlayerRect2.x - PlayerClasses1.WalkSpeed
      Keyboard = pygame.key.get_pressed()			
      if Keyboard[pygame.K_d]:				#Player movement right
          PlayerClasses1.PlayerRect2.x = PlayerClasses1.PlayerRect2.x + PlayerClasses1.WalkSpeed

      if Keyboard[pygame.K_UP]:				#Zombie movement up
          Zombiesclasses1.ZombieRect.y = Zombiesclasses1.ZombieRect.y - Zombiesclasses1.WalkSpeed
      Keyboard = pygame.key.get_pressed()			
      if Keyboard[pygame.K_DOWN]:				#Zombie movement down
          Zombiesclasses1.ZombieRect.y = Zombiesclasses1.ZombieRect.y + Zombiesclasses1.WalkSpeed
      Keyboard = pygame.key.get_pressed()			
      if Keyboard[pygame.K_LEFT]:				#Zombie movement left
          Zombiesclasses1.ZombieRect.x = Zombiesclasses1.ZombieRect.x - Zombiesclasses1.WalkSpeed
      Keyboard = pygame.key.get_pressed()			
      if Keyboard[pygame.K_RIGHT]:			#Zombie movement right
          Zombiesclasses1.ZombieRect.x = Zombiesclasses1.ZombieRect.x + PlayerClasses1.WalkSpeed

      if  PlayerClasses1 == Player2:    
            if Keyboard[pygame.K_LSHIFT] and Stamina > 0:                #- if 'Left Shift' key is pressed
                PlayerClasses1.WalkSpeed   = 10
                Stamina = Stamina - 10
            else:
                PlayerClasses1.WalkSpeed = PlayerClasses1.resetspeed
  

      if  PlayerClasses1 == Player1:    
            if Keyboard[pygame.K_LSHIFT] and Stamina > 0:                #- if 'Left Shift' key is pressed
                PlayerClasses1.WalkSpeed   = -30
                Stamina = Stamina - 75
            else:
                PlayerClasses1.WalkSpeed = PlayerClasses1.resetspeed


  #- Update the window display
  Program(Player1, Zombie2, SprintBarX, Wall1, WalkInWalls)  #- Call the game logic



  #- Update the window
  pygame.display.flip()

  #- Control the game framerate
  Clock.tick(Fps)  #- Limit the frame rate to 60 FPS

pygame.quit()  #- Quit Pygame when the game loop ends
