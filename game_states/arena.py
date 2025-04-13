import pygame
from entities.player import Player
from entities.platform import Platform
from game_states.gameover import gameoverscreen


# You can create/import a boss entity later, placeholder for now

pygame.init()

def arena(screen):
    player = Player(100, 450)
    platforms = [
        Platform(100, 550, 800, 10), 
    ]

    camera = {'x': 0, 'y': 0}
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((10, 10, 30))  # Darker background for boss fight
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.inputs(platforms)

        camera['x'] = player.rect.centerx - screen.get_width() // 2
        camera['y'] = player.rect.centery - screen.get_height() // 2


        for platform in platforms:
            platform.draw(screen, camera)

        player.draw(screen, camera)

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
