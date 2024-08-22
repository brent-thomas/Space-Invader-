import pygame
import random
#Init pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Set title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#load background image
background = pygame.image.load('space_background.jpg')

# Create a transparent surface
overlay = pygame.Surface((800, 600))  
overlay.set_alpha(130)  
overlay.fill((0, 0, 0))  


# Player 
player_icon = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(player_icon,(x,y))

# Enemy 
enemy_icon = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0
enemyY_change = 0

def enemy(x,y):
    screen.blit(enemy_icon,(x,y))

    

#Game loop
running = True
while running:
    #set screen color
    screen.blit(background, (0, 0)) 
    screen.blit(overlay, (0, 0))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if keystoke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                 playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

    # Check if the player has gone off the screen
    if playerX < -32:
        playerX = 800
    elif playerX > 832:
        playerX = 0
    
    playerX += playerX_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
