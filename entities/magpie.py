import pygame
from entities.base import Entity

class Magpie(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 60)
        self.image = pygame.Surface((150, 100))
        self.image.fill((255, 255, 255))
        self.start_x = x
        self.start_y = y
        self.swoop_speed = 16
        self.state = 'waiting'
        self.timer = 0
        self.delay = 40
        self.rect = self.image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 24)
        self.damage = 4
        self.damage_cooldown = 1000
        self.last_hit_time = 0

    def update(self, player, camera, screen_width, screen_height):
        view_rect = pygame.Rect(camera['x'], camera['y'], screen_width, screen_height)


        if self.state == 'waiting':
            self.timer += 1
            if self.timer >= self.delay:
                self.state = 'swooping'
                self.timer = 0

        elif self.state == 'swooping':
            self.rect.y += self.swoop_speed
            if self.rect.top > screen_height + 200:
                self.state = 'resetting'

        elif self.state == 'resetting':
            self.rect.topleft = (self.start_x, self.start_y)
            self.state = 'waiting'
            self.timer = 0

    def apply_damage(self, player, current_time):
        if self.rect.colliderect(player.rect):
            if current_time - self.last_hit_time > self.damage_cooldown:
                if player.has_leafarmour and player.shield_points > 0:
                    player.shield_points -= 1
                    print(f"[Magpie] Shield hit! Remaining shield: {player.shield_points}")
                    if player.shield_points <= 0:
                        player.has_leafarmour = False
                        print("Leafarmour shattered!")
                else:
                    player.health -= self.damage
                    print(f"[Magpie] Player HP: {player.health}")
                self.last_hit_time = current_time

    def draw(self, screen, camera):
        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
        screen.blit(self.image, adjusted_rect)
        label = self.font.render("Magpie", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.rect.centerx - camera['x'], self.rect.top - 10 - camera['y']))
        screen.blit(label, label_rect)
