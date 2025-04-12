import pygame
from entities.player import Player
from entities.enemy import Enemy
from entities.platform import Platform
from game_states.gameover import gameoverscreen
from entities.leafarmour import Leafarmour

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Platformer Game')

def level():
    # Create game objects
    player = Player(100, 250)
    enemies = [
        Enemy(400, 500),
        Enemy(900, 480),
        Enemy(1300, 500),
        Enemy(1600, 450)
    ]
    platforms = [
        Platform(200, 550, 300, 10),
        Platform(450, 450, 300, 10),
        Platform(100, 350, 200, 10),
        Platform(700, 450, 300, 10),
        Platform(950, 350, 200, 10),
        Platform(1100, 400, 200, 10),
        Platform(1350, 300, 300, 10),
        Platform(1350, 550, 300, 10),
        Platform(1650, 450, 200, 10),
        Platform(1850, 350, 300, 10)
    ]

    leafarmour = Leafarmour(700, 420)
    camera = {'x': 0, 'y': 0}

    clock = pygame.time.Clock()
    damage_cooldown = 1000
    last_hit_time = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.inputs(platforms)

        # Update camera to center on player
        camera['x'] = player.rect.centerx - screen.get_width() // 2
        camera['y'] = player.rect.centery - screen.get_height() // 2

        # Inside the main loop, after camera calculation
        for enemy in enemies:
            enemy.update(player, camera, screen.get_width(), screen.get_height())
            enemy.draw(screen, camera)


        # Collision damage check
        current_time = pygame.time.get_ticks()
        if player.rect.colliderect(enemy.rect):
            if current_time - last_hit_time > damage_cooldown:
                if player.has_leafarmour and player.shield_points > 0:
                    player.shield_points -= 1
                    print(f"Shield hit! Remaining shield: {player.shield_points}")
                    if player.shield_points <= 0:
                        player.has_leafarmour = False
                        print("Leafarmour shattered!")
                else:
                    player.health -= 1
                    print(f"Player HP: {player.health}")
                last_hit_time = current_time

        # drawing the platforms
        for platform in platforms:
            platform.draw(screen, camera)

        # drawing the player
        player.draw(screen, camera)

        # drawing the enemies
        # Inside the main loop, after camera calculation
        for enemy in enemies:
            enemy.update(player, camera, screen.get_width(), screen.get_height())
            enemy.draw(screen, camera)



        # Leafarmour draw
        if not leafarmour.collected:
            leafarmour.collect(player.rect, keys, player)
            leafarmour.draw(screen, camera)
        elif player.has_leafarmour:
            leafarmour.rect.topleft = (player.rect.centerx + 5, player.rect.top + 10)
            adjusted_rect = leafarmour.rect.move(-camera['x'], -camera['y'])
            screen.blit(leafarmour.image, adjusted_rect)

        # Health HUD
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_text, (10, 10))

        if player.has_leafarmour:
            shield_text = font.render(f"Shield: {player.shield_points}", True, (0, 255, 0))
            screen.blit(shield_text, (10, 50))

        # Game over checks
        if player.rect.top > screen.get_height():
            retry = gameoverscreen(screen)
            return level() if retry else None
        if player.health <= 0:
            retry = gameoverscreen(screen)
            return level() if retry else None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
