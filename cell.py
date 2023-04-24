import pygame
from pygame.sprite import Sprite
from settings import Settings
class Cell(Sprite):
    def __init__(self, screen):
        self.settings = Settings()
        super(Cell, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(self.settings.WINDOW_WIDTH/2, self.settings.WINDOW_HEIGHT/2, self.settings.BLOCKSIZE, self.settings.BLOCKSIZE)
        self.color = self.settings.REDS[39]
        
    def update(self):
        print('updating')
        
        # self.rect.x += self.settings.BLOCKSIZE
        # if self.rect.x >= self.settings.WINDOW_WIDTH:
        #     self.rect.x -= self.settings.WINDOW_WIDTH
        # if self.rect.y >= self.settings.WINDOW_HEIGHT:
        #     self.rect.y -= self.settings.WINDOW_HEIGHT
        # self.rect.y += self.settings.BLOCKSIZE
        pygame.draw.rect(self.screen, self.color, self.rect)