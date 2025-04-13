import pygame
from entities.player import Player
from entities.platform import Platform
from entities.boss import Ant  # ✅ Import the boss
from game_states.gameover import gameoverscreen

pygame.init()

def arena(screen):
    player = Player(100, 450)
    platforms = [
        Platform(100, 550, 1000, 10), 
        Platform(100, 0, 10, 1000),
    ]

    boss = Ant(500, 200)  # ✅ Spawn the boss
    camera = {'x': 0, 'y': 0}
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((10, 10, 30))  # Boss arena background
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input and movement
        player.inputs(platforms)

        # ✅ Update boss logic (attack, movement, projectile handling)
        boss.update(player, platforms)

        # ✅ Update camera based on player
        camera['x'] = player.rect.centerx - screen.get_width() // 2
        camera['y'] = player.rect.centery - screen.get_height() // 2

        # Draw platforms
        for platform in platforms:
            platform.draw(screen, camera)

        # Draw entities
        player.draw(screen, camera)
        boss.draw(screen, camera)  # ✅ Draw boss and HP bar

        # HUD
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_text, (10, 10))

        if player.has_leafarmour:
            shield_text = font.render(f"Shield: {player.shield_points}", True, (0, 255, 0))
            screen.blit(shield_text, (10, 50))

        # Game over condition
        if player.health <= 0 or player.rect.top > screen.get_height():
            retry = gameoverscreen(screen)
            return arena(screen) if retry else None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
