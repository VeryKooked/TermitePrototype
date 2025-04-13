import pygame
import math
import random
from entities.base import Entity  

class Ant(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 60)
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 255, 0))  # big yellow square for boss
        self.max_health = 100
        self.health = 100
        self.state = 'idle' 
        self.cooldown = 2000  # cooldown in milliseconds
        self.last_attack = pygame.time.get_ticks()
        self.projectiles = []

        # jumping
        self.jump_timer = 0 
        self.jump_interval = 5000  # jump every 5 seconds
        self.jump_force = -30  

        # damage cooldown during dash attack
        self.contact_damage_timer = 0
        self.contact_damage_cooldown = 1000  # 1 second

    def update(self, player, platforms):
        now = pygame.time.get_ticks()

        # periodic jumping motion
        if now - self.jump_timer > self.jump_interval and self.on_ground:
            self.vel_y = self.jump_force
            self.jump_timer = now

        # attacks
        if now - self.last_attack > self.cooldown:
            self.choose_attack(player)
            self.last_attack = now

        # Handle specific states
        if self.state == 'plunging':
            pass  # gravity handled already
        elif self.state == 'dashing':
            if abs(self.rect.centerx - player.rect.centerx) < 20:
                self.vel_x = 0
                self.state = 'idle'
        elif self.state == 'shooting':
            if len(self.projectiles) == 0:
                self.shoot_projectiles()
            self.state = 'idle'

        self.move(platforms)

        # damage done
        if self.rect.colliderect(player.rect):
            if now - self.contact_damage_timer > self.contact_damage_cooldown:
                player.health -= 2
                self.contact_damage_timer = now

        # projectiles
        for bullet in self.projectiles[:]:
            bullet['pos'][0] += bullet['vel'][0]
            bullet['pos'][1] += bullet['vel'][1]

            bullet_rect = pygame.Rect(bullet['pos'][0], bullet['pos'][1], 15, 15)
            if bullet_rect.colliderect(player.rect):
                player.health -= 1  # 1 damage from projectile
                self.projectiles.remove(bullet)

    def choose_attack(self, player):
        choice = random.choice(['plunge', 'dash', 'shoot'])
        if choice == 'plunge':
            self.plunge(player)
        elif choice == 'dash':
            self.dash(player)
        elif choice == 'shoot':
            self.state = 'shooting'

    def plunge(self, player):
        if self.rect.y < player.rect.y:
            self.state = 'plunging'
            self.vel_y = 15

    def dash(self, player):
        self.state = 'dashing'
        direction = 1 if player.rect.x > self.rect.x else -1
        self.vel_x = 15 * direction

    def shoot_projectiles(self):
        self.projectiles = []
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
        for dx, dy in directions:
            velocity = [dx * 5, dy * 5]
            self.projectiles.append({'pos': [self.rect.centerx, self.rect.centery], 'vel': velocity})

    def draw(self, screen, camera):
        screen.blit(self.image, (self.rect.x - camera['x'], self.rect.y - camera['y']))

        # drawing projectiles
        for bullet in self.projectiles:
            pygame.draw.circle(screen, (255, 200, 0), 
                (int(bullet['pos'][0] - camera['x']), int(bullet['pos'][1] - camera['y'])), 5)

        # drawing boss HP bar
        bar_x = 200
        bar_y = 20
        bar_width = 400
        bar_height = 20
        health_ratio = self.health / self.max_health

        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))  # background
        pygame.draw.rect(screen, (255, 100, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))  # health fill

        font = pygame.font.Font(None, 24)
        text = font.render(f"Boss HP: {self.health}", True, (255, 255, 255))
        screen.blit(text, (bar_x + 5, bar_y - 22))