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
    damage_cooldown = 1000  # milliseconds
    last_hit_time = 0

    # Gameloop
    running = True
    while running:
        screen.fill((0, 0, 0))  # background

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player inputs
        player.inputs(platforms)

        # Update and draw enemy
        enemy.update(player)
        enemy.draw(screen)

        # Draw player
        player.draw(screen)

        # Collision damage check
        current_time = pygame.time.get_ticks()
        if player.rect.colliderect(enemy.rect):
            if current_time - last_hit_time > damage_cooldown:
                player.health -= 1
                print(f"Player HP: {player.health}")
                last_hit_time = current_time

        # Draw platforms
        for platform in platforms:
            platform.draw(screen)

        # Display player's health
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_text, (10, 10))

        # Check if player fell off screen
        if player.rect.top > screen.get_height():
            retry = gameoverscreen(screen)
            if retry:
                return level()
            else:
                running = False

        # Game over when health is 0
        if player.health <= 0:
            retry = gameoverscreen(screen)
            if retry:
                return level()
            else:
                running = False

        pygame.display.flip()  # Updating screen
        clock.tick(60)  

    pygame.quit()
