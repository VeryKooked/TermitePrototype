import pygame
from entities.player import Player
from entities.wasp import Wasp  
from environment.platform import Platform
from game_states.gameover import gameoverscreen
from entities.leafarmour import Leafarmour
from entities.magpie import Magpie
from game_states.arena import arena


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Platformer Game')

def draw_gradient_rect(screen, start_x, end_x, y, height, camera_x):
    width = end_x - start_x
    for i in range(width):
        ratio = i / width
        r = int(255 * ratio)  # from 0 to 255
        g = int(255 * ratio)  # from 0 to 255
        b = 0  # yellow fade to arena
        color = (r, g, b)
        pygame.draw.rect(screen, color, (start_x + i - camera_x, y, 1, height))



def level():
    player = Player(100, 250) #player position

    #enemy positions below
    enemies = [
        Wasp(400, 500), Wasp(900, 480), Wasp(1300, 500), Wasp(1600, 450),
        Wasp(1950, 300), Wasp(2400, 500), Wasp(3300, 400),  Wasp(4900, 520),
        Magpie(1425, -400), Magpie(2500, -400), Magpie(4750, -350),
    ]
    #platform positions below
    platforms = [
        Platform(200, 550, 300, 10), Platform(450, 450, 300, 10), Platform(100, 350, 200, 10),
        Platform(700, 450, 300, 10), Platform(950, 350, 200, 10), Platform(1100, 400, 200, 10),
        Platform(1350, 300, 300, 10), Platform(1350, 550, 300, 10), Platform(1650, 450, 200, 10),
        Platform(1850, 350, 300, 10), Platform(1850, 500, 200, 10), Platform(2200, 400, 300, 10),
        Platform(2150, 500, 300, 10), Platform(2500, 450, 300, 10), Platform(2750, 350, 200, 10),
        Platform(3000, 550, 200, 10), Platform(3250, 450, 100, 10), Platform(3400, 550, 200, 10),
        Platform(3400, 300, 200, 10), Platform(3500, 600, 2000, 30), Platform(4600, 500, 300, 10), 
        Platform(4800, 400, 300, 10), Platform(5000, 300, 300, 10) #probably a better way of doing this
    ]
    items = [
        Leafarmour(700, 420),
        Leafarmour(2400, 460),
        Leafarmour(4600, 450)
    ]
    camera = {'x': 0, 'y': 0} #camera
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

        # camera to follow player
        camera['x'] = player.rect.centerx - screen.get_width() // 2
        camera['y'] = player.rect.centery - screen.get_height() // 2

        # update enemies
        for enemy in enemies:
            enemy.update(player, camera, screen.get_width(), screen.get_height())
            enemy.draw(screen, camera)

        current_time = pygame.time.get_ticks()
        for enemy in enemies:
            enemy.apply_damage(player, current_time)

        # draw platforms
        for platform in platforms:
            platform.draw(screen, camera)

                
        
        

        # gradient zone will teleport player to arena
        gradient_start = 5500
        gradient_end = 5700
        draw_gradient_rect(screen, gradient_start, gradient_end, 0, screen.get_height(), camera['x'])
        teleport_zone = pygame.Rect(gradient_start, 0, gradient_end - gradient_start, screen.get_height())
        if player.rect.colliderect(teleport_zone):
            return arena(screen)  # arena


        # draw player
        player.draw(screen, camera)

        # boss zone messages
        font = pygame.font.Font(None, 48)
        if 4000 <= player.rect.x < 4750:
            text = font.render("RECKLESS CHALLENGER, AREN'T YOU?", True, (255, 255, 255))
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 150))
        elif 4750 <= player.rect.x < 5500:
            text = font.render("Very well. Enter my domain.", True, (255, 0, 0))
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 150))

        # Leafarmour logic
        for armour in items:
            if not armour.collected:
                armour.collect(player.rect, keys, player)
                instruction_font = pygame.font.Font(None, 24)
                instruction_text = instruction_font.render("Press ↑ arrow key here", True, (255, 255, 255))
                instruction_pos = (armour.rect.centerx - camera['x'] - instruction_text.get_width() // 2,
                                   armour.rect.top - camera['y'] - 20)
                screen.blit(instruction_text, instruction_pos)

            if not armour.collected:
                armour.draw(screen, camera)
            elif player.has_leafarmour:
                armour.rect.topleft = (player.rect.centerx + 5, player.rect.top + 10)
                adjusted_rect = armour.rect.move(-camera['x'], -camera['y'])
                screen.blit(armour.image, adjusted_rect)

        # HUD
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_text, (10, 10))

        if player.has_leafarmour:
            shield_text = font.render(f"Shield: {player.shield_points}", True, (0, 255, 0))
            screen.blit(shield_text, (10, 50))

        # DYING
        if player.rect.top > screen.get_height() or player.health <= 0:
            retry = gameoverscreen(screen)
            return level() if retry else None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()