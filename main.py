import random
import math

import pygame
from pygame import mixer
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

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)



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

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x,y):
    showScore = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(showScore, (x,y))

#Game over text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_text, (200,250))


# Enemy 
enemy_icon = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_icon.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemy_icon[i],(x,y))

# Missile 
missile_icon = pygame.image.load('missile.png')
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 2
missile_state = 'ready'

def fire_missile(x,y):
    global missile_state
    missile_state = "fire"
    screen.blit(missile_icon, (x+16,y+10))

def isCollision(enemyX,enemyY,missileX,missileY):
    distance = math.sqrt((math.pow(enemyX - missileX,2)) + (math.pow(enemyY - missileY, 2)))
    if distance < 27:
        return True
    else:
        return False

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
                    missile_sound = mixer.Sound('laser.wav')
                    missile_sound.play()
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
    for i in range(num_of_enemies):

        #Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            show_game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX[i] = 736
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

           #Collision
        collision = isCollision(enemyX[i], enemyY[i], missileX, missileY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            missileY = 480
            missile_state = 'ready'
            score += 10
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)
        
        
    #Missle movement
    if missileY <=0:
        missileY = 480
        missile_state = 'ready'

    if missile_state == "fire":
        fire_missile(missileX,missileY)
        missileY -= missileY_change

   
 

    playerX += playerX_change
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
