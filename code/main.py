import sys

import pygame

from settings import *
from level import Level

class StartButton:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 255)
        self.active_color = (200, 200, 200)
        self.inactive_color = (150, 150, 150)
        self.active = False

    def draw(self, screen):
        color = self.active_color if self.active else self.inactive_color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pydew Valley')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.is_running = False  # Oyun başladığında True olacak

    def start_game(self):
        self.is_running = True

    def run(self):
        start_button = StartButton(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 100, "Başlat", self.start_game)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                start_button.handle_event(event)  # Düğme olaylarını yönet

            dt = self.clock.tick() / 1000

            if self.is_running:
                self.level.run(dt)
            else:            
                self.screen.fill((0, 0, 0))  # Ekranı temizle
                start_button.draw(self.screen)  # Başlatma düğmesini çiz
  

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
