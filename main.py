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
enemyX_change = 0.3
enemyY_change = 40

def enemy(x,y):
    screen.blit(enemy_icon,(x,y))

# Missile 
missile_icon = pygame.image.load('missile.png')
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 3
missile_state = 'ready'

def fire_missile(x,y):
    global missile_state
    missile_state = "fire"
    screen.blit(missile_icon, (x+16,y+10))


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
            if event.key == pygame.K_SPACE:
                if missile_state == 'ready':
                    missileX = playerX
                    fire_missile(missileX,missileY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

    # Check if the player has gone off the screen
    if playerX < -32:
        playerX = 800
    elif playerX > 832:
        playerX = 0

    #Move the enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX = 736
        enemyX_change = -0.3
        enemyY += enemyY_change
    
    #Missle movement
    if missileY <=0:
        missileY = 480
        missile_state = 'ready'

    if missile_state == "fire":

        fire_missile(missileX,missileY)
        missileY -= missileY_change

    playerX += playerX_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
