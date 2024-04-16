import pygame

pygame.init()

# Variables to set the size of the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creates the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the player object
# Rect is an object that can be drawn on
player = pygame.Rect((300,250,50,50))

run = True
while run == True:
    # Background colour is set to prevent the screen from being covered by the player
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()
    # Check if 'a' is pressed and player is within left boundary
    if key[pygame.K_a] and player.left > 0:  
        player.move_ip(-1,0)
        # Check if 'd' is pressed and player is within right boundary
    elif key[pygame.K_d] and player.right < SCREEN_WIDTH:  
        player.move_ip(1,0)
        # Check if 'w' is pressed and player is within top boundary
    elif key[pygame.K_w] and player.top > 0:  
        player.move_ip(0,-1)
        # Check if 's' is pressed and player is within bottom boundary
    elif key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:  
        player.move_ip(0,1)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
