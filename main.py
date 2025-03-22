import pygame
from entities.platform import Platform
from entities.player import Player
from entities.enemy import Enemy

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Create platforms
    platforms = [
        Platform(100, 500, 200, 20),  # x, y, width, height
        Platform(400, 400, 200, 20),
        Platform(700, 300, 200, 20)
    ]

    # Create player and enemy
    player = Player(150, 450)  # Start player on a platform
    enemy = Enemy(600, 350)    # Start enemy on a platform

    # Main game loop
    running = True
    while running:
        screen.fill((135, 206, 235))  # Sky blue background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Move the player and enemies
        player.move(keys, platforms)
        enemy.move(platforms)

        # Draw platforms, player, and enemies
        for platform in platforms:
            platform.draw(screen)
        player.draw(screen)
        enemy.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
