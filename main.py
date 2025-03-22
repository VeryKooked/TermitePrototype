import pygame
from entities.player import Player
from entities.enemy import Enemy
from entities.platform import Platform
from game_states.camera import Camera

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Adventure")

# Create game objects
player = Player(100, 500)
enemy = Enemy(400, 500)
platforms = [Platform(200, 550, 300, 20), Platform(600, 450, 300, 20), Platform(100, 350, 300, 20)]

# Initialize Camera
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((135, 206, 235))  # Sky blue background

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    player.move(keys, platforms)
    
    # Enemy movement
    enemy.move(platforms)

    # Update Camera to follow the player
    camera.update(player)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (139, 69, 19), camera.apply_rect(platform.rect))  # Brown platforms

    # Draw entities with camera applied
    player.draw(screen, camera)
    enemy.draw(screen, camera)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()