
import pygame


class MainMenu:
    def __init__(self):
        self.options = ["Start Game", "Quit"]
        self.selected_option = 0

    def display(self, screen):
        font = pygame.font.SysFont('Arial', 36)
        screen.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            cursor = ">" if index == self.selected_option else " "
            text = font.render(f"{cursor} {option}", True, (255, 255, 255))
            screen.blit(text, (150, 100 + index * 50))

    def handle_input(self, input):
        if input == 'up':
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif input == 'down':
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif input == 'enter':
            return self.options[self.selected_option]
        return None
