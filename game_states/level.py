import pygame
from entities.player import Player
from entities.enemy import Enemy
from entities.platform import Platform
from game_states.gameover import gameoverscreen

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Platformer Game')

def level():
    # Create game objects
    player = Player(100, 250)  
    enemy = Enemy(400, 500)
    platforms = [Platform(200, 550, 300, 10), Platform(450, 450, 300, 10), Platform(100, 350, 300, 10)]

    clock = pygame.time.Clock()

    # Gameloop
    running = True
    while running:
        screen.fill((0, 0, 0))  # background

        # update game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # player inputs
        player.inputs(platforms)

        # Draw entities
        player.draw(screen)  
        enemy.draw(screen) 
        enemy.update(player)  # make sure you pass the player object

        # Draw platforms
        for platform in platforms:
            platform.draw(screen)

        # Check if player has fallen off the screen
        if player.rect.top > screen.get_height():
            # Call game over screen and pass the screen object
            result = gameoverscreen(screen)

            # If retry, restart the level
            if result == "retry":
                level()
            return  # Exit current level function if quit or retry handled

        pygame.display.flip()  # Update screen
        clock.tick(60)  

    pygame.quit()
