import pygame
from entities.base import Entity

class Wasp(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.image = pygame.Surface((15, 25))
        self.image.fill((255, 0, 0))
        self.health = 3
        self.speed = 1.5
        self.rect = self.image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 24)
        self.active = False
        self.damage = 1
        self.damage_cooldown = 1000
        self.last_hit_time = 0

    def update(self, player, camera, screen_width, screen_height):
        view_rect = pygame.Rect(camera['x'], camera['y'], screen_width, screen_height)

        if not self.active and self.rect.colliderect(view_rect):
            self.active = True
            print(f"Wasp at {self.rect.topleft} activated!")

        if not self.active:
            return

        # Chase player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max((dx ** 2 + dy ** 2) ** 0.5, 0.0001)
        dx /= distance
        dy /= distance
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def apply_damage(self, player, current_time):
        if self.rect.colliderect(player.rect):
            if current_time - self.last_hit_time > self.damage_cooldown:
                if player.has_leafarmour and player.shield_points > 0:
                    player.shield_points -= 1
                    print(f"[Wasp] Shield hit! Remaining shield: {player.shield_points}")
                    if player.shield_points <= 0:
                        player.has_leafarmour = False
                        print("Leafarmour shattered!")
                else:
                    player.health -= self.damage
                    print(f"[Wasp] Player HP: {player.health}")
                self.last_hit_time = current_time

    def draw(self, screen, camera):
        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
        screen.blit(self.image, adjusted_rect)
        label = self.font.render("Wasp", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.rect.centerx - camera['x'], self.rect.top - 10 - camera['y']))
        screen.blit(label, label_rect)
