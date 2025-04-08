import pygame
from entities.player import Player
from entities.enemy import Enemy
from entities.platform import Platform
from game_states.main_menu import MainMenu

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Platformer Game')

def level():
    # Create game objects
    player = Player(100, 250)  
    enemy = Enemy(400, 500)
    platforms = [Platform(200, 550, 300, 10), Platform(450, 450, 300, 10), Platform(100, 350, 300, 10)]

    clock = pygame.time.Clock()
    main_menu = MainMenu() 

    # Gameloop
    running = True
    while running:
        screen.fill((0, 0, 0))  #background

        #  update game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update entities
        player.update(platforms)
        player.update(platforms)

        # Draw entities
        player.draw(screen)  
        enemy.draw(screen) 

        # Draw platforms
        for platform in platforms:
            platform.draw(screen)

        pygame.display.flip()  # Updating screen
        clock.tick(60)  

    pygame.quit()

